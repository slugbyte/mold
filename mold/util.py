'''
util defines an sane api for running executbales.
'''

import os 
import shlex
import subprocess
from shutil import which 

def cd(path):
    '''cd will change the current working directory for the util.exec and util.shell commands'''
    return os.chdir(path)

class ExecResult:
    '''ExecResult is a wrapper for the results of subprocess.Popen'''
    def __init__(self, status=None, out=None, err=None, fail=None):
        self.status = status
        try:
            self.out = out.decode('utf8')
        except:
            self.out = None
        try:
            self.err = err.decode('utf8')
        except:
            self.out = None
        self.fail = fail
    def check_ok(self):
        return self.fail == None and self.status == 0 
    def check_output(self):
        return bool(self.out) or bool(self.err)

def exec(cmd):
    '''shell runs executables that DONT need a TUI'''
    parsed = shlex.split(cmd)
    parsed[0] = which(parsed[0])
    if not parsed[0]:
       return ExecResult(fail=True) 
    p = subprocess.Popen(parsed, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()
    status = p.returncode
    return ExecResult(status, out, err)

def shell(cmd):
    '''shell runs executables that need a TUI'''
    parsed = shlex.split(cmd)
    parsed[0] = which(parsed[0])
    if not parsed[0]:
       return ExecResult(fail=True) 
    status = subprocess.Popen(parsed, shell=True).wait()
    return ExecResult(status, None, None)

