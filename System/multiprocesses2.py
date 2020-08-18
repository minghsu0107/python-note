from multiprocessing import Pool
from multiprocessing import cpu_count


def demo(a, b):
    print(f'{a} + {b} = {a+b}')
    return a + b


def main():
    pool_sz = min(cpu_count(), 20)
    with Pool(pool_sz) as p:
        print(f'pool size: {pool_sz}')
        res = p.starmap(demo, [(i, i) for i in range(10)])
        p.close()
        p.join()

    print(res)


def main2():
    pool_sz = min(cpu_count(), 20)
    with Pool(pool_sz) as p:
        print(f'pool size: {pool_sz}')
        # returns immediately
        cb = p.starmap_async(demo, [(i, i) for i in range(10)])
        res = cb.get()
        p.close()
        p.join()

    print(res)


if __name__ == '__main__':
    main()
    main2()
