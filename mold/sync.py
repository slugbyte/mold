'''
sync defines the logic for maintaining a MOLD_ROOT using git 
'''

import mold.git as git 
from mold.query import query

# sync help 
# sync 
    # (pull add commit push)
# sync push 
# sync pull 
# sync commit
def _auto(options):
    print('AUTO')
    message = query(options, 0)
    if not git.pull():
        print('UHHHG, unable to pull origin')
        return False
    if not git.add():
        print('DARN, unable to add changes')
        return False
    if not git.commit(message):
        print('FOOY, git commit failed')
        return False
    if not git.push():
        print('GUESS WHUT, FAIL now? ... push to origin')
        return False
    return True

_task_handlers = {
    "auto": _auto,
}

def handle_task(cmd, options):
    # is it a specifc task? -> run it 
    # else -> wun AUTO
    task = query(options, 0)
    for current in ['push', 'pull', 'sync', 'stat', 'diff', 'add', 'commit', 'auto', 'help']:
        if task == current:
            _task_handlers[task](options)
            return print('BOOM FOUND TASK:', task)
    print(f'mold sync can\'t {task} yet.')
