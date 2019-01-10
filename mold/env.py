'''
env parses sys.argv, os.environ, and defines mold constants.
'''

# import sys 
# from os import environ
# from shutil import which
# from mold.util import query

# # ENVIRON PARSE
# HOME = query(environ, 'HOME')
# ROOT_DIR = query(environ, 'MOLD_ROOT') or HOME + '/.mold'
# EDITOR = query(environ, 'EDITOR') or which('nano')
# MOLD_DEBUG = bool(query(environ, 'MOLD_DEBUG'))
# MOLD_COLOR = bool(query(environ, 'MOLD_COLOR'))

# # completion magic 
# MAGIC_MOLD = '__MAGIC_MOLD__'

# # CLI EXIT CODES
# EXIT_STATUS_OK = 0
# EXIT_STATUS_FAIL = 1
# EXIT_STATUS_DEVELOPER_TODO = 2

