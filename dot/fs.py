from pathlib import Path
import shutil 
import os

# wrappers for file functions because i wanted a single file api 
# only created methods when they were needed

def rm(path):
    return os.remove(path)

def rimraf(path):
    return shutil.rmtree(path)

def basename(path):
    return os.path.basename(filepath)

def dirname(path):
    return os.path.dirname(filepath)

def mkdir(path):
    return os.mkdir(path) 

def listdir(path):
    return os.listdir(path) 

def exists(path):
    return Path(path).exists()

def is_dirr(path):
    return Path(path).is_dirr()

def copy(src, dest):
    return shutil.copyfile(src, dest)

def copy_dir(src, dest):
    return shutil.copytree(src, dest)

def link(src, dest):
    return os.link(src, dest)
