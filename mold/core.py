import os
import mold.fs as fs
import mold.env as env

MAGIC_MOLD = '__MAGIC_MOLD__'

# SINGLETON STATE
_TYPE = ''

def set_TYPE(_type):
    global _TYPE
    _TYPE=_type

def get_type_dir():
    return env.ROOT_DIR + '/' + _TYPE 

def _help():
    print(f'''
USAGE: mold {_TYPE} [*OPTIONS] [FILENAME]
    mold {_TYPE} helps manage file assets that you want to often need to {_TYPE} in a directory.

    If you want {_TYPE} a {_TYPE} file just run... 
    mold {_TYPE} <filename> 

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
USAGE: mold {_TYPE} make <filename>
    '''.strip())

def _make_complete():
    return  print(MAGIC_MOLD)

def _make(args):
    if len(args) != 1 or args[0] == 'help':
        return _make_help()
    if args[0] == '____COMPLETE____':
        return _make_complete()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    if _TYPE == 'temp':
        fs.mkdir(filepath)
        os.chdir(filepath)
    exec(env.EDITOR + ' ' + filepath)
    if fs.exists(filepath):
        print('MADE FILE:', filename)
    else:
        print(f'MAKE ABORTED: {filename} not created')

def _list_help():
    print(f'''
USAGE: mold {_TYPE} list
    '''.strip())

def _list_complete():
    return  print('')

def _list(args):
    if len(args) == 0:
        print('\n'.join(fs.listdir(get_type_dir())).replace('.mold', '').strip())
        return 
    if args[0] == '____COMPLETE____':
        return _list_complete()
    return _list_help()

def _load_help():
    print(f'USAGE: mold {_TYPE} load <filepath> [optional new name]')

def _load_complete(args):
    print(MAGIC_MOLD)

def _load(args):
    if len(args) < 0 or args[0] == 'help':
        return _load_help()
    if args[0] == '____COMPLETE____':
        return _load_complete(args)
    filepath = args[0]
    filename = fs.basename(filepath)
    if len(args) == 2:
        filename = args[1]
    if fs.exists(filepath):
        if _TYPE == 'temp':
            fs.copydir(filepath, get_type_dir() + '/' + filename)
        else:
            fs.copy(filepath, get_type_dir() + '/' + filename)
        print(f'LOADED {filename}')
        return 
    print(f'ERROR: no "{filename}" {_TYPE} found')

def _edit_help():
    print(f'USAGE: mold {_TYPE} edit <filename>')

def _edit_complete(args):
    files = fs.listdir(get_type_dir())
    if len(args) == 2:
        for f in files:
            if f == args[1]:
                return print('')
    print(' '.join(fs.listdir(get_type_dir())))

def _edit(args):
    if len(args) != 1 or args[0] == 'help':
        return _edit_help()
    if args[0] == '____COMPLETE____':
        return _edit_complete()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    if fs.exists(filepath):
        if _TYPE == 'temp':
            os.chdir(filepath)
        os.system(env.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" {_TYPE} file found')

def _nuke_help():
    print(f'USAGE: mold {_TYPE} nuke <filename>')

def _nuke_complete(args):
    _edit_complete(args)    

def _nuke(args):
    if len(args) != 1 or args[0] == 'help':
        return _nuke_help()
    if args[0] == '____COMPLETE____':
        return _nuke_complete()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    if fs.exists(filepath):
        if _type == 'temp':
            fs.rimraf(filepath)
        else:
            fs.rm(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" {_TYPE} file found')

def _export(args):
    if len(args) < 1 or args[0] == 'help':
        return _help()
    filename = args[0]
    filepath = get_type_dir() + '/' + filename
    if len(args) == 2:
        filename = args[1]
    if fs.exists(filepath):
        if _TYPE == 'drop':
            fs.copy(filepath, './' + filename)
            return 
        if _TYPE == 'temp':
            fs.copydir(filepath, './' + filename)
            return 
    print(f'ERROR: no "{filename}" {_TYPE} file found')

def complete(args, _type):
    set_TYPE(_type)
    if len(args) == 0:
        return print('help list make load edit nuke')
    if args[0] == 'help':
        return print('')
    if args[0] == 'list':
        return print('')
    if args[0] == 'make':
        return _make_complete()
    if args[0] == 'load':
        return _load_complete(args)
    if args[0] == 'edit':
        return _edit_complete(args)
    if args[0] == 'nuke':
        return _nuke_complete(args)
    return print('help list make load edit nuke')

def main(options, _type):
    set_TYPE(_type)
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
    if _type == 'drop' or _type == 'temp':
        return  _export(options)
