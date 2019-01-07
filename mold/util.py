'''
util defines an sane api for running executbales.
'''

import os 
import shlex
from shutil import which 
from subprocess import Popen

def cd(path):
    '''cd will change the current working directory for the util.exec and util.shell commands'''
    return os.chdir(path)

class ExecResult:
    '''ExecResult is a wrapper for the results of subprocess.Popen'''
    def __init__(self, status=None, out=None, err=None, fail=None):
        self.status = status
        self.out = out
        self.err = err
        self.fail = fail
    def check_ok(self):
        return self.fail == None and self.status == 0 

def exec(cmd, shell=False):
    '''shell runs executables that DONT need a TUI'''
    parsed = shlex.split(cmd)
    parsed[0] = which(parsed[0])
    if not parsed[0]:
       return ExecResult(fail=True) 
    p = Popen(parsed, shell=shell)
    (out, err) = p.communicate()
    status = p.returncode
    return ExecResult(status, out, err)

def shell(cmd):
    '''shell runs executables that need a TUI'''
    return exec(cmd, shell=True)

