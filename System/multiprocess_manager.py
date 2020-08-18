# for IPC (inter-process communication)
import multiprocessing
import time


def test(idx, test_dict, lock):
    test_dict[idx] = idx

    lock.acquire()
    # test_dict['test']['hi'] = idx # will not modify test_dict['test']
    d = test_dict['test']
    d['hi'] = idx
    test_dict['test'] = d
    lock.release()


def main():
    # 當我們聲明瞭一個Manager物件的時候, 程式實際在其他程序啟動了一個server服務,
    # 這個server是阻塞的, 以此來實現程序間資料安全
    # slower than the equivalent using shared memory because the objects
    # need to be serialized/deserialized and sent between processes
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    tmp_dict = manager.dict()
    tmp_dict['test'] = {}

    with multiprocessing.Pool(4) as p:
        for i in range(5):
            # p.apply_async: non-blocking registration (returns immediately)
            p.apply_async(test, args=(i, tmp_dict, lock))
        p.close()
        p.join()

    print(tmp_dict)


if __name__ == '__main__':
    main()
