'''
install defines an api for installing a MOLD_ROOT.
'''

import mold.git as git 
import mold.fs as fs
import mold.system as system
from mold.color import red, green, cyan , reset, yellow, magenta

# PRIVATE
BUILD_DIR = __file__.replace('install.py', 'assets')

def _log_success(ctx, extra='.'):
    print(f'''
{green}SUCCESS{reset}
A MOLD_ROOT has installed to {ctx.MOLD_ROOT}{extra}
{yellow}Follow these IMPORTANT instructions to complete setting up mold.{reset}
First add the follwing two lines to your shell config file (i.e. ~/.bashrc).
    {magenta}export MOLD_ROOT='{ctx.MOLD_ROOT}'
    source $MOLD_ROOT/mold-loader.sh{reset}
Next source your shell config (e.g. "source ~/.bashrc"). 
Then then you will be good to go, {green}Enjoy mold!{reset} :)''')


def _log_failure(ctx):
    print(f'''Sorry, something went wrong, a MOLD_ROOT was not installed.
Create an issue at https://github.com/slugbyte/mold/issues for support.''')

def _cleanup_and_fail(ctx):
    if fs.exists(ctx.MOLD_ROOT):
        fs.rimraf(ctx.MOLD_ROOT)
    _log_failure(ctx )

def _create_mold_root(ctx):
    try:
        if fs.exists(ctx.MOLD_ROOT):
            fs.rimraf(ctx.MOLD_ROOT)
        system.cd(BUILD_DIR)
        tarpath = BUILD_DIR + '/mold-root.tar.gz'
        fs.unpack_tarball(tarpath)
        fs.mv(BUILD_DIR + '/mold-root', ctx.MOLD_ROOT)
        return True
    except: 
        return False

def _setup_git(ctx, remote):
    system.cd(ctx.MOLD_ROOT)
    if not git.init(ctx, remote):
        return False
    return True

# INTERFACE
def install(ctx):
    print(f'{green}Installing{reset} a MOLD_ROOT in {ctx.MOLD_ROOT}')
    if fs.exists(ctx.MOLD_ROOT):
        print(f'\n{red}Hmm,{reset} {ctx.MOLD_ROOT} {red}allready exits.{reset}\nDo you want to remove it and continue? {magenta}[Leave blank to continue]{reset}')
        cancel = input(f'{cyan}Type anything to cancel:{reset} ')
        if cancel: 
            return print(f'\nOk, MOLD_ROOT installation canceled.')
    if not _create_mold_root(ctx):
        return _cleanup_and_fail(ctx)
    if not git.init(ctx):
        return _cleanup_and_fail(ctx)
    # TODO: check ctx for flag --remote-uri 
    print(f'\nDo you want to setup a git remote? {magenta}[Leave blank to skip]{reset}')
    remote = input(f'{cyan}Enter a git uri:{reset} ')
    if not remote:
        return _log_success(ctx, ' with out a remote remote repository.')
    if not git.set_remote(ctx, remote):
        return _log_success(ctx, f'''.
{red}However, git failed to add the remote uri{reset} {remote} 
Run mold help and read the about using "mold --set-remote" to add a remote.''')
    if not git.push(ctx):
        return _log_success(ctx, f'''.
{red}However, git failed to push to the remote uri {remote}{reset}
You remote probbly allready has content in it. If you want to 
overwrite the remote run {cyan}mold sync --force-push{reset}, or you can run
{cyan}mold --install{reset} again and overwrite the current MOLD_ROOT.''')
    _log_success(ctx, f' with the remote repository {remote}')
