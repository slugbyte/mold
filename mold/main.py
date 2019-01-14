'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys

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
    # TODO: make this less janky by removing _result and _setresult from mold_root
    if mold_root.check(ctx) != mold_root.OK:
        print(mold_root.warning(ctx), file=sys.stderr)
        return False
    return True

def _check_main_tasks(ctx):
    if ctx.check_install_set() or ctx.check_clone_set() or ctx.check_set_remote_set():
        mold_root.handle_flag(ctx)
        return False
    return True

def _check_complete(ctx):
    if ctx.check_flag_set('--complete'):
        complete(ctx)
        return False
    return True

def _check_core(ctx):
    for current in ['drop', 'fold', 'exec', 'conf', 'plug']:
        if ctx.command == current:
            core.handle_task(ctx)
            return False 
    return True

def _check_sync(ctx):
    if ctx.command== 'sync':
        sync.handle_task(ctx)
        return False
    return True

# INTERFACE
def main(ctx):
    red = get_color(ctx, 'red')
    reset = get_color(ctx, 'reset')
    # the order of the check invocations can not change
    if not _check_complete(ctx):
        return ctx.OK

    if not _check_main_tasks(ctx):
        return ctx.OK

    if not _check_help(ctx):
        return ctx.OK

    if not _check_mold_root(ctx):
        return ctx.FAIL

    if not _check_core(ctx):
        return ctx.OK

    if not _check_sync(ctx):
        return ctx.OK
    print(f'{red}doh!{reset} mold {ctx.command} isn\'t a feature yet.')
    return ctx.DEV_TODO

