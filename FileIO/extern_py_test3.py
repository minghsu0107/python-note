from ctypes import *

class double_row_element(Structure):
    pass

double_row_element._fields_ = \
[("value", c_double), ("col_index", c_int), ("next_element", POINTER(double_row_element))]


class double_sparse_matrix(Structure):
    _fields_ = \
    [("nrows", c_int), ("ncols", c_int), ("nnz", c_int), \
    ("rows", POINTER(POINTER(double_row_element)))]

class SparseMatrixWrapper:
	def __init__(self, nrows=0, ncols=0):
		if not isinstance(nrows, int):
			raise ValueError("nrows should be an integer")
		if not isinstance(ncols, int):
			raise ValueError("ncols should be an integer")

		self.nrows = nrows
		self.ncols = ncols

		self.double_sparse_pointer = POINTER(double_sparse_matrix)
		self.sparse_library = CDLL("my_clib/linked_list_sparse.so")

		self.initialize_matrix = self.sparse_library.initialize_matrix
		self.initialize_matrix.argtypes = [c_int, c_int]
		self.initialize_matrix.restype = self.double_sparse_pointer
		#self.mat = self.double_sparse_pointer()
		self.mat = self.initialize_matrix(self.nrows, self.ncols)

		self.set_value = self.sparse_library.set_value
		self.set_value.argtypes = [self.double_sparse_pointer, c_int, c_int, c_double]
		self.set_value.restype = c_int

		self.get_value = self.sparse_library.get_value
		self.get_value.argtypes = [self.double_sparse_pointer, c_int, c_int]
		self.get_value.restype = c_double

		self.free_matrix = self.sparse_library.free_matrix

	def setValue(self, row, col, val):
		if not isinstance(row, int):
			raise ValueError("row should be an integer")
		if not isinstance(col, int):
			raise ValueError("col should be an integer")
		if not isinstance(val, float):
			raise ValueError("val should be an integer")

		# By default functions are assumed to return the C int type
		# the return type is <class 'int'>
		return self.set_value(self.mat, row, col, val)

	def getValue(self, row, col):
		if not isinstance(row, int):
			raise ValueError("row should be an integer")
		if not isinstance(col, int):
			raise ValueError("col should be an integer")
		# the return type is <class 'float'>
		return self.get_value(self.mat, row, col)

	def traverse(self):
		for i in range(self.mat.contents.nrows):
			a = self.mat.contents.rows[i]
			b = a.contents.next_element
			while (b):
				print(b.contents.value)
				b = b.contents.next_element
	
	def __del__(self):
		if hasattr(self, 'free_matrix'):
			self.free_matrix(self.mat)

if __name__ == "__main__":
	sm = SparseMatrixWrapper(10, 10)
	print(sm.setValue(1, 3, 6.0)) # 0
	print(sm.getValue(1, 3)) # 6.0
	sm.setValue(4, 2, 10.0)
	sm.setValue(4, 7, 13.0)
	sm.setValue(2, 9, 3.0)
	sm.traverse() # 6.0, 3.0, 10.0, 13.0