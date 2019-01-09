'''
git defines an api for running git opperartions in DOT_ROOT

The Public interface returns a Bool on the success of the opperation
'''

import mold.env as env
import mold.system as system 

# PRIVATE
def _git_exec(args):
    system.cd(env.ROOT_DIR)
    return system.exec('git ' + args)

def _git_shell(args):
    system.cd(env.ROOT_DIR)
    return system.shell('git ' + args)

def _check_remote_uri(uri):
    '''checks that a git remote uri is valid'''
    print(f'Checking {uri}: ', end='')
    if not _git_shell('ls-remote ' + uri).check_ok():
        print(f'Sorry, that a not valid remote uri, make sure it exists.') 
        return False
    print('OK')
    return True

def _get_remote_name():
    r = _git_shell('remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[0]
    except: 
        return None

def _get_remote_uri():
    r = _git_shell('remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[1]
    except: 
        return None

# API INTERFACE
def set_remote(uri):
    '''works as both git add and git set for the MOLD_ROOT'''
    if not uri:
        return False 
    if not _check_remote_uri(uri):
        return False
    name = _get_remote_name()
    if name:
        if not _git_shell('remote remove ' + name):
            return False
    if not _git_shell('remote add origin ' + uri):
        return False
    return True

def add():
    if not _git_shell('add -A').check_ok():
        return False
    return True

def status():
    if not _git_shell('status').check_ok():
        return False
    return True

def diff(githash='HEAD'):
    if not githash:
        githash= 'HEAD'
    if not _git_shell(f'diff {githash}').check_ok():
        return False
    return True

def commit(message):
    if message:
        if not _git_shell(f"commit -m '{message}'").check_ok():
            return False
        return True
    if not _git_shell('commit').check_ok():
        return False
    return True

def hard_reset(githash='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f"reset --hard {githash}").check_ok():
        return False
    return True

def soft_reset(githash='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f"reset {githash}").check_ok():
        return False
    return True

def log():
    if not _git_shell('log').check_ok():
        return False
    return True

def branch():
    if not _git_shell('branch -av').check_ok():
        return False
    return True

def merge(branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f'merge {branch}').check_ok():
        return False
    return True

def checkout(branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f'checkout  {branch}').check_ok():
        return False
    return True

def new_branch(branch=None):
    if not branch:
        return False
    if not _git_shell(f'checkout -b {branch}').check_ok():
        return False
    return True

def pull(branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f'pull origin {branch}').check_ok():
        return False
    return True

def push(branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f'push origin {branch}').check_ok():
        return False
    return True

def force_push(branch='HEAD'):
    if not branch:
        branch = 'HEAD'
    if not _git_shell(f'push origin {branch} --force').check_ok():
        return False
    return True

def init():
    if not _git_shell('init .').check_ok():
        print('Error: git init failed')
        return False
    if not _git_shell('add -A').check_ok():
        print('Error: git add -A failed')
        return False
    if not _git_shell('commit  -m "initial commit"').check_ok():
        print('Error: inital git commit failed')
        return False
    return True
