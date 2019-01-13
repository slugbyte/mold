text = '''
USAGE: mold drop [task] [file] [new-name]

mold drops are file templates. You can use mold drop to create 
or load a file template, and later when you want a copy of 
your drop back.

TASKS:
    list: -- will color_print a list of the drop you have created.

    make: -- will create a new drop file and open it in your 
            text editor, so you can desing a file template. 

    load: -- will a file intor into your config repository 
            as a drop . load allows you to rename the drop
            you are importing.

    edit: -- will open an existing drop with your text editor.

    nuke: -- will remove an drop  from your config repository.

    dump: -- will copy a drop from you config repository into
            your current directory. dump allows you to rename
            the exported drop.

e.g. 
    LOAD DROPS:     mold drop load ./LICENSE.md mit.md 
                    mold drop load ./LICENSE.md cc-share-alike.md 
    EXPORT A DROP:  mold drop dump mit.md ./LICENSE.md 
'''.strip()

