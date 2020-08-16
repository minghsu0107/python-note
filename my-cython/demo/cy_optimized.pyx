from cython.parallel import prange, threadid
import numpy as np
from libc.stdio cimport printf
from libc.math cimport pow

# "cimport" is used to import special compile-time information
# about the numpy module (this is stored in a file numpy.pxd which is
# currently part of the Cython distribution).
cimport numpy as np
cimport cython


cdef double square_and_add(double x):
    """Compute x^2 + x as double.

    This is a cdef function that can be called from within
    a Cython program, but not from Python.
    """
    return pow(x, 2.0) + x

cpdef print_result(double x):
    """This is a cpdef function that can be called from Python."""
    print("({} ^ 2) + {} = {}".format(x, x, square_and_add(x)))


cpdef int test_for_loop(int x):
    cpdef int y = 0
    cpdef int i
    for i in range(x):
        y += i
    return y


# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
DTYPE = np.int

# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.int_t DTYPE_t

# "def" can type its arguments but not have a return type. The type of the
# arguments for a "def" function is checked at run-time when entering the
# function.
#
# The arrays f, g and h is typed as "np.ndarray" instances. The only effect
# this has is to a) insert checks that the function arguments really are
# NumPy arrays, and b) make some attribute access like f.shape[0] much
# more efficient. (In this example this doesn't matter though.)


@cython.boundscheck(False)  # turn off bounds-checking for entire function
# turn off negative index wrapping for entire function
@cython.wraparound(False)
def naive_convolve1(np.ndarray[DTYPE_t, ndim=2] f, np.ndarray[DTYPE_t, ndim=2] g):
    if g.shape[0] % 2 != 1 or g.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")
    assert f.dtype == DTYPE and g.dtype == DTYPE

    # The "cdef" keyword is also used within functions to type variables. It
    # can only be used at the top indentation level (there are non-trivial
    # problems with allowing them in other places, though we'd love to see
    # good and thought out proposals for it).
    #
    # For the indices, the "int" type is used. This corresponds to a C int,
    # other C types (like "unsigned int") could have been used instead.
    # Purists could use "Py_ssize_t" which is the proper Python type for
    # array indices.
    cdef int vmax = f.shape[0]
    cdef int wmax = f.shape[1]
    cdef int smax = g.shape[0]
    cdef int tmax = g.shape[1]
    cdef int smid = smax // 2
    cdef int tmid = tmax // 2
    cdef int xmax = vmax + 2 * smid
    cdef int ymax = wmax + 2 * tmid
    # specify ndim for efficient indexing
    cdef np.ndarray[DTYPE_t, ndim= 2] h = np.zeros([xmax, ymax], dtype=DTYPE)
    cdef int x, y, s, t, v, w

    # It is very important to type ALL your variables. You do not get any
    # warnings if not, only much slower code (they are implicitly typed as
    # Python objects).
    cdef int s_from, s_to, t_from, t_to

    # For the value variable, we want to use the same data type as is
    # stored in the array, so we use "DTYPE_t" as defined above.
    # NB! An important side-effect of this is that if "value" overflows its
    # datatype size, it will simply wrap around like in C, rather than raise
    # an error like in Python.
    cdef DTYPE_t value
    for x in range(xmax):
        for y in range(ymax):
            s_from = max(smid - x, -smid)
            s_to = min((xmax - x) - smid, smid + 1)
            t_from = max(tmid - y, -tmid)
            t_to = min((ymax - y) - tmid, tmid + 1)
            value = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v = x - smid + s
                    w = y - tmid + t
                    value += g[smid - s, tmid - t] * f[v, w]
            h[x, y] = value
    return h


@cython.boundscheck(False)
@cython.wraparound(False)
# memoryviews are C structures that can hold a pointer to the data of a NumPy array
# and all the necessary buffer metadata to provide efficient and safe access
def naive_convolve2(DTYPE_t[:, :] f, DTYPE_t[:, :] g):
    if g.shape[0] % 2 != 1 or g.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")

    cdef int vmax = f.shape[0]
    cdef int wmax = f.shape[1]
    cdef int smax = g.shape[0]
    cdef int tmax = g.shape[1]
    cdef int smid = smax // 2
    cdef int tmid = tmax // 2
    cdef int xmax = vmax + 2 * smid
    cdef int ymax = wmax + 2 * tmid
    cdef np.ndarray[DTYPE_t, ndim= 2] h = np.zeros([xmax, ymax], dtype=DTYPE)
    cdef int x, y, s, t, v, w

    cdef int s_from, s_to, t_from, t_to

    cdef DTYPE_t value
    for x in range(xmax):
        for y in range(ymax):
            s_from = max(smid - x, -smid)
            s_to = min((xmax - x) - smid, smid + 1)
            t_from = max(tmid - y, -tmid)
            t_to = min((ymax - y) - tmid, tmid + 1)
            value = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v = x - smid + s
                    w = y - tmid + t
                    value += g[smid - s, tmid - t] * f[v, w]
            h[x, y] = value
    return h


# this can allow your algorithm to work with any libraries supporting the buffer interface
# however, with some speed penalty
def naive_convolve3(object[DTYPE_t, ndim=2] f, object[DTYPE_t, ndim=2] g):
    if g.shape[0] % 2 != 1 or g.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")
    assert f.dtype == DTYPE and g.dtype == DTYPE

    cdef int vmax = f.shape[0]
    cdef int wmax = f.shape[1]
    cdef int smax = g.shape[0]
    cdef int tmax = g.shape[1]
    cdef int smid = smax // 2
    cdef int tmid = tmax // 2
    cdef int xmax = vmax + 2 * smid
    cdef int ymax = wmax + 2 * tmid
    cdef np.ndarray[DTYPE_t, ndim= 2] h = np.zeros([xmax, ymax], dtype=DTYPE)
    cdef int x, y, s, t, v, w

    cdef int s_from, s_to, t_from, t_to

    cdef DTYPE_t value
    for x in range(xmax):
        for y in range(ymax):
            s_from = max(smid - x, -smid)
            s_to = min((xmax - x) - smid, smid + 1)
            t_from = max(tmid - y, -tmid)
            t_to = min((ymax - y) - tmid, tmid + 1)
            value = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v = x - smid + s
                    w = y - tmid + t
                    value += g[smid - s, tmid - t] * f[v, w]
            h[x, y] = value
    return h


# fused type is similar to C++ ‘s templates.
# It generates multiple function declarations at compile time,
# and then chooses the right one at run-time
ctypedef fused my_type:
    int
    double
    cython.longlong

# We declare our plain c function nogil (to release GIL)
cdef my_type clip(my_type a, my_type min_value, my_type max_value) nogil:
    return min(max(a, min_value), max_value)


@cython.boundscheck(False)
@cython.wraparound(False)
def compute(my_type[:, ::1] array_1, my_type[:, ::1] array_2, my_type a, my_type b, my_type c):

    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]

    assert tuple(array_1.shape) == tuple(array_2.shape)

    if my_type is int:
        dtype = np.intc
    elif my_type is double:
        dtype = np.double
    elif my_type is cython.longlong:
        dtype = np.longlong

    result = np.zeros((x_max, y_max), dtype=dtype)
    cdef my_type[:, ::1] result_view = result

    cdef my_type tmp
    cdef Py_ssize_t x, y
    # cdef int thread_id = -1

    # We use prange here.
    # OpenMP automatically starts a thread pool and distributes the work according to the schedule used
    # Variables assigned to in a parallel with block will be private and unusable after the block
    # If num_threads not given, OpenMP will decide how many threads to use
    for x in prange(x_max, nogil=True, schedule='dynamic', num_threads=None):
        #thread_id = threadid()
        #printf("Thread ID: %d\n", thread_id)

        for y in range(y_max):

            tmp = clip(array_1[x, y], 2, 10)
            tmp = tmp * a + array_2[x, y] * b
            if tmp < 0:
                with gil:
                    raise Exception()
            result_view[x, y] = tmp + c

    return result
