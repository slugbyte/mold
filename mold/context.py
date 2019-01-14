'''
a MoldContext parses and stores sys.argv and os.environ, it also has several constants and provieds
some convience methods. One context gets created in __main__ and is passed through the entire app.
'''

import mold.fs as fs
from mold.util import query 
from mold.system import which, check_is_tty

_flags = set(['--complete', '--color', '-v', 'help', '-h', '--help', '--quick-install', '--install', '--clone', '--set-remote', '--force', '--version'])

# STORES ARGS AND ENV VARS
class MoldContext:
    def __init__(self, sys_argv, os_environ):
        # parse and strip flags from argv
        mold_argv = [] # argv witout flags or path to file being executed
        flags = set([]) 
        for arg in sys_argv:
            if _flags.issuperset([arg]):
                flags.add(arg)
            else:
                mold_argv.append(arg)

        # PARGS ARGV AND COMPLETE ARGV
        self.sys_argv  = sys_argv
        # mold_argv is offset by one when the completion is set
        if flags.issuperset(['--complete']):
            self.mold_argv = mold_argv[1:]
        else: 
            self.mold_argv = mold_argv
        self.command = query(self.mold_argv, 1)
        self.task = query(self.mold_argv, 2)
        self.options = self.mold_argv[3:]
        self.flags = flags

        # PARSED ENVIRON AND CONSTANTS
        self.HOME = query(os_environ, 'HOME')
        self.EDITOR = query(os_environ, 'EDITOR') or which('atom') or which('vim') or which('nano')
        self.MOLD_ROOT = query(os_environ, 'MOLD_ROOT') or (HOME +'/.mold')
        self.MOLD_DOCS = __file__.replace('context.py', 'docs')
        self.MOLD_DEBUG = bool(query(os_environ, 'MOLD_DEBUG'))
        self.MOLD_COLOR = check_is_tty() or bool(query(os_environ, 'MOLD_COLOR'))
        self.OK = 0
        self.FAIL = 1
        self.IO_ERROR = 2
        self.MOLD_ROOT_ERROR = 3
        self.MOLD_ROOT_DIRS_ERROR = 4
        self.DEV_TODO = 99

    def check_has_options(self): 
        return len(self.options) != 0

    def check_flag_set(self, name):
        return self.flags.issuperset([name])

    def check_color_mode_set(self):
        return self.MOLD_COLOR or self.check_flag_set('--color')

    def check_verbose_set(self):
        return self.check_flag_set('-v')

    def check_help_set(self):
        return self.check_flag_set('help') or self.check_flag_set('-h') or self.check_flag_set('--help')

    def check_set_remote_set(self):
        return self.check_flag_set('--set-remote')

    def check_clone_set(self):
        return self.check_flag_set('--clone')

    def check_install_set(self):
        return self.check_flag_set('--install') or self.check_flag_set('--quick-install')

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
