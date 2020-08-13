from multiprocessing import Pool
from multiprocessing import cpu_count

def demo(a, b):
	print(f'{a} + {b} = {a+b}')
	return a + b

pool_sz = min(cpu_count(), 20)
with Pool(pool_sz) as p:
	print(f'pool size: {pool_sz}')
	res = p.starmap(demo, [(i, i) for i in range(10)])
	p.close()
	p.join()

print(res)