import time
import os 
import sys
import tarfile
from shutil import which
from subprocess import call 

import mold.fs as fs
import mold.env as env 
from mold.util import exec

BUILD_DIR = __file__.replace('install.py', '')

def create_mold_root():
    if fs.exists(env.ROOT_DIR):
        fs.rimraf(env.ROOT_DIR)
    os.chdir(BUILD_DIR)
    tarpath = BUILD_DIR + 'mold-root.tar.gz'
    tar = tarfile.open(tarpath, 'r:gz')
    tar.extractall()
    tar.close()
    fs.mv(BUILD_DIR + '/mold-root', env.ROOT_DIR)

def setup_git(remote):
    os.chdir(env.ROOT_DIR)
    exec('git init .')
    exec('git add -A')
    exec('git commit -m inital-commit')
    if not remote: 
        return print(f'\n{env.ROOT_DIR} is setup complete\nRun \'mold help\' for help setting up a git remote')
    if remote:
        result = exec(f'git remote add origin {remote}')
        if result.check_ok():
            exec('git push origin HEAD')

def install():
    if fs.exists(env.ROOT_DIR):
        print(f'{env.ROOT_DIR} allready exits, want to continue and replace it?')
        quit = input('Hit enter to contine, type anything to abort: ')
        if quit:
            print('intall cancled')
            return 
    create_mold_root()
    print('Do you want to set the git remote? leave blank for none')
    setup_git(input('Enter a git uri: '))
    
