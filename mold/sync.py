'''
sync defines the logic for maintaining a MOLD_ROOT using git 
'''

import mold.git as git 
from mold.util import query

def _auto(ctx):
    message = ctx.get_option(0)
    if not git.pull(ctx):
        return False
    if not git.add(ctx):
        return False
    if not git.commit(ctx, message):
        return False
    if not git.push(ctx):
        return False
    return True

def _make_no_arg_git_task(name):
    methods = {
        "add": git.add,
        "log": git.log,
        "branch": git.branch,
        "status": git.status,
    }
    def handler(ctx):
        methods[name](ctx)
    return handler

def _make_one_arg_git_task(name):
    methods = {
        "diff": git.diff,
        "push": git.push,
        "pull": git.pull,
        "commit": git.commit,
        "merge": git.merge,
        "checkout": git.checkout,
        "new_branch": git.new_branch,
        "hard_reset": git.hard_reset,
        "soft_reset": git.soft_reset,
        "force_push": git.force_push,
    }
    def handler(ctx):
        arg = ctx.get_option(0)
        methods[name](ctx, arg)
    return handler

_task_handlers = {
    # custom 
    "auto": _auto,
    # curry no arg
    "add": _make_no_arg_git_task('add'),
    "log": _make_no_arg_git_task('log'),
    "status": _make_no_arg_git_task('status'),
    "branch": _make_no_arg_git_task('branch'),
    # curry one arg
    "diff": _make_one_arg_git_task('diff'),
    "push": _make_one_arg_git_task('push'),
    "pull": _make_one_arg_git_task('pull'),
    "commit": _make_one_arg_git_task('commit'),
    "--merge": _make_one_arg_git_task('merge'),
    "--checkout": _make_one_arg_git_task('checkout'),
    "--new-branch": _make_one_arg_git_task('new_branch'),
    "--soft-reset": _make_one_arg_git_task('soft_reset'),
    "--hard-reset": _make_one_arg_git_task('hard_reset'),
    "--force-push": _make_one_arg_git_task('force_push'),
}

def handle_task(ctx):
    # TODO: consider not default to the long help for all the commands
    # Instad there could be a shor USAGE: comand [task] [options] for
    # each command? **FUTURE**
    try:
        _task_handlers[ctx.task](ctx)
    except:
        print(f'mold sync can\'t {ctx.task} yet.')

