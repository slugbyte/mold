from subprocess import Popen
from shutil import which 
import shlex

def get(table, key, fail=None):
    paths = key.split('.')
    try: 
        return table[key]
    except:
        return fail

class ExecResult:
    def __init__(self, status=None, out=None, err=None, fail=None):
        self.status = status
        self.out = out
        self.err = err
        self.fail = fail
    def check_ok(self):
        return self.fail == None and self.status == 0 

def exec(cmd):
    parsed = shlex.split(cmd)
    parsed[0] = which(parsed[0])
    if not parsed[0]:
       return ExecResult(fail=True) 
    p = Popen(parsed)
    (out, err) = p.communicate()
    status = p.returncode
    return ExecResult(status, out, err)
