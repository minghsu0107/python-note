all: linked_list_sparse.so

linked_list_sparse.so: extern_c_test3.o
	gcc -shared -fPIC -o linked_list_sparse.so extern_c_test3.o
	rm -f extern_c_test3.o

extern_c_test3.o: extern_c_test3.c
	gcc -c extern_c_test3.c

clean:
	rm -f linked_list_sparse.so
