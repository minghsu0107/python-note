import ctypes
import os


def run(func_file_path):
    so_file_path = func_file_path[:-4] + ".so"
    if not os.path.isfile(so_file_path):
        cmd = "g++ -shared -fPIC " + "-o " + so_file_path + " " + func_file_path
        os.system(cmd)
    ll = ctypes.cdll.LoadLibrary
    lib = ll(so_file_path)
    # os.remove(so_file_path)
    return lib
