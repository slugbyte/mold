'''
env parses sys.argv, os.environ, and defines mold constants.
'''

import sys 
from os import environ
from  shutil import which

def get(table, prop):
    try:
        return table[prop]
    except:
        return None

# ARG PARSE
ARGV = sys.argv
SUB_COMMAND = get(ARGV, 1)
OPTIONS = ARGV[2:]

# ENVIRON PARSE
HOME = get(environ, 'HOME')
ROOT_DIR = get(environ, 'MOLD_ROOT') or HOME + '/.mold'
EDITOR = get(environ, 'EDITOR') or which('nano')
MOLD_DEBUG_MODE = get(environ, 'MOLD_DEBUG_MODE') 

# completion magic 
MAGIC_MOLD = '__MAGIC_MOLD__'

# CLI EXIT CODES
EXIT_STATUS_OK = 0
EXIT_STATUS_FAIL = 1
EXIT_STATUS_DEVELOPER_TODO = 2

