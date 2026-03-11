assert 0, "ver 0.0.1 isn't support"

from os import symlink as __sym_link__
from os.path import dirname as __get_dir__
from os.path import basename as __base_name__
from PyPInclude import lib as __lib__
from time import time as __time__
from random import random as __random__
from Cython.Build import __cythonize__
from sys import argv as __program_param__
from subprocess import run as __shell__
from os import chdir as __cd__
from os import getcwd as __pwd__
from contextlib import contextmanager as __wither__

__all__ = []

__lib_pw__ = hash(str(__time__() + __random__()))

__libsetter__ = __lib__("lcl", __lib_pw__)

del __lib_pw__

@__wither__
def enter_directory(dir):
    ret = __pwd__()
    try:
        __cd__(dir)
        yield __pwd__()
    finally: __cd__(ret)

@(-__libsetter__)
def effected_cythonize(*argv, **kargv):
    """
    # function effected_cythonize

    use side-effect to make setup.py as cythonize builder

    forse the program's parameter as "setup.py build_ext --inplace"
    
     - fin - 
    """
    
    L_minus_3 = len(__program_param__) - 3
    if L_minus_3 < 0:
        __program_param__.extend(["" for _ in range(-L_minus_3)])
    __program_param__[1] = "build_ext"
    __program_param__[2] = "--inplace"
    
    return cythonize(*argv, **kargv)

@(-)


@(-__libsetter__)
def initalize(file):
    __PyPInclude__ = __get_dir__(file)
    __lcl__ = __get_dir__(__file__)
    
    include = __path_join__(__PyPInclude__, "include")
    
    __lcl__linkpath = __path_join__(include, "__lcl__")
    lcl_pkg_link_path = __path_join__(__lcl__, __base_name__(__dir_name__(__PyPInclude__)))
    
    __sym_link__(__lcl__linkpath, __lcl__)
    __sym_link__(lcl_pkg_link_path, include)
