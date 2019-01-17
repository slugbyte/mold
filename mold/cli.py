'''
main is defines the logic for the cli, it is a router 
for SUB_COMMANDs and OPTIONS.
'''

import sys
import mold
import mold.commands.core as core
import mold.commands.sync as sync
import mold.commands.help as help
import mold.commands.root as root
import mold.commands.complete as complete
from mold.color import get_color

# PRIVATE
# TODO migrate the _check methods into each command's handle_context
# TODO migrate colors into context
def _check_help(ctx):
    if ctx.check_help_set():
        help.handle_help(ctx)
        return ctx.OK
    if ctx.command == None:
        print('''USAGE: mold [--flags] [command] [task] [...options]
    run "mold help" for more info''')
        return ctx.OK
    return ctx.NEXT_COMMAND

def _check_root(ctx):
    if ctx.command == 'root':
        return root.handle_context(ctx)
    result = root.check(ctx)
    if result != ctx.OK:
        return result
    return ctx.NEXT_COMMAND

def _check_version(ctx):
    if ctx.command == '--version':
        print('v' + mold.__version__)
        return ctx.OK
    return ctx.NEXT_COMMAND

def _check_complete(ctx):
    if ctx.check_flag_set('--complete'):
        complete.handle_context(ctx)
        return ctx.OK
    return ctx.NEXT_COMMAND

def _check_core(ctx):
    for current in ['leaf', 'fold', 'exec', 'conf', 'plug']:
        if ctx.command == current:
            core.handle_context(ctx)
            return ctx.OK
    return ctx.NEXT_COMMAND

def _check_list(ctx):
    if ctx.command== 'list':
        for current in ['leaf', 'fold', 'exec', 'conf', 'plug']:
            content = ctx.get_command_dirlist(current) 
            if len(content) == 0:
                continue
            print(current)
            print('    '+ '\n    '.join(ctx.get_command_dirlist(current)) or 'Empty')
        return ctx.OK
    return ctx.NEXT_COMMAND

def _check_sync(ctx):
    if ctx.command == 'sync':
        sync.handle_context(ctx)
        return ctx.OK
    return ctx.NEXT_COMMAND

# INTERFACE
def handle_context(ctx):
    # The ordering of the commands array is important
    commands = [
        _check_complete,
        _check_version,
        _check_help,
        _check_root,
        _check_core,
        _check_list,
        _check_sync,
    ]
    
    for command in commands:
        result = command(ctx)
        if result != ctx.NEXT_COMMAND:
            return result

    red = get_color(ctx, 'red')
    reset = get_color(ctx, 'reset')
    print(f'{red}doh!{reset} mold {ctx.command} isn\'t a feature yet.')
    return ctx.OK

