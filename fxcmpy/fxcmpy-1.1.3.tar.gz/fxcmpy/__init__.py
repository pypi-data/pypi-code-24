from fxcmpy.fxcmpy import fxcmpy as fxcmpy  
from fxcmpy.fxcmpy_open_position import fxcmpy_open_position 
from .fxcmpy_closed_position import *
from .fxcmpy_order import *
from .fxcmpy_oco_order import *
import os

path = os.path.join(os.path.dirname(__file__), 'VERSION') 

with open(path, 'r') as f:
    __version__ = f.read()


