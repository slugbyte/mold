'''
install defines an api for installing a MOLD_ROOT.
'''

import mold.git as git 
import mold.fs as fs
import mold.env as env 
import mold.system as system
from mold.color import red, green, cyan , reset, yellow, magenta

# PRIVATE
BUILD_DIR = __file__.replace('install.py', 'assets')

def _log_success(extra='.'):
    print(f'''
{green}SUCCESS{reset}
A MOLD_ROOT has installed to {env.ROOT_DIR}{extra}
{yellow}Follow these IMPORTANT instructions to complete setting up mold.{reset}
First add the follwing two lines to your shell config file (i.e. ~/.bashrc).
    {magenta}export MOLD_ROOT='{env.ROOT_DIR}'
    source $MOLD_ROOT/mold-loader.sh{reset}
Next source your shell config (e.g. "source ~/.bashrc"). 
Then then you will be good to go, {green}Enjoy mold!{reset} :)''')


def _log_failure():
    print(f'''Sorry, something went wrong, a MOLD_ROOT was not installed.
Create an issue at https://github.com/slugbyte/mold/issues for support.''')

def _cleanup_and_fail():
    if fs.exists(env.ROOT_DIR):
        fs.rimraf(env.ROOT_DIR)
    _log_failure()

def _create_mold_root():
    try:
        if fs.exists(env.ROOT_DIR):
            fs.rimraf(env.ROOT_DIR)
        system.cd(BUILD_DIR)
        tarpath = BUILD_DIR + '/mold-root.tar.gz'
        fs.unpack_tarball(tarpath)
        fs.mv(BUILD_DIR + '/mold-root', env.ROOT_DIR)
        return True
    except: 
        return False

def _setup_git(remote):
    system.cd(env.ROOT_DIR)
    if not git.init(remote):
        return False
    return True

# INTERFACE
def install():
    print(f'{green}Installing{reset} a MOLD_ROOT in {env.ROOT_DIR}')
    if fs.exists(env.ROOT_DIR):
        print(f'\n{red}Hmm,{reset} {env.ROOT_DIR} {red}allready exits.{reset}\nDo you want to remove it and continue? {magenta}[Leave blank to continue]{reset}')
        cancel = input(f'{cyan}Type anything to cancel:{reset} ')
        if cancel: 
            return print(f'\nOk, MOLD_ROOT installation canceled.')
    if not _create_mold_root():
        return _cleanup_and_fail()
    if not git.init():
        return _cleanup_and_fail()
    print(f'\nDo you want to setup a git remote? {magenta}[Leave blank to skip]{reset}')
    remote = input(f'{cyan}Enter a git uri:{reset} ')
    if not remote:
        return _log_success(' with out a remote remote repository.')
    if not git.set_remote(remote):
        return _log_success(f'''.
{red}However, git failed to add the remote uri{reset} {remote} 
Run mold help and read the about using "mold --set-remote" to add a remote.''')
    if not git.push():
        return _log_success(f'''.
{red}However, git failed to push to the remote uri {remote}{reset}
You remote probbly allready has content in it. If you want to 
overwrite the remote run {cyan}mold sync --force-push{reset}, or you can run
{cyan}mold --install{reset} again and overwrite the current MOLD_ROOT.''')
    _log_success(f' with the remote repository {remote}')
