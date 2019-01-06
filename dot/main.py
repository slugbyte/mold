import os
import sys
from pathlib import Path

import dot.env as env
import dot.ensure as ensure
from dot.core import core
from dot.complete import complete

def help():
    print('''
USAGE: dot [SUBCOMMAND] [OPTIONS]
    A system configuration and shell workflow tool.

    SUBCOMMANDS: 
        conf    mange config files (init, make, load, nuke, help)
        temp    project scaffolding templates (init, make, load, nuke, help)
        drop    file asset templates (<name>, make, load, edit, nuke, help)
        plug    bash pugins (make, edit, nuke)
        pack    system package installers (make, edit, nuke)
        exec    system binarys (load, nuke)
        push    commit dot updates and push
        pull    pull dot updates and install 
        stat    git stat and diff the dot repository
        help    show this help  
    '''.strip())

def main():
    if ensure.check() != ensure.OK:
        print(ensure.warning(), file=sys.stderr)
        return sys.exit(1)
    argv = sys.argv
    if len(argv) == 1:
        return help()
    sub_command = argv[1]
    options = argv[2:]
    if(sub_command == '--inistall'):
        return print('TODO: --install')
    if(sub_command == '--fix-root'):
        return print('TODO: --fix-root')
    if(sub_command == 'complete'):
        return complete(argv)
    if(sub_command == 'drop'):
        return core(options, 'drop')
    if(sub_command == 'temp'):
        return core(options, 'temp')
    if(sub_command == 'plug'):
        return core(options, 'plug')
    if(sub_command == 'pack'):
        return core(options, 'pack')
    if(sub_command == 'exec'):
        return core(options, 'exec')
    if(sub_command == 'conf'):
        return core(options, 'conf')
    if(sub_command == 'push'):
        return print('push')
    if(sub_command == 'pull'):
        return print('pull')
    if(sub_command == 'stat'):
        return print('stat')
    if(sub_command == 'diff'):
        return print('diff')

