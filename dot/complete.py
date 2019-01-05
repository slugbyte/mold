import core

_commands = ['conf', 'temp', 'drop', 'plug', 'pack', 'exec', 'push', 'pull', 'stat', 'help']

def _main_complete():
   print('temp drop plug pack exec push pull stat help')

def complete(args):
    if len(args) < 4:
        return _main_complete()
    for cmd in _commands:
        if args[3] == cmd:
            return core.complete(args[4:], cmd)
    return _main_complete()
