'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys

import mold.env as env
import mold.core as core
import mold.sync as sync
import mold.ensure as ensure
import mold.help as help
from mold.complete import complete
from mold.install import install
from mold.color import red, reset

# PRIVATE
def _check_usage(cmd, options):
    if cmd == None:
        print('''USAGE: mold [SUBCOMMAND] [OPTIONS] 
    run "mold help" for more info''')
        return False
    return True

def _check_help(cmd, options):
    if(cmd == 'help' or cmd == '-h' or cmd == '--help'):
        help.main()
        return False 
    return True

def _check_mold_root(cmd, options):
    if ensure.check() != ensure.OK:
        print(ensure.warning(), file=sys.stderr)
        return False
    return True

def _check_install(cmd, options):
    if cmd  == '--install':
        install()
        return False
    return True

def _check_complete(cmd, options):
    if(cmd == 'complete'):
        complete()
        return False
    return True

def _check_core(cmd, options):
    for current in ['drop', 'fold', 'exec', 'conf', 'plug']:
        if cmd == current:
            core.handle_task(cmd, options)
            return False 
    return True

def _check_sync(cmd, options):
    if cmd == 'sync':
        sync.handle_task(cmd, options)
        return False
    return True

# INTERFACE
def main(cmd, options):
    if not _check_usage(cmd, options):
        return env.EXIT_STATUS_OK
    if not _check_help(cmd, options):
        return env.EXIT_STATUS_OK
    if not _check_install(cmd, options):
        return env.EXIT_STATUS_OK
    if not _check_mold_root:
        return env.EXIT_STATUS_FAIL
    if not _check_complete(cmd, options):
        return env.EXIT_STATUS_OK
    if not _check_core(cmd, options):
        return env.EXIT_STATUS_OK
    if not _check_sync(cmd, options):
        return env.EXIT_STATUS_OK
    print(f'{red}doh!{reset} mold {cmd} isn\'t a feature yet.')
    return env.EXIT_STATUS_DEVELOPER_TODO

