assert 0, "ver 0.0.1 isn't support"

from os import symlink as __sym_link__
from os.path import dirname as __get_dir__
from os.path import basename as __base_name__
from PyPInclude import lib as __lib__
from time import time as __time__
from random import random as __random__

__all__ = []

__lib_pw__ = hash(str(__time__() + __random__()))

__libsetter__ = __lib__("lcl", __lib_pw__)

del __lib_pw__

@(-__libsetter__)
def initalize(file):
    __PyPInclude__ = __get_dir__(file)
    __lcl__ = __get_dir__(__file__)
    
    include = __path_join__(__PyPInclude__, "include")
    
    __lcl__linkpath = __path_join__(include, "__lcl__")
    lcl_pkg_link_path = __path_join__(__lcl__, __base_name__(__dir_name__(__PyPInclude__)))
    
    __sym_link__(__lcl__linkpath, __lcl__)
    __sym_link__(lcl_pkg_link_path, include)