'''
core defines the logic for the sub commands make load list edit nuke.
It also defines the abilty for drop and fold to export content.
'''

import os 
import mold.fs as fs
import mold.system as system
from mold.util import query

# TODO: have each task handler return an exit code from the ctx
# then refactor main to return the result of the task handler
# IDEA create two log functions for OK and FAIL , they can be used
# They should return OK or FAIL exit codes they can be used 
# to log a status and exit in one one :)

# TODO: have _make and _load only link the single conf that is being added to 
# the MOLD_ROOT
def _link_conf(ctx):
    if ctx.command != 'conf':
        return 
    for current in ctx.get_command_dirlist():
        src = ctx.MOLD_ROOT + '/conf/' + current
        dest = ctx.HOME + '/' + current
        fs.force_link(src, dest)

def _make(ctx):
    filename = ctx.get_option(0)
    filepath = ctx.get_command_dir() + '/' + filename
    if ctx.command == 'fold':
        fs.mkdir(filepath)
        system.cd(filepath)
    # TODO: LOG ERROR IF EDIT WASNT POSSIBLE
    system.shell(ctx.EDITOR + ' ' + filepath)
    if fs.exists(filepath):
        if ctx.command == 'conf':
            _link_conf(ctx)
        print(f'MADE {ctx.command.upper()}:', filename)
    else:
        print(f'MAKE {ctx.command.upper()} ABORTED: {filename} not created')

def _load(ctx):
    filepath = ctx.get_option(0)
    filename = ctx.get_option(1) or fs.basename(filepath)
    if fs.exists(filepath):
        # first load conten
        if ctx.command == 'fold':
            if not fs.is_dir(filepath):
                return print(f'USAGE ERROR: {filepath} is not a directory, use mold drop instead.')
            fs.copy_dir(filepath, ctx.get_command_dir() + '/' + filename)
        else:
            if fs.is_dir(filepath):
                return print(f'USAGE ERROR: {filepath}" is a directory, mold {ctx.command} only supports files.')
            fs.copy(filepath, ctx.get_command_dir() + '/' + filename)
        # then if its a conf link it 
        if ctx.command == 'conf':
            _link_conf(ctx)
        print(f'LOADED {ctx.command.upper()}: {filename}')
        return 
    print(f'ERROR: no "{filename}" {ctx.command} found')

# LIST
def _list(ctx):
        print('\n'.join(ctx.get_command_dirlist()))

def _edit(ctx):
    filename = ctx.get_option(0)
    filepath = ctx.get_command_dir() + '/' + filename
    if fs.exists(filepath):
        if ctx.command == 'fold': # IF you dont cd when using TUI editors its edit a dir structure
            system.cd(filepath) 
        # TODO: LOG ERROR IF EDIT WASNT POSSIBLE
        system.shell(ctx.EDITOR + ' ' + filepath)
        return 
    print(f'ERROR: no "{filename}" {ctx.command} file found')

def _nuke(ctx):
    filename = ctx.get_option(0)
    filepath = ctx.get_command_dir() + '/' + filename
    if fs.exists(filepath):
        if ctx.command == 'fold':
            fs.rimraf(filepath)
        else:
            fs.rm(filepath)
        print(f'REMOVED {filename}')
        return 
    print(f'ERROR: no "{filename}" {ctx.command} file found')

# EXPORT and LINK
def _dump(ctx):
    if not (ctx.command == 'fold' or ctx.command == 'drop'):
        print(f'Error: {ctx.command} does not support the drop task')
        return 
    filename = ctx.get_option(0)
    filepath = ctx.get_command_dir() + '/' + filename
    output  = ctx.get_option(1) or filename
    if fs.exists(filepath):
        if ctx.command == 'drop':
            fs.copy(filepath, './' + output) 
            return 
        if ctx.command == 'fold':
            fs.copydir(filepath, './' + output)
            return 
    print(f'ERROR: no "{filename}" {ctx.command} file found')

_task_handlers = {
    "make": _make,
    "load": _load,
    "list": _list,
    "edit": _edit,
    "nuke": _nuke,
    "dump": _dump,
}


def handle_task(ctx):
    try: 
        _task_handlers[ctx.task](ctx)
    except: 
        print(f'wut whoe, {ctx.task} is not known to mold {ctx.command}.')
