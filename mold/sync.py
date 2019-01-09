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
        "stat": git.stat,
        "push": git.push,
        "pull": git.pull,
        "force_push": git.force_push,
    }
    def handler(options):
        print('foo yee', git_method)
        git_methods[git_method]()
    return handler

def _make_one_arg_git_task(git_method):
    git_methods = {
        "diff": git.diff,
        "commit": git.commit,
        "hard_reset": git.hard_reset,
    }
    def handler(options):
        print('foo yee', git_method)
        arg = query(options, 1)
        git_methods[git_method](arg)
    return handler

_task_handlers = {
    "auto": _auto,
    "add": _make_no_arg_git_task('add'),
    "log": _make_no_arg_git_task('log'),
    "stat": _make_no_arg_git_task('stat'),
    "diff": _make_no_arg_git_task('diff'),
    "push": _make_no_arg_git_task('push'),
    "pull": _make_no_arg_git_task('pull'),
    "--force-push": _make_no_arg_git_task('force_push'),
    "diff": _make_one_arg_git_task('diff'),
    "commit": _make_one_arg_git_task('commit'),
    "--hard-reset": _make_one_arg_git_task('hard_reset'),
}

def handle_task(cmd, options):
    # is it a specifc task? -> run it 
    # else -> wun AUTO
    task = query(options, 0)
    for current in ['push', 'pull', 'sync', 'stat', 'diff', 'add', 'commit', 'auto', 'log', 'help', '--force-push', '--hard-reset']:
        if task == current:
            _task_handlers[task](options)
            return print('BOOM FOUND TASK:', task)
    print(f'mold sync can\'t {task} yet.')
