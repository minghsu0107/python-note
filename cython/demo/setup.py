from distutils.core import Extension, setup
from Cython.Build import cythonize
import numpy
import os

os.environ['CFLAGS'] = f'-stdlib=libc++ -I {numpy.get_include()}'

# define an extension that will be cythonized and compiled
ext = Extension(name="cy_optimized",
                sources=["cy_optimized.pyx"],
                language='c++'
                # extra_compile_args=['-fopenmp', '-O3'], # using openmp for parallelism, O3 optimized
                # extra_link_args=['-fopenmp'],
                )

# specify python3 source
setup(ext_modules=cythonize(ext, compiler_directives={
      'language_level': "3"}), include_dirs=[numpy.get_include()])
