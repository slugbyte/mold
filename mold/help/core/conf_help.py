text = '''
USAGE: mold conf [task] [file] 

mold confs are dotfiles. When you create or load a conf it 
will be hard linked to your home directory. Hard links are 
filesystem references to the same file. Editing the file in
your home directory will also edit the file in your config 
repository, and vice versa. 

If you run the nuke task it will only delete the file from 
your config repository. It will NOT remove it from your 
home directory. 

TASKS:
    list: -- will color_print a list all of your conf files. 

    make: -- will create a new conf file and open it in your 
            text editor, when the file will be hard linked 
            to your home directory. 

    load: -- will a file into your config repository as a conf 
            file and then hard link it to your home directory.

    edit: -- will open an existing conf with your text editor.

    nuke: -- will remove an conf file from your config repository, 
            but it will NOT remove it from your $HOME directory.

e.g. 
    LOAD CONFs:     mold conf load ~/.bashrc 
                    mold comf load ~/.nethackrc
'''.strip()
