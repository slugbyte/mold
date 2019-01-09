''' 
defines a function name query for safly accsting collections
'''

import mold.env as env

def query(collection, key):
    try:
        return collection[key]
    except:
        return None
