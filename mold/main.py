import sys

import mold
import mold.env as env
import mold.ensure as ensure
from mold.core import main
from mold.complete import complete

def help():
    print(f'''
{mold.__description__} 

USAGE: mold [SUBCOMMAND] [OPTIONS]

SETUP and CONFIGURATION:
    Run `mold --install` to use the interactive installer.
    For manual intall instrcuions see {mold.__url__}.

    Run `mold --set-origin [https://github.com/user/example.git]` 
    to reset your $DOT_ROOT's git remote.

HELP: 
    mold and each of the mold subcomands have -h, --help, and help options for 
    printing help.

SUBCOMANDS: 
    stat    check the status of the $DOT_ROOT repository 
    pack    manage and execute system package installers 
    conf    manage configuration files (aka. moldfiles)
    temp    manage project scaffolding templates 
    drop    manage file asset templates 
    exec    manage executables
    plug    manage bash pugins 
    sync    sync git remote 
    help    show this help  

<3 Bug reports are much appreciated {mold.__url__.replace('https://', '')}/issues
    '''.strip())

def main():
    if ensure.check() != ensure.OK:
        print('goo')
        print(ensure.warning(), file=sys.stderr)
        return sys.exit(1)
    argv = sys.argv
    if len(argv) == 1:
        return print('''USAGE: mold [SUBCOMMAND] [OPTIONS] 
    run "mold help" for more info''')
    sub_command = argv[1]
    options = argv[2:]
    if(sub_command == 'help' or sub_command == '-h' or sub_command == '--help'):
        return help()
    if(sub_command == '--inistall'):
        return print('TODO: --install')
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

