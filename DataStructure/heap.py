import heapq as hq
import numpy as np
data = np.arange(10)  # 将生成的数据随机打乱顺序
np.random.shuffle(data)
print(data)
# 定义heap列表
heap = []  # 使用heapq库的heappush函数将数据堆入
for i in data:
    hq.heappush(heap, i)
print(heap)
hq.heappush(heap, 0.5)

hq.heappop(heap)
hq.heappop(heap)

heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
hq.heapify(heap)
print(heap)

print(hq.nlargest(1, heap))
print(hq.nsmallest(1, heap))
