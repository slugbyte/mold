'''
complete defines the routing routing logic for arguments to  mold --complete. 
'''

import mold.env as env 
import mold.core as core
import mold.ensure as ensure

# PRIVATE 
_core_comands = ['conf', 'drop', 'plug', 'exec', 'stat', 'help', 'fold']
_sync_comands = ['push', 'pull', 'link']
_main_comands = ['stat', '--install', '--clone']

def _main_complete():
   print('fold drop conf plug exec sync stat help')

# INTERFACE
def complete():
    if  ensure.check() != ensure.OK:
        return 
    if len(env.ARGV) < 4:
        return _main_complete()
    for cmd in _core_comands:
        if env.ARGV[3] == cmd:
            return core.complete(cmd, env.ARGV[4:])
    return _main_complete()
