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

def _check_remote_uri(ctx, uri=None):
    '''checks that a git remote uri is valid'''
    print(f'Checking {uri}: ', end='')
    result = _git_exec(ctx, 'ls-remote ' + uri)
    if not result.check_ok():
        print(f'Sorry, that a not valid remote uri, make sure it exists.') 
        return result
    print('OK')
    return result

def _get_remote_name(ctx):
    r = _git_exec(ctx, 'remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[0]
    except: 
        return None

def _get_remote_uri(ctx):
    r = _git_exec(ctx, 'remote -v')
    if not r.check_ok() or not r.out:
        return None
    try:
        return r.out.split(' ')[0].split('\t')[1]
    except: 
        return None

def _get_current_branch(ctx):
    r = _git_exec(ctx, 'branch')
    if not r.check_ok() or not r.out:
        print('fooey', r.check_ok())
        return None
    try:
        for branch in r.out.split('\n'):
            if branch.strip().startswith('*'):
                return branch.replace('*', '').strip()
    except: 
        return None

# API INTERFACE
def set_remote(ctx, uri=None):
    '''works as both git add and git set for the MOLD_ROOT'''
    if not uri:
        return system.fail()
    if not _check_remote_uri(ctx, uri):
        return system.fail()
    # TODO: consider refactoring out all the {name} and force for mold to use origin ?
    name = _get_remote_name(ctx)
    if name:
        result = _git_shell(ctx, 'remote remove ' + name) 
        if not result.check_ok():
            return result
    name = name or 'origin'
    result = _git_shell(ctx, f'remote add {name} {uri}')
    if not result.check_ok():
        return result
    result = _git_shell(ctx, f'fetch {name}')
    if not result.check_ok():
        print(f'WARNING: failed to git fetch {name}')
        return result 
    print('MOLD_ROOT\'s git remote origin is now:', uri)
    return result 


def add(ctx):
    return _git_shell(ctx, 'add -A')

def status(ctx):
    return _git_shell(ctx, 'status')

def remote(ctx):
    return _git_shell(ctx, 'remote -v')

def diff(ctx, githash=None):
    if not githash:
        githash= 'HEAD'
    return _git_shell(ctx, f'diff {githash}')

def commit(ctx, message=None):
    if message:
        return _git_shell(ctx, f"commit -m '{message}'")
    return _git_shell(ctx, 'commit')

def hard_reset(ctx, githash=None):
    if not githash:
        githash = 'HEAD'
    return _git_shell(ctx, f"reset --hard {githash}")

def soft_reset(ctx, githash=None):
    if not githash:
        githash = 'HEAD'
    return _git_shell(ctx, f"reset --soft {githash}")

def log(ctx):
    return _git_shell(ctx, 'log')

def branch(ctx):
    return _git_shell(ctx, 'branch -av')

def merge(ctx, branch=None):
    print('merging', branch)
    if not branch:
        branch = 'HEAD'
    return _git_shell(ctx, f'merge {branch}')

def checkout(ctx, branch=None):
    if not branch:
        branch = 'HEAD'
    return _git_shell(ctx, f'checkout  {branch}')

def new_branch(ctx, branch=None):
    if not branch:
        return system.fail()
    return _git_shell(ctx, f'checkout -b {branch}')

def pull(ctx, branch=None):
    if not branch:
        branch = _get_current_branch(ctx)
    return _git_shell(ctx, f'pull origin {branch}')

def push(ctx, branch=None):
    if not branch:
        branch = 'HEAD'
    return _git_shell(ctx, f'push origin {branch}')

def force_push(ctx, branch=None):
    if not branch:
        branch = 'HEAD'
    _git_shell(ctx, f'push origin {branch} --force')

def clone(ctx, url=None):
    # clone uses system.exec and shell because there is not MOLD_ROOT to cd into
    if not uri:
        print('ERROR: git clone requires a git-uri')
        return system.fail()
    print(f'Checking {uri}: ', end='')
    result = _check_remote_uri(ctx, uri)
    if not result.check_ok():
        return result
    return system.shell(f'git clone {uri} {ctx.MOLD_ROOT}' )

def init(ctx):
    result = _git_shell(ctx, 'init .')
    if not result.check_ok():
        print('Error: git init failed')
        return result
    result = _git_shell(ctx, 'add -A')
    if not result.check_ok():
        print('Error: git add -A failed')
        return result
    result = _git_shell(ctx, 'commit  -m "initial commit"') 
    if not result .check_ok():
        print('Error: inital git commit failed')
    return result 

