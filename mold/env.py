import os 
from  shutil import which

ROOT_DIR = ''
EDITOR = ''
MOLD_DEBUG_MODE = ''

try:
    ROOT_DIR = os.environ['MOLD_ROOT']
except:
    ROOT_DIR = ''

try:
    EDITOR = os.environ['EDITOR']
except:
    EDITOR = which('nano')

try:
    MOLD_DEBUG_MODE = os.environ['MOLD_DEBUG_MODE']
except:
    MOLD_DEBUG_MODE = ''
