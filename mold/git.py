'''
git defines an api for running git opperartions in DOT_ROOT

The Public interface returns a Bool on the success of the opperation
'''

import mold.system as system 

# PRIVATE
def _git_exec(ctx, args):
    system.cd(ctx.MOLD_ROOT)
    return system.exec('git ' + args)

def _git_shell(ctx, args):
    system.cd(ctx.MOLD_ROOT)
    return system.shell('git ' + args)

def _check_remote_uri(ctx, uri):
    '''checks that a git remote uri is valid'''
    print(f'Checking {uri}: ', end='')
    if not _git_shell(ctx, 'ls-remote ' + uri).check_ok():
        print(f'Sorry, that a not valid remote uri, make sure it exists.') 
        return False
    print('OK')
    return True

def _get_remote_name(ctx):
    r = _git_shell(ctx, 'remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[0]
    except: 
        return None

def _get_remote_uri(ctx, ):
    r = _git_shell(ctx, 'remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[1]
    except: 
        return None

# API INTERFACE
def set_remote(ctx, uri):
    '''works as both git add and git set for the MOLD_ROOT'''
    if not uri:
        return False 
    if not _check_remote_uri(ctx, uri):
        return False
    name = _get_remote_name(ctx)
    if name:
        if not _git_shell(ctx, 'remote remove ' + name):
            return False
    if not _git_shell(ctx, 'remote add origin ' + uri):
        return False
    return True

def add(ctx):
    if not _git_shell(ctx, 'add -A').check_ok():
        return False
    return True

def status(ctx):
    if not _git_shell(ctx, 'status').check_ok():
        return False
    return True

def diff(ctx, githash='HEAD'):
    if not githash:
        githash= 'HEAD'
    if not _git_shell(ctx, f'diff {githash}').check_ok():
        return False
    return True

def commit(ctx, message):
    if message:
        if not _git_shell(ctx, f"commit -m '{message}'").check_ok():
            return False
        return True
    if not _git_shell(ctx, 'commit').check_ok():
        return False
    return True

def hard_reset(ctx, githash):
    if not githash:
        githash = 'HEAD'
    if not _git_shell(ctx, f"reset --hard {githash}").check_ok():
        return False
    return True

def soft_reset(ctx, githash):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(ctx, f"reset {githash}").check_ok():
        return False
    return True

def log(ctx):
    if not _git_shell(ctx, 'log').check_ok():
        return False
    return True

def branch(ctx):
    if not _git_shell(ctx, 'branch -av').check_ok():
        return False
    return True

def merge(ctx, branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(ctx, f'merge {branch}').check_ok():
        return False
    return True

def checkout(ctx, branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(ctx, f'checkout  {branch}').check_ok():
        return False
    return True

def new_branch(ctx, branch=None):
    if not branch:
        return False
    if not _git_shell(ctx, f'checkout -b {branch}').check_ok():
        return False
    return True

def pull(ctx, branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(ctx, f'pull origin {branch}').check_ok():
        return False
    return True

def push(ctx, branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(ctx, f'push origin {branch}').check_ok():
        return False
    return True

def force_push(ctx, branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(ctx, f'push origin {branch} --force').check_ok():
        return False
    return True

def init(ctx):
    if not _git_shell(ctx, 'init .').check_ok():
        print('Error: git init failed')
        return False
    if not _git_shell(ctx, 'add -A').check_ok():
        print('Error: git add -A failed')
        return False
    if not _git_shell(ctx, 'commit  -m "initial commit"').check_ok():
        print('Error: inital git commit failed')
        return False
    return True
