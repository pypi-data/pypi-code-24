from fxcmpy.fxcmpy import fxcmpy as fxcmpy  
from fxcmpy.fxcmpy_open_position import fxcmpy_open_position 
from .fxcmpy_closed_position import *
from .fxcmpy_order import *
from .fxcmpy_oco_order import *

with open('VERSION', 'r') as f:
    __version__ = f.read()


