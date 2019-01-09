'''
sync defines the logic for maintaining a MOLD_ROOT using git 
'''

import mold.git as git 
from mold.util import query

def _auto(options):
    message = query(options, 1)
    if not git.pull():
        return False
    if not git.add():
        return False
    if not git.commit(message):
        return False
    if not git.push():
        return False
    return True

def _make_no_arg_git_task(git_method):
    git_methods = {
        "add": git.add,
        "log": git.log,
        "status": git.status,
        "branch": git.branch,
    }
    def handler(options):
        print('foo yee', git_method)
        git_methods[git_method]()
    return handler

def _make_one_arg_git_task(git_method):
    git_methods = {
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
    def handler(options):
        arg = query(options, 1)
        print('foo yee', git_method, arg)
        git_methods[git_method](arg)
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

def handle_task(cmd, options):
    # is it a specifc task? -> run it 
    # else -> wun AUTO
    task = query(options, 0)
    for current in [ 'help', 'auto', 'diff', 'push', 'pull', 'add',
        'log', 'status', 'branch', 'commit', '--merge', '--checkout',
        '--new-branch', '--force-push', '--soft-reset', '--hard-reset', ]:
        if task == current:
            _task_handlers[task](options)
            return print('BOOM FOUND TASK:', task)
    print(f'mold sync can\'t {task} yet.')
