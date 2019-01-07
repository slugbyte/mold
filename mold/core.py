'''
core defines the logic for the sub commands make load list edit nuke.
It also defines the abilty for drop and fold to export content.
'''

import os 
import mold.fs as fs
import mold.env as env
import mold.util as util
import mold.help as help
from mold.query import query

# TASK AND TASK HELPER FUNCTION SIGNATURE
# def _name(cmd, task, args) (data is a filename or filepath but file is a reserved word)
# much of the time the arguments will not be used, but it will make adding features in the 
# future much easier if the inteface for all the functions is allways the same. :)


MAGIC_MOLD = '__MAGIC_MOLD__'

# PRIVATE
def _cmd_dir(cmd, task, args):
    return env.ROOT_DIR + '/' + cmd

# MAKE
def _make_help(cmd, task, args):
    print(f'\nUSAGE: mold {cmd} make <filename>\n')

def _make_complete(cmd, task, args):
    return  print(MAGIC_MOLD)

def _make(cmd, task, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return _make_help(cmd, task, args)
    filepath = _cmd_dir(cmd, task, args) + '/' + filename
    if cmd == 'fold':
        fs.mkdir(filepath)
        util.cd(filepath)
    util.shell(env.EDITOR + ' ' + filepath)
    if fs.exists(filepath):
        print('MADE FILE:', filename)
    else:
        print(f'MAKE ABORTED: {filename} not created')

# LOAD
def _load_help(cmd, task, args):
    print(f'USAGE: mold {cmd} load <filepath> [optional new name]')

def _load_complete(cmd, task, args):
    print(MAGIC_MOLD)

# TODO: add checks for if file or if dir (dep on cmd)
def _load(cmd, task, args):
    filepath = query(args, 0)
    if filepath == 'help' or not filepath:
        return _load_help(cmd, task, args)
    filename = query(args, 1) or fs.basename(filepath)
    if fs.exists(filepath):
        if cmd == 'fold':
            fs.copydir(filepath, _cmd_dir(cmd, task, args) + '/' + filename)
        else:
            fs.copy(filepath, _cmd_dir(cmd, task, args) + '/' + filename)
        print(f'LOADED {filename}')
        return 
    print(f'ERROR: no "{filename}" {cmd} found')

# LIST
def _list_help(cmd, task, args):
    print(f'\nUSAGE: mold {cmd} list\n')

def _list_complete(cmd, task, args):
    return  print('')

def _list(cmd, task, args):
    for current in fs.listdir(_cmd_dir(cmd, task, args)):
        if current != '.mold':
            print(current)

# EDIT
def _edit_help(cmd, task, args):
    print(f'USAGE: mold {cmd} edit <filename>')

def _edit_complete(cmd, task, args):
    _list(cmd, task, args)

def _edit(cmd, task, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return _edit_help(cmd, task, args)
    filepath = _cmd_dir(cmd, task, args) + '/' + filename
    if fs.exists(filepath):
        # if cmd == 'fold': # util.cd(filepath) # TEST WITH OUT AND RESTORE IF USEFULL
        util.shell(env.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" {cmd} file found')

# NUKE
def _nuke_help(cmd, task, args):
    print(f'USAGE: mold {cmd} nuke <filename>')

def _nuke_complete(cmd, task, args):
    _list(cmd, task, args)

def _nuke(cmd, task, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return _nuke_help(cmd, task, args)
    filepath = _cmd_dir(cmd, task, args) + '/' + filename
    if fs.exists(filepath):
        if cmd == 'fold':
            fs.rimraf(filepath)
        else:
            fs.rm(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" {cmd} file found')

# EXPORT 
def _dump(cmd, task, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return print("FOOOO MAKE DUMP HELP")
    filepath = _cmd_dir(cmd, task, args) + '/' + filename
    output  = query(args, 1) or filename
    if fs.exists(filepath):
        if cmd == 'drop':
            fs.copy(filepath, './' + output) 
            return 
        if cmd == 'fold':
            fs.copydir(filepath, './' + output)
            return 
    print(f'ERROR: no "{filename}" {cmd} file found')

_task_completions = {
    "make": _make_complete,
    "load": _load_complete,
    "list": _list_complete,
    "edit": _edit_complete,
    "nuke": _nuke_complete,
}

_task_handlers = {
    "make": _make,
    "load": _load,
    "list": _list,
    "edit": _edit,
    "nuke": _nuke,
    "dump": _dump,
}

# INTERFACE
def complete(cmd, args):
    if cmd == None or len(args) == 0:
        return print('help make load list edit nuke')
    task = args[0]
    if task == 'help':
        return print('TODO: IMPLAMENT HELP FO EACH TASK')
    for current in ['make', 'load', 'list', 'edit', 'nuke']:
        if task == current:
            return _task_completions[task](cmd, task, args)
    return complete(None, [])

def handle_task(cmd, options):
    if len(options) == 0 or options[0] == 'help':
        return print('TODO: MAKE INDIVIDUAL COMMAND HELP')
    task = query(options, 0)
    filename = query(options, 1)
    for current in ['make', 'load', 'list', 'edit', 'nuke', 'dump']:
        if task == current:
            return _task_handlers[task](cmd, task, options[1:])
    print('wut whoe')


# mold CMD  TASK FILE (in core ALL WAYS?)
# mold help
# mold drop help 
# mold drop list
# mold drop make file
# mold drop load file
# mold drop edit file
# mold drop dump file
# muld drop nuke file
