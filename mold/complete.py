'''
complete defines the routing routing logic for arguments to  mold --complete. 
'''

import mold.core as core
import mold.ensure as ensure
import mold.util as util

# PRIVATE 
# --install, --clone, --set-remote, and any other --* commands do not tab complete
_completable_commands = ['conf', 'plug', 'exec', 'temp', 'drop', 'sync']
_completable_core_default_tasks = ['help', 'make', 'load', 'list', 'edit', 'nuke']
_completable_sync_tasks = ['auto', 'log', 'add', 'commit', 'push', 'pull', 'diff', 'status', 'branch']
        # '--new-branch', '--checkout', '--merge', '--soft-reset', '--hard-reset'

# TODO: implament --clone, --set-remote 
# _main_comands = ['--install']

def _complete_no_suggestions(ctx):
    print('')

def _complete_magic_mold(ctx):
    print(ctx.MAGIC_MOLD)

def _complete_command_dirlist(ctx):
    content = []
    print(' '.join(ctx.get_command_dirlist()))

def _create_handler_from_word_list(words):
    def _complete_words(ctx):
        print(' '.join(words))
    return _complete_words

_completion_handlers = {
    # main 
    "main": _create_handler_from_word_list(['fold', 'drop', 'conf', 'plug', 'exec', 'sync', 'help']),
    # commands
    "help": _complete_magic_mold,
    "conf": _create_handler_from_word_list(_completable_core_default_tasks),
    "exec": _create_handler_from_word_list(_completable_core_default_tasks),
    "plug": _create_handler_from_word_list(_completable_core_default_tasks),
    "fold": _create_handler_from_word_list(_completable_core_default_tasks + ['dump']),
    "drop": _create_handler_from_word_list(_completable_core_default_tasks + ['dump']),
    "sync": _create_handler_from_word_list(_completable_sync_tasks),
    "--install": _complete_no_suggestions,
    "--set-remote": _complete_no_suggestions,
    # core tasks
    "load": _complete_magic_mold,
    "make": _complete_no_suggestions,
    "list": _complete_no_suggestions,
    "edit": _complete_command_dirlist,
    "nuke": _complete_command_dirlist, 
    "dump": _complete_command_dirlist, 
    # sync tasks
    "auto": _complete_no_suggestions,
    "log": _complete_no_suggestions,
    "add": _complete_no_suggestions,
    "commit": _complete_no_suggestions,
    "push": _complete_no_suggestions,
    "pull": _complete_no_suggestions,
    "diff": _complete_no_suggestions,
    "status": _complete_no_suggestions,
    "branch": _complete_no_suggestions,
    # TODO: create a branch name completion handler checkout, and merge 
    "--merge": _complete_no_suggestions,
    "--checkout": _complete_no_suggestions,
    "--new-branch": _complete_no_suggestions,
    "--force-push": _complete_no_suggestions,
    "--soft-reset": _complete_no_suggestions,
    "--hard-reset": _complete_no_suggestions,
}

# INTERFACE

# complete gets passed $COMPLINE and needs to reparse argv[2] and 
def complete(ctx):
    # if MOLD_ROOT is not setup no completion 4 you
    if  ensure.check(ctx) != ensure.OK:
        return _complete_no_suggestions(ctx)

    # if no command show main until command 
    if ctx.command == None or ctx.command == 'mold': 
        return _completion_handlers['main'](ctx)
    try:
        if ctx.task == None:
            return _completion_handlers[ctx.command](ctx)   
    except:
        return _completion_handlers['main'](ctx)

    # if no task show command until task 
    try:
        _completion_handlers[ctx.task](ctx)
    except:
        return _completion_handlers[ctx.command](ctx)

