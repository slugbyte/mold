'''
git defines an api for running git opperartions in DOT_ROOT

The Public interface returns a Bool on the success of the opperation
'''

import mold.env as env
import mold.util as util 

# PRIVATE
def _git_exec(args):
    util.cd(env.ROOT_DIR)
    return util.exec('git ' + args)

def _git_shell(args):
    util.cd(env.ROOT_DIR)
    return util.shell('git ' + args)

def _check_remote_uri(uri):
    '''checks that a git remote uri is valid'''
    print(f'Checking {uri}: ', end='')
    if not _git_exec('ls-remote ' + uri).check_ok():
        print(f'Sorry, that a not valid remote uri, make sure it exists.') 
        return False
    print('OK')
    return True

def _get_remote_name():
    r = _git_exec('remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[0]
    except: 
        return None

def _get_remote_uri():
    r = _git_exec('remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[1]
    except: 
        return None

# API INTERFACE
def init():
    if not _git_exec('init .').check_ok():
        print('Error: git init failed')
        return False
    if not _git_exec('add -A').check_ok():
        print('Error: git add -A failed')
        return False
    if not _git_exec('commit  -m "initial commit"').check_ok():
        print('Error: inital git commit failed')
        return False

def set_remote(uri):
    '''works as both git add and git set for the MOLD_ROOT'''
    if not _check_remote_uri(uri):
        return False
    name = _get_remote_name()
    if name:
        if not _git_exec('remote remove ' + name):
            return False
    if not _git_exec('remote add origin ' + uri):
        return False
    return True
