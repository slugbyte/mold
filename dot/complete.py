import core

def _main_complete():
   print('temp drop plug pack exec push pull stat help')

def complete(args):
    if len(args) < 4:
        return _main_complete()
    if args[3] == 'drop':
        return core.complete(args[4:], 'drop')
    if args[3] == 'plug':
        return core.complete(args[4:], 'plug')
    return _main_complete()
