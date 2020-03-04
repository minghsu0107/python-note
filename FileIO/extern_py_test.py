from my_extern.extern import run

lib = run("my_clib/extern_c_test.cpp")  
lib.cfoo2(3, 4)  
