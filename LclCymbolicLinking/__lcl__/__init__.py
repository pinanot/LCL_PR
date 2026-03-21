assert 0, "ver 0.0.1 isn't support"

from os import symlink as __sym_link__
from os.path import dirname as __get_dir__
from os.path import basename as __base_name__
from os.path import isdir as __is_dir__
from os.path import islink as __is_link__
from os.path import isfile as __is_file__
from os.path import realpath as __get_real_path__
from PyPInclude import lib as __lib__
from martialaw import partial as __partial__
from functools import wraps as __smart_deco_wraps__
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

@-__libsetter__
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

@-__lib_setter__
def run_setup(__file__):
    with enter_directory(__get_dir__(__file__)) as dirpath: return __shell__(["python", "setup.py"])

def initialize_core(file, *, on_pypi_pkg = True):
    __PyPInclude__ = __get_dir__(file)
    __lcl__ = __get_dir__(__file__)
    
    include = __path_join__(__PyPInclude__, "include") if on_pypi_pkg else __PyPInclude__
    
    __lcl__linkpath = __path_join__(include, "__lcl__")
    lcl_pkg_link_path = __path_join__(__lcl__, __base_name__(__dir_name__(__PyPInclude__))) if on_pypi_pkg else __base_name__(__PyPInclude__)
    
    __sym_link__(__lcl__linkpath, __lcl__)
    __sym_link__(lcl_pkg_link_path, include)

@-__libsetter__
@lambda f : __smart_deco_wraps__(f)(partial(initialize_core, on_pypi_pkg = True))
def initialize(__file__):
    """
    # function initialize(__file__)
    
     - fin -
    """
    
    pass

@-__libsetter__
@lambda f : __smart_deco_wraps__(f)(partial(initialize_core, on_pypi_pkg = False))
def init_dir(__file__):
    """
    # function init_dir(__file__)
    
     - fin -
    """
    
    pass

is_same_real_path = lambda x, y : __get_real_path__(x) == __get_real__path(y)
is_dir_link = lambda x : __is_link__(x) and __is_dir__(x)

@(-__libsetter__)
def get_lcl_project_info(file, *, lclpath = __get_dir__(__file__), raises = False):
    """
    # function get_lcl_project_info(file, *, lclpath = default path, rasies = False)
    
     - fin -
    """
    if raise:
        ret = lib.lcl.get_lcl_project_info(file, lclpath = lclpath, raises = False)
        if type(ret) == tuple: return ret
        else: raise ret
    else:
        __PyPInclude__ = __get_dir__(file)
        if is_dir_link(
            __lcl__ := __path_join__(
                __PyPInclude__,
                "__lcl__"
            )
        ) and is_dir_link(
            pkgname_link := __path_join__(
                lclpath,
                pkgname := __base_name__(
                    __PyPInclude__
                )
            )
        ):
            if is_same_real_path(
                __PyPInclude__,
                pkgname_link
            ) and is_same_real_path(
                lclpath,
                __lcl__
            ): return pkgname, pkgname_link, __lcl__
            else: return NotLclProjectError(f"{pkgname} is not lcl project s.t. installed on lcl")
        elif __is_dir__(
            include := __path_join__(
                __PyPInclude__,
                "include"
            )
        ) and is_dir_link(
            pkgname_link := __path_join__(
                lclpath,
                pkgname := __base_name__(
                    __get_dir__(
                        __PyPInclude__
                    )
                )
            )
        ):
            if is_dir_link(
                __lcl__ := __path_join__(
                    include,
                    "__lcl__"
                )
            ): 
                if is_same_real_path(
                    include,
                    pkgname_link
                ) and is_same_real_path(
                    lclpath,
                    __lcl__
                ): return pkgname, pkgname_link, __lcl__
                else: return NotLclProjectError(f"{pkgname} is not lcl project s.t. installed on lcl")
            else: NotLclProjectError(f"{pkgname} is not lcl project s.t. installed on lcl")
    else: return NotLclProjectError(f"{file} is not in lcl project")

@-__libsetter__
def uninstall_lclproject(file, *, lclpath = __get_dir__(__file__)):
    pkgname, pkgname_link, __lcl__ = lib.lcl.get_lcl_project_info(file, lclpath = lclpath, raises = True)
    pass