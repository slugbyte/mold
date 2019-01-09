'''
install defines an api for installing a MOLD_ROOT.
'''

import mold.git as git 
import mold.fs as fs
import mold.env as env 
import mold.util as util

# PRIVATE
BUILD_DIR = __file__.replace('install.py', 'assets')

def _log_success(extra='.'):
    print(f'''
A MOLD_ROOT has installed{extra}
Follow these IMPORTANT instructions to complete setting up mold.
First add the follwing two lines to your shell config file (i.e. ~/.bashrc).
    export MOLD_ROOT='{env.ROOT_DIR}'
    source $MOLD_ROOT/mold-loader.sh
Then then source your shell config (e.g. "source ~/.bashrc"). 
Finally you will be good to go, Enjoy mold! :)''')


def _log_failure():
    print(f'''Sorry, something went wrong, a MOLD_ROOT was not installed.
Create an issue at https://github.com/slugbyte/mold/issues for support.''')

def _create_mold_root():
    try:
        if fs.exists(env.ROOT_DIR):
            fs.rimraf(env.ROOT_DIR)
        util.cd(BUILD_DIR)
        tarpath = BUILD_DIR + '/mold-root.tar.gz'
        fs.unpack_tarball(tarpath)
        fs.mv(BUILD_DIR + '/mold-root', env.ROOT_DIR)
        return True
    except: 
        if fs.exists(env.ROOT_DIR):
            fs.rimraf(env.ROOT_DIR)
        return False

def _setup_git(remote):
    util.cd(env.ROOT_DIR)
    if not git.init(remote):
        return False
    return True

# INTERFACE
def install():
    print(f'Installing a MOLD_ROOT in {env.ROOT_DIR}')
    if fs.exists(env.ROOT_DIR):
        print(f'\nHmm, {env.ROOT_DIR} allready exits.\nDo you want to remove it and continue? [Leave blank to continue]')
        cancel = input('Type anything to cancel: ')
        if cancel: 
            return print('\nOk, MOLD_ROOT installation canceled.')
    if not _create_mold_root():
        return _log_failure()
    print('\nDo you want to setup a git remote? [Leave blank to skip]')
    remote = input('Enter a git uri: ')
    if not remote:
        return _log_success(' with out a remote remote repository.')
    if not git.init():
        return _log_success(f'''. However, git failed to add the remote uri ({remote}). 
Run mold help and read the about using "mold --set-remote" to add a remote.
''')
    _log_success('with the remote repository {remote}.')
