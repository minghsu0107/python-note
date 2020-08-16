# works well for I/O intensive tasks
# such as high loaded webserver, and web spider
import requests
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

loop = asyncio.get_event_loop()
url = 'https://www.google.com.tw/'

# 5 threads: concurrency level = 5
# if only 1 thread, the response will be handled sequentially (blockingly) from idx 0 to num_of_req
# even though we register the task in a non-blocking manner
# this is because other tasks will be idled until at least 1 thread in the pool finishes its task
_executor = ThreadPoolExecutor(5)


class Timer:
    def __init__(self, do_start=True):
        if do_start:
            self.start()

    def start(self):
        self.st = time.time()

    def end(self):
        self.et = time.time()
        return self.et - self.st


async def send_req(idx, url):
    _st = time.time()
    print("Send a request to {}..., idx = {}".format(url, idx))
    # register a new event: requests.get(url) ends;
    # python雖然因為GIL，並不能用多核心來同時跑多個線程，
    # 但線程並不會被網路io所阻塞，所以loop.run_in_executor利用這個特性把request.get包裝成一個非阻塞的Future對象
    res = await loop.run_in_executor(_executor, requests.get, url)
    # callback:
    _diff = time.time() - _st
    print(
        "Receive a response for {:.02f} second(s). idx = {}, res = {}".format(_diff, idx, res))


def other_tasks():
    _st = time.time()
    time.sleep(0.1)
    _diff = time.time() - _st
    print("Other task took {:.01f} second(s).".format(_diff))


num_of_req = 10
timer = Timer()

# 1) Let high IO tasks be handled in asyncio way
tasks = []
for i in range(num_of_req):
    task = loop.create_task(send_req(i, url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))

# 2) Executing normal tasks after finishing the asyncio tasks
for i in range(num_of_req):
    other_tasks()


loop.close()
print("After {} request(s), {:.02f} second(s) passed!".format(
    num_of_req, timer.end()))
