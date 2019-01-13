# mold
> A CLI for managing dotfiles, shell scripts, executables, project scaffolds, and file templates


## USAGE
`mold [--flags] [command] [...options]`

## SYNOPSIS:
 mold uses a git repository called a mold root to store and track system configuration files. The mold root is configured using the environment variable $MOLD_ROOT and unless you have a custom install it will be set to $HOME/.mold

 mold splits the files it tracks into the following classifications conf, plug, exec, drop, and fold. Each of theses classifications is has different behaviors and gets its own subdirectory in $MOLD_ROOT for storing content. Below are descriptions of the unique behaviors of each mold classification.

[conf](./conf_help.md) files are dotfiles that are hard linked to the $HOME directory.

[plug](./plug_help.md) files are shell scripts that will be sourced each time a new shell is loaded.

[exec]('./exec_help.md) files will be added to a directory on $PATH.  

[drop](./drop_help.md) files are file asset templates that you can want to future projects.   

[fold](./fold_help.md) templates are project directory scaffolds, they are drops but for whole directories.  

Each of mold's file classifications has a "command" that and "tasks" that allow you to create, read, update, and destroy classification specific content. The mold commands are the name of the classification. The following example demonstrates using the **conf** command with **make** task to create a .bashrc file `$ mold conf make .bashrc`

## INSTALL:
To install a $MOLD_ROOT for the first time run `$ mold --install` and follow along with the interactive installer.

For custom installations see the mold github repository  
https://github.com/slugbyte/mold

## SETUP FROM AN EXISTING MOLD_ROOT REPOSITORY
To install an existing MOLD_ROOT run `$ mold --clone [GIT_URI]`

## CONFIGURATION
#### GIT REMOTE
To change your $MOLD_ROOT's git remote origin run   
<span/>`$ mold --set-remote [GIT_URI]`

#### TEXT EDITOR
To change the text editor mold uses for editing file and git commits set the $EDITOR in your shell configuration.  
e.g. `export EDITOR = /usr/local/bin/vim`

## HELP
To find information about a mold comand or task just add *help*, *--help*, or *-h* anywhere and a help dialog will be printed. `mold help`, `mold --help`, and `mold -h` all do the same thing.

The order of the help arguments does not matter.  
`mold help conf make` and `mold conf make --help`   
will both print the conf-make help.  

# MOLD COMMANDS
* help -- show this help  
* sync -- manage the MOLD_ROOT git
* fold -- manage project scaffolding templates (+ dump task)
* drop -- manage file asset templates (+ dump task)
* conf -- manage configuration files 
* exec -- manage executables
* plug -- manage shell script plugins

<3 Bug reports are much appreciated https://github.com/slugbyte/mold/issues
