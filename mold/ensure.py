import mold.env as env 
import mold.fs as fs

# ensure's errno values
ENV_ERROR = 1
DIR_ERROR = 2
OK = 0 

# Singleton state (HAHHHAH I hate singletons, me sooo lazy :p)
_result = -1 # -1 == check no run yet

# Singleton interface
def _set_result(errno):
    global _result
    _result = errno
    return errno

def warning(): 
    if _result == ENV_ERROR:
        return "Make sure your DOT_ROOT and EDITOR environment variables are set"
    if _result == DIR_ERROR:
        return '''Looks like your DOT_ROOT directory is missing or broken. 
Try runing mold --install, or mold --fix-root'''

def check():
    if _result != -1:
        return _result
    if (not env.ROOT_DIR) or (not env.EDITOR):
        return _set_result(ENV_ERROR)
    if (not fs.exists(env.ROOT_DIR)) or (not fs.is_dir(env.ROOT_DIR)):
        return _set_result(DIR_ERROR)
    for d in ['conf', 'plug', 'temp', 'drop', 'pack']:
        if not fs.exists(env.ROOT_DIR + '/' + d):
            return _set_result(DIR_ERROR)
