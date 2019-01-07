'''
git defines an api for running git opperartions in DOT_ROOT
'''

import mold.env as env
import mold.util as util 

def git_exec(args):
    util.cd(env.ROOT_DIR)
    return util.exec('git ' + args)

def git_shell(args):
    util.cd(env.ROOT_DIR)
    return util.shell('git ' + args)

def init():
    if not git_exec('init .').check_ok():
        print('Error: git init failed')
        return False
    if not git_exec('add -A').check_ok():
        print('Error: git add -A failed')
        return False
    if not git_exec('commit  -m "initial commit"').check_ok():
        print('Error: inital git commit failed')
        return False

def check_remote_uri(uri):
    '''checks that a git remote uri is valid'''
    print(f'Checking {uri}: ', end='')
    if not git_exec('ls-remote ' + uri).check_ok():
        print(f'Sorry, that a not valid remote uri, make sure it exists.') 
        return False
    print('OK')
    return True

def get_remote_name():
    r = git_exec('remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[0]
    except: 
        return None

def get_remote_uri():
    r = git_exec('remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[1]
    except: 
        return None

def set_remote(uri):
    '''works as both git add and git set for the MOLD_ROOT'''
    if not check_remote_uri(uri):
        return False
    name = get_remote_name()
    if name:
        if not git_exec('remote remove ' + name):
            return False
    if not git_exec('remote add origin ' + uri):
        return False
    return True
