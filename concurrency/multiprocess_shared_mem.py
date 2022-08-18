from multiprocessing import Pool, Value, Array
import time

# Usage: Array(typecode_or_type, size_or_initializer, *, lock=True)
# 只能接受 1d array
L = Array('d', [1.1, 7.2, 6.3, 5.4])
# Usage: Value(typecode_or_type, *args, lock=True)
# 接受單一數字
# set lock = True for synchronized write
S = Value('i', 3, lock=True)


def run(idx):
    print(f'{idx} start')
    time.sleep(1)
    for i in range(len(L)):
        L[i] = 0
    S.value = idx
    print(f'{idx} end')
    return idx


def main():
    pool_sz = 4
    with Pool(pool_sz) as p:
        print(f'pool size: {pool_sz}')
        # p.map: blocks and does not register new tasks
        # until there exists idle workers in the pool
        res = p.map(run, [idx for idx in range(5)])
        p.close()
        p.join()
        print(res)

    print(L[:], S.value)


if __name__ == '__main__':
    main()
