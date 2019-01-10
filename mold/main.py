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
def _check_usage(ctx):
    if ctx.command == None:
        print('''USAGE: mold [SUBCOMMAND] [OPTIONS] 
    run "mold help" for more info''')
        return False
    return True

def _check_help(ctx):
    command = ctx.command 
    if(command == 'help' or command == '-h' or command == '--help'):
        help.main(ctx)
        return False 
    return True

def _check_mold_root(ctx):
    # TODO: refactor ensure so that it returns a bool 
    # make check use waringing internally 
    if ensure.check(ctx) != ensure.OK:
        print(ensure.warning(ctx), file=sys.stderr)
        return False
    return True

def _check_install(ctx):
    if ctx.command == '--install':
        install(ctx)
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
        return ctx.EXIT_STATUS_OK

    if not _check_usage(ctx):
        return ctx.EXIT_STATUS_OK

    if not _check_help(ctx):
        return ctx.EXIT_STATUS_OK

    if not _check_install(ctx):
        return ctx.EXIT_STATUS_OK

    if not _check_mold_root(ctx):
        return ctx.EXIT_STATUS_FAIL

    if not _check_core(ctx):
        return ctx.EXIT_STATUS_OK

    if not _check_sync(ctx):
        return ctx.EXIT_STATUS_OK
    print(f'{red}doh!{reset} mold {ctx.command} isn\'t a feature yet.')
    return ctx.EXIT_STATUS_DEVELOPER_TODO

