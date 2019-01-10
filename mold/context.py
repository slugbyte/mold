'''
a MoldContext parses and stores sys.argv and os.environ, it also has several constants and provieds
some convience methods. One context gets created in __main__ and is passed through the entire app.
'''
from shutil import which 
import mold.fs as fs
from mold.util import query

_flags = set(['complete', '--color', '-v'])

# STORES ARGS AND ENV VARS
class MoldContext:
    def __init__(self, sys_argv, os_environ):
        # parse and strip flags
        mold_argv = [] # argv witout flags or path to file being executed
        flags = set([]) 
        for arg in sys_argv:
            if _flags.issuperset([arg]):
                flags.add(arg)
            else:
                mold_argv.append(arg)

        self.sys_argv  = sys_argv
        # mold_argv is offset by one when the completion is running
        if flags.issuperset(['complete']):
            self.mold_argv = mold_argv[1:]
        else: 
            self.mold_argv = mold_argv
        self.command = query(self.mold_argv, 1)
        self.task = query(self.mold_argv, 2)
        self.options = self.mold_argv[3:]
        self.flags = flags

        # PARSED ENVIRON
        self.HOME = query(os_environ, 'HOME')
        self.EDITOR = query(os_environ, 'EDITOR') or which('atom') or which('vim') or which('nano')
        self.MOLD_ROOT = query(os_environ, 'MOLD_ROOT') or (HOME +'/.mold')
        self.MOLD_DEBUG = bool(query(os_environ, 'MOLD_DEBUG'))
        self.MOLD_COLOR = bool(query(os_environ, 'MOLD_COLOR'))

        # CONSTANTS
        # TODO: evaluate if colors in color.py should be migrated to context contants
        self.MOLD_MAGIC = '__MAGIC_MOLD__' # used by _mold (bash script) for knowing when to complete file names
        # TODO: CREATE SOME KIND OF SEMANTIC EXIT CODES
        self.EXIT_STATUS_OK = 0
        self.EXIT_STATUS_FAIL = 1
        self.EXIT_STATUS_DEVELOPER_TODO = 2

    def check_has_options(self): return len(self.options) != 0

    def check_flag_set(self, name):
        return self.flags.issuperset([name])

    def get_command_dir(self):
        if not self.command:
            return None
        return self.MOLD_ROOT + '/' + self.command

    def get_command_dirlist(self):
        result = [] 
        command_dir  = self.get_command_dir()
        if command_dir == None:
            return result
        for current in fs.listdir(command_dir):
            if current != '.mold':
                result.append(current)
        return result

    def get_option(self, index):
        return query(self.options, index)
