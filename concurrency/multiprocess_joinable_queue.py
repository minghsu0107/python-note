from time import sleep
from random import random
from multiprocessing import JoinableQueue
from multiprocessing import Process
 

def producer(queue):
    print('Producer starting', flush=True)

    for i in range(10):
        task = (i, random())
        print(f'.producer added {task}', flush=True)
        
        queue.put(task)

    queue.put(None)
    print('Producer finished', flush=True)
 
def consumer(queue):
    print('Consumer starting', flush=True)
    while True:
        task = queue.get()
        # check for signal that we are done
        if task is None:
            break

        sleep(task[1])
        print(f'.consumer got {task}', flush=True)
        # mark the unit of work as processed
        queue.task_done()
    # mark the signal as processed
    queue.task_done()
    print('Consumer finished', flush=True)
 
if __name__ == '__main__':
    queue = JoinableQueue()

    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
  
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()

    producer_process.join()
    print('Main found that the producer has finished', flush=True)

    # wait for the queue to empty
    queue.join()

    print('Main found that all tasks are processed', flush=True)
