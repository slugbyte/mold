import mold.fs as fs
import mold.git as git 
from mold.install import install
from mold.color import get_color

# PRIVATE
# Singleton state (HAHHHAH I hate singletons, me sooo lazy :p)
def check(ctx):
    red = get_color(ctx, 'red')
    yellow = get_color(ctx, 'yellow')
    reset = get_color(ctx, 'reset')
    # TODO: on refactor where check uses warning 
    # dont long anythin if ctx.command == 'complete'
    if ctx.check_flag_set('--complete'):
        return ctx.OK
    if (not ctx.MOLD_ROOT) or (not fs.exists(ctx.MOLD_ROOT)) or (not fs.is_dir(ctx.MOLD_ROOT)):
        print(f'''{red}ERROR:{reset} Looks like your MOLD_ROOT directory hasent been set up yet.
    {yellow}Try runing "mold root --install"{reset}''')
        return ctx.MOLD_ROOT_ERROR
    for d in ['conf', 'plug', 'fold', 'file', 'exec']:
        if not fs.exists(ctx.MOLD_ROOT + '/' + d):
            print(f'''{red}ERROR:{reset} Somthing is wrong with your MOLD_ROOT directory.
    {yellow}Try runing "mold root --fix"{reset}''')
            return ctx.MOLD_ROOT_DIRS_ERROR
    return ctx.OK

def _clone(ctx):
    red = get_color(ctx, 'red')
    cyan = get_color(ctx, 'cyan')
    reset = get_color(ctx, 'reset')
    # TODO LINK ALL THE CONFS
    if not ctx.task:
        print('{red}USAGE ERROR:{reset} mising git-uri\n    e.g. mold root --set-remote [git-uri]')
        return ctx.FAIL
    if fs.exists(ctx.MOLD_ROOT):
        if not ctx.check_flag_set('--force'):
            print(f'{red}WARNING:{reset} {ctx.MOLD_ROOT} allready exists do you want to remove it?')
            abort = 'y' != input(f'{cyan}Do you want to contiune the installation? y/n:{reset} ').strip()
            if (abort):
                print('Ok, mold --clone aborted.')
                return ctx.OK
        fs.rimraf(ctx.MOLD_ROOT) 
    git.clone(ctx, ctx.task)
    result = check(ctx)
    if result != ctx.OK:
        return result
    # TODO run mold root check to see if the dirs are OK
    ctx.link_conf()
    return ctx.OK

def _set_remote(ctx):
    if not ctx.task:
        print('USAGE ERROR: mising git-uri\n    e.g. mold root --set-remote [git-uri]')
        return ctx.FAIL
    git.set_remote(ctx, ctx.command)
    return ctx.OK

def handle_flag(ctx):
    if ctx.check_install_set():
        return install(ctx)
    if ctx.check_clone_set():
        return _clone(ctx)
    if ctx.check_set_remote_set():
        return _set_remote(ctx)
    print('hit handle_flag')
    return ctx.FAIL

