import mold.core as core
import mold.ensure as ensure

_core_comands = ['conf', 'temp', 'drop', 'plug', 'pack', 'exec', 'push', 'pull', 'stat', 'help']
_sync_comands = ['push', 'pull', 'link']
_main_comands = ['stat']

def _main_complete():
   print('temp drop conf plug pack exec sync stat help')

def complete(args):
    if  ensure.check() != ensure.OK:
        return 
    if len(args) < 4:
        return _main_complete()
    for cmd in _core_comands:
        if args[3] == cmd:
            return core.complete(args[4:], cmd)
    return _main_complete()
