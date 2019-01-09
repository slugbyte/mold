'''
help defines an api for printing mold help messages.
'''

import mold 
from mold.color import green, red, magenta, yellow, reset, cyan, blue

header_color = cyan 
task_color = blue
command_color = magenta
warning_color = red 

def colorify(str):
    for header in ['USAGE:', 'ABOUT:', 'INSTALL:', 'CONFIGURATION:', 'HELP:', 'COMMANDS:', 
            'TASKS:', 'NOTE:', 'INSTALL FROM REPOSITORY:']:
        str = str.replace(header, f'{header_color}{header}{reset}')
    for command in ['conf:', 'plug:', 'exec:', 'drop:', 'fold:', 'sync:']:
        str = str.replace(command, f'{command_color}{command.replace(":", "")}{reset}')
    for task in [' list:', ' make:', ' load:', ' edit:', ' dump:', ' nuke:', 
            ' add:', ' commit:', ' push:', ' merge:', ' auto:', ' log:', ' pull:',
            ' status:', ' branch:', ' diff:', ' --force-push:', ' --hard-reset:', ' --new-branch:', 
            ' --delete-branch:', ' --checkout:']:
        str = str.replace(task, f'{task_color}{task.replace(":", "")}{reset}')
    for warn in ['WARNING:', 'DANGER:']: 
        str = str.replace(warn, f'{warning_color}{warn}{reset}')
    return str

def color_print(*args):
    color_args = []
    for x in args:
        color_args.append(colorify(x))
    print(*color_args)

# INTERFACE
def main():
    color_print(colorify(f'''
{green}{mold.__description__}{reset}

USAGE: mold [COMMAND] [TASK] [OPTIONS]

ABOUT:
    mold uses a git repository to store and track system configuration
    files. It splits the files in to the following classifications.
        conf: -- conf files are the dotfiles that will be hard linked to 
                the $HOME directory. e.g. mold load ~/.bashrc
        plug: -- plug files are shell scripts that will be sourced each time
                you create a new shell. e.g. mold plug make alias.sh
        exec: -- exec files will be added to a directory that will be in 
                the $PATH. e.g. exec load ./my-program 
        drop: -- drop files are file asset templates that you want add to 
                future projects. e.g. mold drop MIT-LICENSE.md
        fold: -- a fold is a project directory scaffold template, its like
                drop but its a whole directory. mold fold react-starter

INSTALL:
    To install a $MOLD_ROOT for the first time run `mold --install` 
    The $MOLD_ROOT directory will be set to ~/.mold and it will
    use $EDITOR or nano as the text editor.

    For custom installation see the mold github repository.

INSTALL FROM REPOSITORY:
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
    mold and each of the mold comands have -h, --help, and help options for 
    color_printing help.

COMMANDS: 
    TASKLESS:
    help:    show this help  

    WITH TASKS (auto and many more)
    sync:    sync git with remote and system config

    WITH TASKS (make load edit nuke) 
    fold:    manage project scaffolding templates (+ dump task)
    drop:    manage file asset templates (+ dump task) 
    conf:    manage configuration files 
    exec:    manage executables
    plug:    manage bash pugins 

<3 Bug reports are much appreciated {mold.__url__}/issues
    '''.strip()))

def fold():
    color_print('''
USAGE: mold fold [task] [diectorry] [new-name]

mold folds are templates for scaffold dierctorys. You can use 
mold fold load or create a directory, and later when you want 
a copy of that directory you can get a copy back.

TASKS:
    list: -- will color_print a list of the folds you have created.

    make: -- will create a new fold directory and open it in your 
            text editor, so you can desing a new dirrectory 
            template. 

    load: -- will copy an exisiting directory into your config 
            repository as a fold. load allows you to rename the
            directory you are importing.

    edit: -- will open an existing fold with your text editor.

    nuke: -- will remove an fold from your config repository.

    dump: -- will copy a fold from you config repository into
            your current directory. dump allows you to rename
            the exported fold.

e.g. 
    LOAD A FOLD:    mold fold load ./react-boiler
    EXPORT A FOLD:  mold fold dump react-boiler ./peronal-blog
    '''.strip())

def drop():
    color_print('''
USAGE: mold drop [task] [file] [new-name]

mold drops are file templates. You can use mold drop to create 
or load a file template, and later when you want a copy of 
your drop back.

TASKS:
    list: -- will color_print a list of the drop you have created.

    make: -- will create a new drop file and open it in your 
            text editor, so you can desing a file template. 

    load: -- will a file intor into your config repository 
            as a drop . load allows you to rename the drop
            you are importing.

    edit: -- will open an existing drop with your text editor.

    nuke: -- will remove an drop  from your config repository.

    dump: -- will copy a drop from you config repository into
            your current directory. dump allows you to rename
            the exported drop.

e.g. 
    LOAD DROPS:     mold drop load ./LICENSE.md mit.md 
                    mold drop load ./LICENSE.md cc-share-alike.md 
    EXPORT A DROP:  mold drop dump mit.md ./LICENSE.md 
'''.strip())

def conf():
    color_print('''
USAGE: mold conf [task] [file] 

mold confs are dotfiles. When you create or load a conf it 
will be hard linked to your home directory. Hard links are 
filesystem references to the same file. Editing the file in
your home directory will also edit the file in your config 
repository, and vice versa. 

If you run the nuke task it will only delete the file from 
your config repository. It will NOT remove it from your 
home directory. 

TASKS:
    list: -- will color_print a list all of your conf files. 

    make: -- will create a new conf file and open it in your 
            text editor, when the file will be hard linked 
            to your home directory. 

    load: -- will a file into your config repository as a conf 
            file and then hard link it to your home directory.

    edit: -- will open an existing conf with your text editor.

    nuke: -- will remove an conf file from your config repository, 
            but it will NOT remove it from your $HOME directory.

e.g. 
    LOAD CONFs:     mold conf load ~/.bashrc 
                    mold comf load ~/.nethackrc
'''.strip())

def plug():
    color_print('''
USAGE: mold plug [task] [file] 

mold plugs are shell scripts that will be loaded each time 
you create a new shell. Its great place to add ENV var 
config, aliases, functions, or startup scripts. 

NOTE: Anything you load as a plug will be sourced by your shell 
on load, so be carful to only load files your shell can source. 

TASKS:
    list: -- will color_print a list all of your plug files. 

    make: -- will create a new plug file and open it in your 
            text editor.

    load: -- will a file into your config repository as a plug.

    edit: -- will open an existing plug with your text editor.

    nuke: -- will remove an plug file from your config repository. 

e.g. 
    CREATE PLUGS:   mold plug make my-aliases.sh 
                    mold plug make git-shortcuts.sh         
                    mold plug load ./git-aware-prompt.sh
'''.strip())

def exec():
    color_print('''
USAGE: mold exec [task] [file] 

mold execs are executbale files that will be stored in
a directory on your $PATH. 

NOTE: If your file does not have executable permsions 
you will not be able to run it. so remember to chmod 775 it
if you need to.

TASKS:
    list: -- will color_print a list all of your exec files. 

    make: -- will create a new exec file and open it in your 
            text editor. It will automaticly have executable 
            permissions (755).

    load: -- will a file into your config repository as a exec.
            You can rename execs that you are loading

    edit: -- will open an existing exec with your text editor.

    nuke: -- will remove an exec file from your config repository. 

e.g. 
    CREATE EXECS:   mold exec make troll.py
    LOAD EXECS:     mold load ./a.out fetch-metadata
'''.strip())

def _task_one_file_arg_help(cmd, task, description):
    color_print(f'USAGE: mold {cmd} {task} <filename>\n{description}')

def _task_two_file_arg_help(cmd, task, description):
    color_print(f'USAGE: mold {cmd} {task} <filename> [optional <new-filename>]\n{description}')

def make(cmd):
    _task_one_file_arg_help(cmd, 'make', f'Make a new {cmd} with your text editor.')

def edit(cmd):
    _task_one_file_arg_help(cmd, 'edit', f'Edit an existing {cmd}.')

def nuke(cmd):
    also = ''
    if cmd == 'conf':
        also = '\nIt will not delete the file fom your $HOME directoy.'
    _task_one_file_arg_help(cmd, 'edit', f'Delete a {cmd} from your config repo.{also}')

def load(cmd):
    _task_two_file_arg_help(cmd, 'load', f'Load a {cmd} into your config repo.')

def dump(cmd):
    _task_two_file_arg_help(cmd, 'load', f'Copy a {cmd} from your config repo into your current directory.')

def list(cmd):
    color_print(f'USAGE: mold {cmd} list\nList the {cmd}z in your config repo')


#SYNC 
def sync():
    color_print('''
USAGE: mold sync [task] [arg] 
    mold sync is a wrapper for a few git commands. For all of the sync tasks
    the arg is optional.

WARNING:
    Tasks this start with -- are slightly dangerous, they have the potentail
    to remove data in a way that can not be undone. Use them with caution.

TASKS:
    NO ARGS:
    add: -- will run 'git add -A'

    log: -- will run 'git log'

    status: -- will run 'git status'

    pull: -- will run 'git pull origin HEAD' witch will pull from what 
            ever branch you have checked out.

    push: -- will run 'git push origin HEAD' witch will push to the 
            current branch'

    branch: -- will run 'git branch -avv' and list the current branches.

    WITH ARGS:
    diff: [arg] -- will run 'git diff [arg]', and the arg is optional.

    commit: [message] -- will run git commit with an optional message. 
                     no message is provided git will open your text 
                     editor and you can compose a commit message there. 

    DANGER:
    --force-push: -- DANGER: this will run 'git push origin HEAD ---force'
                    it will overwrite your remote with the current HEAD.

    --hard-reset: [arg] -- DANGER: this will run 'git reset --hard [arg]'
                          this will roll you branch back. If you dont 
                          provide an arg it will default to HEAD.
    --new-branch: [name] -- 
    --delete-branch: [name] -- 
    --checkout: [name] --


    auto: [message] -- command with pull, add -A, commit [message], 
            push.  If a message is provided it will be used as the commit 
            message. If no message is provied git will open your text 
            editor and you can compose a commit message there. This will 
            likely be the most useful command.

e.g. 
    Pull Add Commit Push:   mold sync auto
'''.strip())
