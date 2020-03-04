import ctypes
from my_extern.extern import run
   

class Wrapper:
    def __init__(self, func_file_name, mes):
        # 動態鍵結
        mes = ctypes.c_char_p(mes.encode('utf-8'))

        self.lib = run(func_file_name)
        self.obj = self.lib.cbacken_new(mes)
        self.func_file_name = func_file_name

    def sort(self, lst, STL=False):
        n = len(lst)
        # init arr
        cb_ARR = ctypes.c_int * n
        cb_arr = cb_ARR()
        for i in range(n):
            if not isinstance(lst[i], int):
                raise ValueError("Only support Integer Array")

            cb_arr[i] = lst[i]
        # init int
        cb_N = ctypes.c_int
        cb_n = cb_N()
        cb_n = n
        # sort
        if STL == False:
            self.lib.cbacken_sort(self.obj, cb_arr, cb_n)
        else:
            self.lib.cbacken_sort2(self.obj, cb_arr, cb_n)
        nlst = [x for x in cb_arr]
        return nlst

if __name__ == '__main__':
    mes = "hello"
    wp = Wrapper("my_clib/extern_c_test2.cpp", mes)
    print(wp.sort([2, 1, 4, 3, 7, 11, 99, 6, 6], STL=False))


