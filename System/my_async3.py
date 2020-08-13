# works well for I/O intensive tasks
# such as high loaded webserver, and web spider
import requests  
import time  
import asyncio  
from concurrent.futures import ThreadPoolExecutor
  
loop = asyncio.get_event_loop()  
url = 'https://www.google.com.tw/'  

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
    res = await loop.run_in_executor(_executor, requests.get, url)
    # callback: 
    _diff = time.time() - _st  
    print("Receive a response for {:.02f} second(s). idx = {}".format(_diff, idx))  
  
  
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
    task = loop.create_task(send_req(i, url))  
    tasks.append(task)  

loop.run_until_complete(asyncio.wait(tasks))
  
# 2) Executing normal tasks while waiting the asyncio tasks  
for i in range(num_of_req):  
    other_tasks()
  
  
loop.close()  
print("After {} request(s), {:.02f} second(s) passed!".format(num_of_req, timer.end()))