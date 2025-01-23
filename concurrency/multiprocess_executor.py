import concurrent.futures as cf
import logging
import math
import numpy as np
import time
import threading

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format,
                    level=logging.INFO, datefmt="%H:%M:%S")

r_lists = [[np.random.randint(500000) for _ in range(3000)]
           for _ in range(1000)]


def merge(l_1, l_2):
    out = []
    key_1 = 0
    key_2 = 0
    for i in range(len(l_1) + len(l_2)):
        if l_1[key_1] < l_2[key_2]:
            out.append(l_1[key_1])
            key_1 += 1
            if key_1 == len(l_1):
                out = out + l_2[key_2:]
                break
        else:
            out.append(l_2[key_2])
            key_2 += 1
            if key_2 == len(l_2):
                out = out + l_1[key_1:]
                break
    return out


def merge_sort(l):
    if len(l) == 1:
        return l
    mid_point = math.floor((len(l) + 1) / 2)
    l_1, l_2 = merge_sort(l[:mid_point]), merge_sort(l[mid_point:])
    out = merge(l_1, l_2)
    del l_1, l_2
    return out


# By default, the number of processes
# is equal to the number of processors on the machine.
if __name__ == '__main__':
    logging.info("Starting Sorting")
    with cf.ProcessPoolExecutor() as executor:
        sorted_lists_futures = [executor.submit(
            merge_sort, r_list) for r_list in r_lists]
    logging.info("Sorting Completed")
    for future in sorted_lists_futures:
        print(future.result())
