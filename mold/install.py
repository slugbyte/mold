import os 
import sys
from shutil import which
import mold.fs as fs

def install():
    mold_root = '' 
    editor = os.environ['EDITOR']
    remote = ''
    print('Hit enter for defaults')
    mold_root = input('Enter direcotry in which to save mold content (~/.mold): ~/')
    if not mold_root:
        mold_root = os.environ['HOME'] + '/.mold'
    else:
        mold_root = os.environ['HOME'] + '/' + mold_root
    while not editor:
        choice  = input('Enter the command to you want use as a text editor (nano):')
        if not choice:
            editor  = which('nano')
        else:
            editor = which(choice)
            if not editor:
                print(f'${choice} not found.')
    print('whould you like to configure a git remote?')
    remote = input('Enter a git remote uri (none):')
    if not remote:
        remote = 'NONE'
    
    print('\nYou have selected the following options.')
    print(f'MOLD_ROOT = {mold_root}\nEDITOR = {editor}\nGIT REMOTE = {remote}')
    quit = input('\nWould you like continue the installation? Type anything to cancel:')
    if quit:
        print('canceled')
        return 

    



