'''
install defines an api for installing a MOLD_ROOT.
'''

import mold.git as git 
import mold.fs as fs
import mold.env as env 
import mold.util as util

# PRIVATE
BUILD_DIR = __file__.replace('install.py', '')

def _create_mold_root():
    if fs.exists(env.ROOT_DIR):
        fs.rimraf(env.ROOT_DIR)
    util.cd(BUILD_DIR)
    tarpath = BUILD_DIR + 'mold-root.tar.gz'
    fs.unpack_tarball(tarpath)
    fs.mv(BUILD_DIR + '/mold-root', env.ROOT_DIR)

def _setup_git(remote):
    util.cd(env.ROOT_DIR)
    if not git.init():
        return 
    
    if not remote: 
        return print(f'\n{env.ROOT_DIR} is setup complete\nRun \'mold help\' for help setting up a git remote')
    if remote:
        result = exec(f'git remote add origin {remote}')
        if result.check_ok():
            exec('git push origin HEAD')

# INTERFACE
def install():
    if fs.exists(env.ROOT_DIR):
        print(f'{env.ROOT_DIR} allready exits, want to continue and replace it?')
        quit = input('Hit enter to contine, type anything to abort: ')
        if quit:
            print('intall cancled')
            return 
    _create_mold_root()
    print('Do you want to set the git remote? leave blank for none')
    _setup_git(input('Enter a git uri: '))
    
