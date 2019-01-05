import os
import env
from shutil import copyfile
from pathlib import Path

_DROP_DIR = env.ROOT_DIR + '/drop'

def _help():
    print('''
USAGE: dot drop [*OPTIONS] [FILENAME]
    dot drop helps manage file assets that you want to often need to drop in a directory.

    If you want drop a dropfile just run... 
    dot drop <filename> 

    If you need to manage dropfiles use the folling options.

    OPTIONS: 
        make <filename>  create and edit an empty dropfile
        load <filepath>  create a drop file from an existing file 
        list <filename>  list all the dropfiles
        edit <filename>  edit a dropfile
        nuke <filename>  remove a drop file
        help | -h | --help  print this help
    '''.strip())

def _make_help():
    print('''
USAGE: dot drop make <filename>
    '''.strip())

def _make_complete():
    return  print('')

def _make(args):
    if len(args) != 1 or args[0] == 'help':
        return _make_help()
    if args[0] == '____COMPLETE____':
        return _make_complete()
    filename = args[0]
    filepath = _DROP_DIR + '/' + filename
    os.system(env.EDITOR + ' ' + filepath)
    if Path(filepath).exists():
        print('MADE DROPFILE:', filename)
    else:
        print(f'MAKE ABORTED: {filename} not created')

def _list_help():
    print('''
USAGE: dot drop list
    '''.strip())

def _list_complete():
    return  print('')

def _list(args):
    if len(args) == 0:
        print('\n'.join(os.listdir(_DROP_DIR)))
        return 
    if args[0] == '____COMPLETE____':
        return _list_complete()
    return _list_help()

def _load_help():
    print('USAGE: dot drop load <filepath> [optional new name]')

def _load_complete():
    print(' '.join(os.listdir('./')))
    return  

def _load(args):
    if len(args) < 0 or args[0] == 'help':
        return _load_help()
    if args[0] == '____COMPLETE____':
        return _load_complete()
    filepath = args[0]
    filename = os.path.basename(filepath)
    if len(args) == 2:
        filename = args[1]
    print('len', len(args))
    if Path(filepath).exists():
        copyfile(filepath, _DROP_DIR + '/' + filename)
        print(f'LOADED {filename}')
        return 
    print(f'ERROR: no "{filename}" dropfile found')

def _edit_help():
    print('USAGE: dot drop edit <filename>')

def _edit_complete():
    print(' '.join(os.listdir(_DROP_DIR)))

def _edit(args):
    if len(args) != 1 or args[0] == 'help':
        return _edit_help()
    if args[0] == '____COMPLETE____':
        return _edit_complete()
    filename = args[0]
    filepath = _DROP_DIR + '/' + filename
    if Path(filepath).exists():
        os.system(env.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" dropfile found')

def _nuke_help():
    print('USAGE: dot drop nuke <filename>')

def _nuke_complete():
    _edit_complete()    

def _nuke(args):
    if len(args) != 1 or args[0] == 'help':
        return _nuke_help()
    if args[0] == '____COMPLETE____':
        return _nuke_complete()
    filename = args[0]
    filepath = _DROP_DIR + '/' + filename
    if Path(filepath).exists():
        os.remove(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" dropfile found')

def drop(options):
    if len(options) == 0:
        return _help()
    if options[0] == 'help':
        return _help()
    if options[0] == 'make':
        return _make(options[1:])
    if options[0] == 'load':
        return _load(options[1:])
    if options[0] == 'list':
        return _list(options[1:])
    if options[0] == 'edit':
        return _edit(options[1:])
    if options[0] == 'nuke':
        return _nuke(options[1:])
    return print('CHECK FOR FILES')



