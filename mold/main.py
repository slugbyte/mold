import sys

import mold
import mold.env as env
import mold.ensure as ensure
from mold.core import main
from mold.complete import complete
from mold.install import install

def help():
    print(f'''
{mold.__description__} 

USAGE: mold [SUBCOMMAND] [OPTIONS]

ABOUT:
    mold uses a git repository to store and track system configuration
    files. It splits the files in to the following classifications.
        conf -- conf files are the dotfiles that will be hard linked to 
                the $HOME directory. e.g. dot load ~/.bashrc
        plug -- plug files are shell scripts that will be sourced each time
                you create a new shell. e.g. dot plug make alias.sh
        exec -- exec files will be added to a directory that will be in 
                the $PATH. e.g. exec load ./my-program 
        drop -- drop files are file asset templates that you want add to 
                future projects. e.g. dot drop MIT-LICENSE.md
        fold -- a fold is a project directory scaffold template, its like
                drop but its a whole directory. dot fold react-starter

INSTALL:
    To install a $MOLD_ROOT for the first time run `mold --install` 
    The $MOLD_ROOT directory will be set to ~/.mold and it will
    use $EDITOR or nano as the text editor.

    For custom installation see the mold github repository.

INSTALL USING AN EXISTING GIT REMOTE:
    To install from an existing remote run `mold --clone [git uri]`

CONFIGURATION:
    GIT REMOTE:
    You can either manualy change the MOLD_ROOT git remote, or you can 
    also run `mold --set-origin [https://github.com/user/example.git]` 
    to reset the git remote.

    TEXT EDITOR:
    To change the text editor use bash to $EDITOR to point to the 
    a text editor executable.
    e.g. In the shell config write 'export EDITOR = /usr/local/bin/vim'

HELP: 
    mold and each of the mold subcomands have -h, --help, and help options for 
    printing help.

SUBCOMANDS: 
    stat    check the status of the $MOLD_ROOT repository 
    conf    manage configuration files (aka. moldfiles)
    temp    manage project scaffolding templates 
    drop    manage file asset templates 
    exec    manage executables
    plug    manage bash pugins 
    sync    sync git remote 
    help    show this help  

<3 Bug reports are much appreciated {mold.__url__}/issues
    '''.strip())

def main():
    argv = sys.argv
    if len(argv) == 1:
        return print('''USAGE: mold [SUBCOMMAND] [OPTIONS] 
    run "mold help" for more info''')
    sub_command = argv[1]
    options = argv[2:]
    if(sub_command == 'help' or sub_command == '-h' or sub_command == '--help'):
        return help()
    if ensure.check() != ensure.OK:
        if sub_command == '--install':
            return install()
        print(ensure.warning(), file=sys.stderr)
        return sys.exit(1)
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

