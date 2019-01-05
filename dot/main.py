import sys
from drop import drop
from complete import complete

def help():
    print('''
USAGE: dot [SUBCOMMAND] [OPTIONS]
    A system configuration and shell workflow tool.

    SUBCOMMANDS: 
        temp    project scaffolding templates (init, make, load, nuke, help)
        drop    file asset templates (<name>, make, load, edit, nuke, help)
        plug    bash pugins (make, edit, nuke)
        pack    system package installers (make, edit, nuke)
        exec    system binarys (load, nuke)
        push    commit dot updates and push
        pull    pull dot updates and install 
        stat    git stat and diff the dot repository
        help    show this help  
    '''.strip())

def main(argv):
    if len(argv) == 1:
        return help()
    sub_command = argv[1]
    options = argv[2:]
    # print('                                DEBUG: sub_command', sub_command)
    # print('                                DEBUG: options', options)
    if(sub_command == 'drop'):
        return drop(options)
    if(sub_command == 'temp'):
        return print('temp')
    if(sub_command == 'plug'):
        return print('plug')
    if(sub_command == 'pack'):
        return print('pack')
    if(sub_command == 'exec'):
        return print('exec')
    if(sub_command == 'push'):
        return print('push')
    if(sub_command == 'pull'):
        return print('pull')
    if(sub_command == 'stat'):
        return print('stat')
    if(sub_command == 'diff'):
        return print('diff')
    if(sub_command == 'complete'):
        return complete(argv)
    # help()

if __name__ == "__main__":
    main(sys.argv)

