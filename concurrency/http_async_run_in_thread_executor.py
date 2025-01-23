# works well for I/O intensive tasks
# such as high loaded webserver, and web spider
import requests
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor


class Timer:
    def __init__(self, do_start=True):
        if do_start:
            self.start()

    def start(self):
        self.st = time.time()

    def end(self):
        self.et = time.time()
        return self.et - self.st


async def send_req(loop, executor, idx, url):
    _st = time.time()
    print("Send a request to {}..., idx = {}".format(url, idx))
    # python雖然因為GIL，並不能用多核心來同時跑多個線程，
    # 但線程並不會被網路io所阻塞，所以loop.run_in_executor利用這個特性把request.get包裝成一個非阻塞的Future對象
    s = requests.Session()
    # headers = {'content-type': 'application/json'}
    # s.headers.update(headers)
    res = await loop.run_in_executor(executor, s.get, url)
    # callback:
    _diff = time.time() - _st
    print(
        "Receive a response for {:.02f} second(s). idx = {}, res = {}".format(_diff, idx, res))
    return idx


def other_tasks():
    _st = time.time()
    time.sleep(0.1)
    _diff = time.time() - _st
    print("Other task took {:.01f} second(s).".format(_diff))


def main():
    loop = asyncio.get_event_loop()
    url = 'https://www.google.com.tw/'
    num_of_req = 10
    timer = Timer()

    # 5 threads: concurrency level = 5
    # if only 1 thread, the response will be handled sequentially (blockingly) from idx 0 to num_of_req
    # even though we register the task in a non-blocking manner
    # this is because other tasks will be idled until at least 1 thread in the pool finishes its task
    executor = ThreadPoolExecutor(5)

    # 1) Let high IO tasks be handled in asyncio way
    tasks = []
    for i in range(num_of_req):
        task = loop.create_task(send_req(loop, executor, i, url))
        tasks.append(task)

    # blocking
    results = loop.run_until_complete(asyncio.gather(*tasks))
    print(results) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 2) Executing normal tasks after finishing the asyncio tasks
    for i in range(num_of_req):
        other_tasks()

    loop.close()
    print("After {} request(s), {:.02f} second(s) passed!".format(
        num_of_req, timer.end()))


if __name__ == "__main__":
    main()
