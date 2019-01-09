'''
core defines the logic for the sub commands make load list edit nuke.
It also defines the abilty for drop and fold to export content.
'''

import os 
import mold.fs as fs
import mold.env as env
import mold.system as system
import mold.help as help
from mold.util import query

# TASK AND TASK HELPER FUNCTION SIGNATURE
# def _name(cmd, args) (data is a filename or filepath but file is a reserved word)
# much of the time the arguments will not be used, but it will make adding features in the 
# future much easier if the inteface for all the functions is allways the same. :)


MAGIC_MOLD = '__MAGIC_MOLD__'

# PRIVATE
def _cmd_dir(cmd, args):
    return env.ROOT_DIR + '/' + cmd

# MAKE
def _make_complete(cmd, args):
    return  print(MAGIC_MOLD)

def _make(cmd, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return help.make(cmd)
    filepath = _cmd_dir(cmd, args) + '/' + filename
    if cmd == 'fold':
        fs.mkdir(filepath)
        system.cd(filepath)
    system.shell(env.EDITOR + ' ' + filepath)
    if fs.exists(filepath):
        print('MADE FILE:', filename)
    else:
        print(f'MAKE ABORTED: {filename} not created')

# LOAD
def _load_complete(cmd, args):
    print(MAGIC_MOLD)

# TODO: add checks for if file or if dir (dep on cmd)
def _load(cmd, args):
    filepath = query(args, 0)
    if filepath == 'help' or not filepath:
        return help.load(cmd)
    filename = query(args, 1) or fs.basename(filepath)
    if fs.exists(filepath):
        if cmd == 'fold':
            fs.copy_dir(filepath, _cmd_dir(cmd, args) + '/' + filename)
        else:
            fs.copy(filepath, _cmd_dir(cmd, args) + '/' + filename)
        print(f'LOADED {filename}')
        return 
    print(f'ERROR: no "{filename}" {cmd} found')

# LIST
def _list_complete(cmd, args):
    return  print('')

def _list(cmd, args):
    arg = query(args, 0)
    if arg == 'help':
        return help.list(cmd)
    for current in fs.listdir(_cmd_dir(cmd, args)):
        if current != '.mold':
            print(current)

# EDIT
def _edit_complete(cmd, args):
    _list(cmd, args)

def _edit(cmd, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return help.edit(cmd)
    filepath = _cmd_dir(cmd, args) + '/' + filename
    if fs.exists(filepath):
        # if cmd == 'fold': # system.cd(filepath) # TEST WITH OUT AND RESTORE IF USEFULL
        system.shell(env.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" {cmd} file found')

# NUKE
def _nuke_complete(cmd, args):
    _list(cmd, args)

def _nuke(cmd, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return help.nuke(cmd)
    filepath = _cmd_dir(cmd, args) + '/' + filename
    if fs.exists(filepath):
        if cmd == 'fold':
            fs.rimraf(filepath)
        else:
            fs.rm(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" {cmd} file found')

# EXPORT 
def _dump(cmd, args):
    filename = query(args, 0)
    if filename == 'help' or not filename:
        return help.dump(cmd)
    filepath = _cmd_dir(cmd, args) + '/' + filename
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

_cmd_helps = {
    "conf": help.conf,
    "plug": help.plug,
    "exec": help.exec,
    "fold": help.fold,
    "drop": help.drop,
}

# INTERFACE
def complete(cmd, args):
    if cmd == None or len(args) == 0:
        return print('help make load list edit nuke')
    task = args[0]
    if task == 'help':
        return ''
    for current in ['make', 'load', 'list', 'edit', 'nuke']:
        if task == current:
            return _task_completions[task](cmd, args)
    return complete(None, [])

def handle_task(cmd, options):
    task = query(options, 0)
    if task == 'help' or not task:
        return _cmd_helps[cmd]()
    filename = query(options, 1)
    for current in ['make', 'load', 'list', 'edit', 'nuke', 'dump']:
        if task == current:
            return _task_handlers[task](cmd, options[1:])
    print(f'wut whoe, {task} is not known to mold {cmd}.')
