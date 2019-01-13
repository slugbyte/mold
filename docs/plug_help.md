text = '''
USAGE: mold plug [task] [file] 

mold plugs are shell scripts that will be loaded each time 
you create a new shell. Its great place to add ENV var 
config, aliases, functions, or startup scripts. 

NOTE: Anything you load as a plug will be sourced by your shell 
on load, so be carful to only load files your shell can source. 

TASKS:
    list: -- will color_print a list all of your plug files. 

    make: -- will create a new plug file and open it in your 
            text editor.

    load: -- will a file into your config repository as a plug.

    edit: -- will open an existing plug with your text editor.

    nuke: -- will remove an plug file from your config repository. 

e.g. 
    CREATE PLUGS:   mold plug make my-aliases.sh 
                    mold plug make git-shortcuts.sh         
                    mold plug load ./git-aware-prompt.sh
'''.strip()

