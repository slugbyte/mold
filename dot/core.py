import os
import env
from shutil import copyfile
from pathlib import Path

_TYPE = ''

def get_type_dir():
    return env.ROOT_DIR + '/' + _TYPE 

def _help():
    print(f'''
USAGE: dot {_TYPE} [*OPTIONS] [FILENAME]
    dot {_TYPE} helps manage file assets that you want to often need to {_TYPE} in a directory.

    If you want {_TYPE} a {_TYPE} file just run... 
    dot {_TYPE} <filename> 

    If you need to manage {_TYPE} files use the folling options.

    OPTIONS: 
        make <filename>  create and edit an empty {_TYPE}file
        load <filepath>  create a {_TYPE} file from an existing file 
        list <filename>  list all the {_TYPE} files
        edit <filename>  edit a {_TYPE} file
        nuke <filename>  remove a {_TYPE} file
        help | -h | --help  print this help
    '''.strip())

def _make_help():
    print(f'''
USAGE: dot {_TYPE} make <filename>
    '''.strip())

def _make_complete():
    return  print('')

def _make(args):
    if len(args) != 1 or args[0] == 'help':
        return _make_help()
    if args[0] == '____COMPLETE____':
        return _make_complete()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    os.system(env.EDITOR + ' ' + filepath)
    if Path(filepath).exists():
        print('MADE FILE:', filename)
    else:
        print(f'MAKE ABORTED: {filename} not created')

def _list_help():
    print(f'''
USAGE: dot {_TYPE} list
    '''.strip())

def _list_complete():
    return  print('')

def _list(args):
    if len(args) == 0:
        print('\n'.join(os.listdir(get_type_dir())))
        return 
    if args[0] == '____COMPLETE____':
        return _list_complete()
    return _list_help()

def _load_help():
    print(f'USAGE: dot {_TYPE} load <filepath> [optional new name]')

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
        copyfile(filepath, get_type_dir() + '/' + filename)
        print(f'LOADED {filename}')
        return 
    print(f'ERROR: no "{filename}" {_TYPE} file found')

def _edit_help():
    print(f'USAGE: dot {_TYPE} edit <filename>')

def _edit_complete(args):
    files = os.listdir(get_type_dir())
    if len(args) == 2:
        for f in files:
            if f == args[1]:
                return print('')
    print(' '.join(os.listdir(get_type_dir())))

def _edit(args):
    if len(args) != 1 or args[0] == 'help':
        return _edit_help()
    if args[0] == '____COMPLETE____':
        return _edit_complete()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    if Path(filepath).exists():
        os.system(env.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" {_TYPE} file found')

def _nuke_help():
    print(f'USAGE: dot {_TYPE} nuke <filename>')

def _nuke_complete(args):
    _edit_complete(args)    

def _nuke(args):
    if len(args) != 1 or args[0] == 'help':
        return _nuke_help()
    if args[0] == '____COMPLETE____':
        return _nuke_complete()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    if Path(filepath).exists():
        os.remove(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" {_TYPE} file found')

def complete(args, _type):
    global _TYPE
    _TYPE=_type
    if len(args) == 0:
        return print('help list make load edit nuke')
    if args[0] == 'help':
        return print('')
    if args[0] == 'list':
        return print('')
    if args[0] == 'make':
        return _make_complete()
    if args[0] == 'load':
        return _load_complete()
    if args[0] == 'edit':
        return _edit_complete(args)
    if args[0] == 'nuke':
        return _nuke_complete(args)
    return print('help list make load edit nuke')

def core(options, _type):
    global _TYPE
    _TYPE=_type
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
