import drop

def _main_complete():
   print('temp drop plug pack exec push pull stat help')

def complete(args):
    if len(args) < 4:
        return _main_complete()
    if args[3] == 'drop':
        return drop.complete(args[4:])
        return print('hey cool drop')
    return _main_complete()
    print(len(args), ','.join(args))
