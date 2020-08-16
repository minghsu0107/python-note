# Import the extension module hello.
import hello
import timeit


def main():
    # Call the print_result method
    hello.print_result(23.0)

    setup_py = '''
def test_for_loop_py(x):
    y = 0
    for i in range(x):
        y += i
    return y
'''
    cy = timeit.timeit('hello.test_for_loop_cy(500)',
                       setup='import hello', number=1000)
    py = timeit.timeit('test_for_loop_py(500)', setup=setup_py, number=1000)
    print(cy, py)
    print(f'Cython is {py/cy}x faster')


if __name__ == '__main__':
    main()
