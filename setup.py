from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name = 'Envelope Cython app',
    ext_modules = cythonize("envelope.pyx"),
    include_dirs = [np.get_include()], 
)