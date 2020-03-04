# works well for I/O intensive tasks
# such as high loaded webserver, and web spider
import requests  
import time  
import asyncio  
import threading  
  
loop = asyncio.get_event_loop()  
url = 'https://www.google.com.tw/'  
  
class Timer:  
    def __init__(self, do_start=True):  
        if do_start:  
            self.start()  
  
    def start(self):  
        self.st = time.time()  
  
    def end(self):  
        self.et = time.time()  
        return self.et - self.st  
  
  
async def send_req(url):  
    _st = time.time()  
    print("Send a request to {}...".format(url))
    # register a new event: requests.get(url) ends;  
    res = await loop.run_in_executor(None, requests.get, url)
    # callback: 
    _diff = time.time() - _st  
    print("Receive a response for {:.02f} second(s).".format(_diff))  
  
  
def other_tasks():  
    _st = time.time()  
    time.sleep(0.5)  
    _diff = time.time() - _st  
    print("Other task took {:.01f} second(s).".format(_diff))  
  
  
num_of_req = 10  
timer = Timer()  
  
# 1) Let high IO tasks be handled in asyncio way  
tasks = []  
for i in range(num_of_req):  
    task = loop.create_task(send_req(url))  
    tasks.append(task)  
  
future_thd = threading.Thread(target=loop.run_until_complete, args=(asyncio.wait(tasks),))  
future_thd.start()  
  
# 2) Executing normal tasks while waiting the asyncio tasks  
for i in range(num_of_req):  
    other_tasks()  
  
  
# 3) Wait for thread of asyncio tasks to complete
future_thd.join()
  
  
loop.close()  
print("After {} request(s), {:.02f} second(s) passed!".format(num_of_req, timer.end()))