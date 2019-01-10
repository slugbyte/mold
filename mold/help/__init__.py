'''
help defines an api for printing mold help messages.
'''

import mold as _mold
import mold.color as color

# load all the help files
import mold.help.main_help as main_help 
import mold.help.core.conf_help as conf_help
import mold.help.core.fold_help as conf_help

header_color = color.cyan 
task_color = color.blue
command_color = color.magenta
warning_color = color.red 
reset = color.reset

# TODO: refacter each help to be a string
# then create a comple fiunction that will choose to colorify base on ctx
# then make a create_help_handler to generate help defs (functions)

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

def compile(ctx, text):
    green = color.green
    reset = color.reset
    mold = _mold
    return text.format(**locals())

def main(ctx):
    color_print(compile(ctx, main_help.text))

def conf(ctx):
    color_print(compile(ctx, conf_help.text))


def _task_one_file_arg_help(ctx, description):
    color_print(f'USAGE: mold {ctx.command} {ctx.task} <filename>\n{description}')

def _task_two_file_arg_help(ctx,  description):
    color_print(f'USAGE: mold {ctx.command} {ctx.task} <filename> [optional <new-filename>]\n{description}')

def make(ctx):
    _task_one_file_arg_help(ctx, f'Make a new {ctx.command} with your text editor.')

def edit(ctx):
    _task_one_file_arg_help(ctx,  f'Edit an existing {ctx.command}.')

def nuke(ctx):
    also = ''
    if ctx.command == 'conf':
        also = '\nIt will not delete the file fom your $HOME directoy.'
    _task_one_file_arg_help(ctx, f'Delete a {ctx.command} from your config repo.{also}')

def load(ctx):
    _task_two_file_arg_help(ctx, f'Load a {ctx.command} into your config repo.')

def dump(ctx):
    _task_two_file_arg_help(ctx.command, 'load', f'Copy a {ctx.command} from your config repo into your current directory.')

def list(ctx):
    color_print(f'USAGE: mold {ctx.command} list\nList the {ctx.command}z in your config repo')


#SYNC 
def sync(ctx):
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
