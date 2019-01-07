'''
fs defines a consistant api for working with the file system. 
It is made of wrapper functions for methods in os, shutil, tarfile, and pathlib.
'''

import os
import shutil
import tarfile
from pathlib import Path

# wrappers for file functions because i wanted a single file api 
# only created methods when they were needed

def mv(src, dest):
    return os.replace(src, dest)

def rm(path):
    return os.remove(path)

def rimraf(path):
    return shutil.rmtree(path)

def basename(path):
    return os.path.basename(path)

def dirname(path):
    return os.path.dirname(path)

def mkdir(path):
    return os.mkdir(path) 

def mkfile(path):
    return Path(path).touch()

def listdir(path):
    return os.listdir(path) 

def exists(path):
    return Path(path).exists()

def is_dir(path):
    return Path(path).is_dir()

def copy(src, dest):
    return shutil.copyfile(src, dest)

def copy_dir(src, dest):
    return shutil.copytree(src, dest)

def link(src, dest):
    return os.link(src, dest)

def unpack_tarball(path):
    tar = tarfile.open(path, 'r:gz')
    tar.extractall()
    tar.close()
