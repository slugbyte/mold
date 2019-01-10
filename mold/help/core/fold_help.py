text = '''
USAGE: mold fold [task] [diectorry] [new-name]

mold folds are templates for scaffold dierctorys. You can use 
mold fold load or create a directory, and later when you want 
a copy of that directory you can get a copy back.

TASKS:
    list: -- will color_print a list of the folds you have created.

    make: -- will create a new fold directory and open it in your 
            text editor, so you can desing a new dirrectory 
            template. 

    load: -- will copy an exisiting directory into your config 
            repository as a fold. load allows you to rename the
            directory you are importing.

    edit: -- will open an existing fold with your text editor.

    nuke: -- will remove an fold from your config repository.

    dump: -- will copy a fold from you config repository into
            your current directory. dump allows you to rename
            the exported fold.

e.g. 
    LOAD A FOLD:    mold fold load ./react-boiler
    EXPORT A FOLD:  mold fold dump react-boiler ./peronal-blog
'''.strip()
