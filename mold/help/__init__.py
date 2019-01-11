'''
help defines an api for printing mold help messages.
'''

import mold as _mold
import mold.color as color

# load all the help files
import mold.help.main_help as main_help 

# core 
import mold.help.core.conf_help as conf_help
import mold.help.core.plug_help as plug_help
import mold.help.core.exec_help as exec_help
import mold.help.core.drop_help as drop_help
import mold.help.core.fold_help as fold_help
import mold.help.core.core_task_help as core_task_help

# sync 
import mold.help.sync.sync_help as sync_help

# TODO NOW: 1) get the rest of the help text in this file into own files
# 2) make help text files for sync tasks
# 3) figure out how you want to really go about compile and color <3

# TODO: refacter each help to be a string
# then create a comple fiunction that will choose to colorify base on ctx
# then make a create_help_handler to generate help defs (functions)

header_color = color.cyan 
task_color = color.blue
command_color = color.magenta
warning_color = color.red 
reset = color.reset


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

def compile(ctx, text):
    green = color.green
    reset = color.reset
    mold = _mold
    return text.format(**locals())

def main(ctx):
    color_print(compile(ctx, main_help.text))
def conf(ctx):
    color_print(compile(ctx, conf_help.text))
def plug(ctx):
    color_print(compile(ctx, conf_plug.text))


