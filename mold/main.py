'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys

import mold.core as core
import mold.sync as sync
import mold.ensure as ensure
import mold.help as help
from mold.complete import complete
from mold.install import install
from mold.color import red, reset

# PRIVATE
def _check_help(ctx):
    if ctx.check_help_set():
        help.handle_help(ctx)
        return False 
    if ctx.command == None:
        print('''USAGE: mold [SUBCOMMAND] [OPTIONS] 
    run "mold help" for more info''')
        return False
    return True

def _check_mold_root(ctx):
    # TODO: refactor ensure so that it returns a bool 
    # make check use waringing internally 
    if ensure.check(ctx) != ensure.OK:
        print(ensure.warning(ctx), file=sys.stderr)
        return False
    return True

def _check_main_tasks(ctx):
    if ctx.check_install_set():
        install(ctx)
        return False
    if ctx.check_clone_set():
        print('TODO: implament --clone')
        return False
    if ctx.check_set_remote_set():
        print('TODO: implament --set-remote')
        return False
    return True

def _check_complete(ctx):
    if ctx.check_flag_set('complete'):
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

