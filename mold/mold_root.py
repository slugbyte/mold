import mold.git as git 
from mold.install import install
import mold.fs as fs

# PRIVATE
# Singleton state (HAHHHAH I hate singletons, me sooo lazy :p)
_result = -1 # -1 == check no run yet

def _set_result(errno):
    global _result
    _result = errno
    return errno

# INTERFACE

# FAUX ENUM
ENV_ERROR = 1
DIR_ERROR = 2
ROOT_ERROR = 3
OK = 0 

def warning(ctx): 
    if _result == ENV_ERROR:
        return "Make sure your MOLD_ROOT and EDITOR environment variables are set"
    if _result == ROOT_ERROR:
        return '''Looks like your MOLD_ROOT directory hasent been set up
Try runing mold --install'''
    if _result == DIR_ERROR:
        return '''Hmmm, Somthing is wrong with your MOLD_ROOT directory
Try runing mold --fix-root'''

def check(ctx):
    # TODO: on refactor where check uses warning 
    # dont long anythin if ctx.command == 'complete'
    if _result != -1:
        return _result
    if (not ctx.MOLD_ROOT) or (not fs.exists(ctx.MOLD_ROOT)) or (not fs.is_dir(ctx.MOLD_ROOT)):
        return _set_result(ROOT_ERROR)
    for d in ['conf', 'plug', 'fold', 'file', 'exec']:
        if not fs.exists(ctx.MOLD_ROOT + '/' + d):
            return _set_result(DIR_ERROR)
    return OK

def _clone(ctx):
    # TODO LINK ALL THE CONFS
    if not ctx.command:
        print('USAGE ERROR: mising git-uri\n    e.g. mold --set-remote [git-uri]')
        return ctx.FAIL
    if fs.exists(ctx.MOLD_ROOT):
        if not ctx.check_flag_set('--force'):
            print(f'WARNING: {ctx.MOLD_ROOT} allready exists do you want to remove it? leave empty to continue')
            abort = input(f'type anything to abort cloning: ')
            if (abort):
                print('clone aborted')
                return ctx.OK
        fs.rimraf(ctx.MOLD_ROOT) 
    git.clone(ctx, ctx.command)
    return ctx.OK

def _set_remote(ctx):
    if not ctx.command:
        print('USAGE ERROR: mising git-uri\n    e.g. mold --set-remote [git-uri]')
        return ctx.FAIL
    git.set_remote(ctx, ctx.command)
    return ctx.OK

def handle_flag(ctx):
    if ctx.check_install_set():
        install(ctx)
        return False
    if ctx.check_clone_set():
        _clone(ctx)
        return False
    if ctx.check_set_remote_set():
        _set_remote(ctx)
        return False
    print('hit handle_flag')

