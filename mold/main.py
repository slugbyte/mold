'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys

import mold.env as env
import mold.core as core
import mold.ensure as ensure
import mold.help as help
from mold.complete import complete
from mold.install import install

def check_usage(cmd, options):
    if cmd == None:
        print('''USAGE: mold [SUBCOMMAND] [OPTIONS] 
    run "mold help" for more info''')
        return False
    return True

def check_help(cmd, options):
    if(cmd == 'help' or cmd == '-h' or cmd == '--help'):
        help.main()
        return False 
    return True

def check_install(cmd, options):
    if ensure.check() != ensure.OK:
        if cmd  == '--install':
            return install()
        print(ensure.warning(), file=sys.stderr)
        return False
    return True

def check_complete(cmd, options):
    if(cmd == 'complete'):
        complete()
        return False
    return True

def check_core(cmd, options):
    for current in ['drop', 'fold', 'exec', 'conf', 'plug']:
        if cmd == current:
            core.main(cmd, options)
            return False 
    return True

def main(cmd, options):
    if not check_usage(cmd, options):
        return env.EXIT_STATUS_OK
    if not check_help(cmd, options):
        return env.EXIT_STATUS_OK
    if not check_install(cmd, options):
        return env.EXIT_STATUS_FAIL
    if not check_complete(cmd, options):
        return env.EXIT_STATUS_OK
    if not check_core(cmd, options):
        return env.EXIT_STATUS_OK
    if cmd == 'push':
        print('push')
        return env.EXIT_STATUS_DEVELOPER_TODO
    if cmd == 'pull':
        print('pull')
        return env.EXIT_STATUS_DEVELOPER_TODO
    if cmd == 'stat':
        print('stat')
        return env.EXIT_STATUS_DEVELOPER_TODO
    if cmd  == 'diff':
        print('diff')
        return env.EXIT_STATUS_DEVELOPER_TODO
    return env.EXIT_STATUS_DEVELOPER_TODO
