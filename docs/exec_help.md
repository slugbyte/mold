text = '''
USAGE: mold exec [task] [file] 

mold execs are executbale files that will be stored in
a directory on your $PATH. 

NOTE: If your file does not have executable permsions 
you will not be able to run it. so remember to chmod 775 it
if you need to.

TASKS:
    list: -- will color_print a list all of your exec files. 

    make: -- will create a new exec file and open it in your 
            text editor. It will automaticly have executable 
            permissions (755).

    load: -- will a file into your config repository as a exec.
            You can rename execs that you are loading

    edit: -- will open an existing exec with your text editor.

    nuke: -- will remove an exec file from your config repository. 

e.g. 
    CREATE EXECS:   mold exec make troll.py
    LOAD EXECS:     mold load ./a.out fetch-metadata
'''.strip()
