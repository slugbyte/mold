'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys

import mold
import mold.core as core
import mold.sync as sync
import mold.help as help
import mold.mold_root as mold_root
from mold.complete import complete
from mold.color import get_color

# PRIVATE
def _check_help(ctx):
    if ctx.check_help_set():
        help.handle_help(ctx)
        return False 
    if ctx.command == None:
        print('''USAGE: mold [--flags] [command] [task] [...options]
    run "mold help" for more info''')
        return False
    return True

def _check_mold_root(ctx):
    if ctx.command == 'root':
        return mold_root.handle_flag(ctx)
    result = mold_root.check(ctx)
    if result != ctx.OK:
        return result
    return True

def _check_main_tasks(ctx):
    if ctx.check_flag_set('--version'):
        print('v' + mold.__version__)
        return False
    return True

def _check_complete(ctx):
    if ctx.check_flag_set('--complete'):
        complete(ctx)
        return False
    return True

def _check_core(ctx):
    for current in ['leaf', 'fold', 'exec', 'conf', 'plug']:
        if ctx.command == current:
            core.handle_task(ctx)
            return False 
    return True

def _check_list(ctx):
    if ctx.command== 'list':
        for current in ['leaf', 'fold', 'exec', 'conf', 'plug']:
            content = ctx.get_command_dirlist(current) 
            if len(content) == 0:
                continue
            print(current)
            print('    '+ '\n    '.join(ctx.get_command_dirlist(current)) or 'Empty')
        return False
    return True

def _check_sync(ctx):
    if ctx.command== 'sync':
        sync.handle_task(ctx)
        return False
    return True

# INTERFACE
def handle_context(ctx):
    red = get_color(ctx, 'red')
    reset = get_color(ctx, 'reset')
    # the order of the check invocations can not change
    if not _check_complete(ctx):
        return ctx.OK

    if not _check_main_tasks(ctx):
        return ctx.OK

    if not _check_help(ctx):
        return ctx.OK

    result = _check_mold_root(ctx)
    if result != True:
        return result

    if not _check_core(ctx):
        return ctx.OK

    if not _check_list(ctx):
        return ctx.OK

    if not _check_sync(ctx):
        return ctx.OK
    print(f'{red}doh!{reset} mold {ctx.command} isn\'t a feature yet.')
    return ctx.OK

