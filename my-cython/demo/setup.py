from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled
ext = Extension(name="hello", sources=["hello.pyx"])
# specify python3 source
setup(ext_modules=cythonize(ext, compiler_directives={'language_level' : "3"}))