'''
core defines the logic for the sub commands make load list edit nuke.
It also defines the abilty for drop and fold to export content.
'''

import mold.fs as fs
import mold.env as env
import mold.util as util
import mold.help as help

MAGIC_MOLD = '__MAGIC_MOLD__'

# SINGLETON STATE

def getcmd_dir(cmd, options):
    return env.ROOT_DIR + '/' + cmd

def _make_help(cmd, options):
    print(f'''
USAGE: mold {cmd} make <filename>
    '''.strip())

def _make_complete(cmd, options):
    return  print(MAGIC_MOLD)

def _make(cmd, options):
    if len(options) != 1 or options[0] == 'help':
        return _make_help(cmd, options)
    filename = options[0]
    filepath = getcmd_dir() + '/' + filename
    if cmd == 'fold':
        fs.mkdir(filepath)
        util.cd(filepath)
    util.shell(env.EDITOR + ' ' + filepath)
    if fs.exists(filepath):
        print('MADE FILE:', filename)
    else:
        print(f'MAKE ABORTED: {filename} not created')

def _list_help(cmd, options):
    print(f'''
USAGE: mold {cmd} list
    '''.strip())

def _list_complete(cmdi, options):
    return  print('')

def _list(cmd, options):
    if len(options) == 0:
        print('\n'.join(fs.listdir(getcmd_dir())).replace('.mold', '').strip())
        return 
    return _list_help(cmd, options)

def _load_help(cmd, options):
    print(f'USAGE: mold {cmd} load <filepath> [optional new name]')

def _load_complete(cmd, options):
    print(MAGIC_MOLD)

def _load(cmd, options):
    if len(options) < 0 or options[0] == 'help':
        return _load_help(cmd, options)
    filepath = options[0]
    filename = fs.basename(filepath)
    if len(options) == 2:
        filename = options[1]
    if fs.exists(filepath):
        if cmd == 'fold':
            fs.copydir(filepath, getcmd_dir() + '/' + filename)
        else:
            fs.copy(filepath, getcmd_dir() + '/' + filename)
        print(f'LOADED {filename}')
        return 
    print(f'ERROR: no "{filename}" {cmd} found')

def _edit_help(cmd):
    print(f'USAGE: mold {cmd} edit <filename>')

def _edit_complete(cmd, args):
    files = fs.listdir(getcmd_dir())
    if len(args) == 2:
        for f in files:
            if f == args[1]:
                return print('')
    print(' '.join(fs.listdir(getcmd_dir())).replace('.mold', '').strip())

def _edit(cmd, args):
    if len(args) != 1 or args[0] == 'help':
        return _edit_help()
    filename = args[0]
    filepath = getcmd_dir() + '/' + filename
    if fs.exists(filepath):
        if cmd == 'fold':
            util.cd(filepath)
        util.shell(env.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" {cmd} file found')

def _nuke_help(cmd):
    print(f'USAGE: mold {cmd} nuke <filename>')

def _nuke_complete(cmd, args):
    _edit_complete(args)    

def _nuke(cmd, args):
    if len(args) != 1 or args[0] == 'help':
        return _nuke_help()
    filename = args[0]
    filepath = getcmd_dir() + '/' + filename
    if fs.exists(filepath):
        if cmd == 'fold':
            fs.rimraf(filepath)
        else:
            fs.rm(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" {cmd} file found')

def _export(cmd, args):
    if len(args) < 1 or args[0] == 'help':
        return _help()
    filename = args[0]
    filepath = getcmd_dir() + '/' + filename
    if len(args) == 2:
        filename = args[1]
    if fs.exists(filepath):
        if cmd == 'drop':
            fs.copy(filepath, './' + filename) 
            return 
        if cmd == 'fold':
            fs.copydir(filepath, './' + filename)
            return 
    print(f'ERROR: no "{filename}" {cmd} file found')

def complete(cmd, args):
    if len(args) == 0:
        return print('help list make load edit nuke')
    if args[0] == 'help':
        return print('')
    if args[0] == 'list':
        return print('')
    if args[0] == 'make':
        return _make_complete(cmd)
    if args[0] == 'load':
        return _load_complete(cmd, args)
    if args[0] == 'edit':
        return _edit_complete(cmd, args)
    if args[0] == 'nuke':
        return _nuke_complete(cmd, args)
    return print('help list make load edit nuke')

def main(cmd, options):
    if len(options) == 0 or options[0] == 'help':
        return help.main()
    if options[0] == 'make':
        return _make(cmd, options[1:])
    if options[0] == 'load':
        return _load(cmd, options[1:])
    if options[0] == 'list':
        return _list(cmd, options[1:])
    if options[0] == 'edit':
        return _edit(cmd, options[1:])
    if options[0] == 'nuke':
        return _nuke(cmd, options[1:])
    if cmd == 'drop' or cmd == 'fold':
        return  _export(cmd, options)
