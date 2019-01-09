''' 
defines a function name query for safly accsting collections
'''

import mold.env as env
from mold.color import magenta, reset

def query(collection, key):
    try:
        return collection[key]
    except:
        return None

def debug(*args):
    if env.MOLD_DEBUG:
        print(f'{magenta}_MOLD_DEBUG_:{reset}', *args)
