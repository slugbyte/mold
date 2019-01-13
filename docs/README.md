# mold
> A CLI for managing dotfiles, shell scripts, executables, project scaffolds, and file templates


## USAGE
`$ mold [--flags] [command] [...options]`

## SYNOPSIS
 mold uses a git repository called a mold root to store and track system configuration files. The mold root is configured using the environment variable $MOLD\_ROOT and unless you have a custom install it will be set to $HOME/.mold

<br /><span/>

 mold splits the files it tracks into the following classifications conf, plug, exec, drop, and fold. Each of theses classifications is has different behaviors and gets its own subdirectory in $MOLD\_ROOT for storing content. Below are descriptions of the unique behaviors of each mold classification.

<br /><span/>

[conf](./conf_help.md) files are dotfiles that are hard linked to the $HOME directory.

[plug](./plug_help.md) files are shell scripts that will be sourced each time a new shell is loaded.

[exec]('./exec_help.md) files will be added to a directory on $PATH.  

[drop](./drop_help.md) files are file asset templates that you can want to future projects.   

[fold](./fold_help.md) templates are project directory scaffolds, they are drops but for whole directories.  

<br /><span/>
Each of mold's file classifications has a "command" that and "tasks" that allow you to create, read, update, and destroy classification specific content. The mold commands are the name of the classification. The following example demonstrates using the **conf** command with **make** task to create a .bashrc file   
e.g. `$ mold conf make .bashrc`

<br /><span/>

The mold commands [conf](./conf_help.md), [plug](./plug_help.md), [exec]('./exec_help.md), [drop](./drop_help.md), and [fold](./fold_help.md) each the following tasks for managing content.  

* **make** - will create content  
* **load** - will copy or download content into the $MOLD\_ROOT  
* **edit** - will open content using $EDITOR  
* **nuke** - will remove content  
* **list** - will list the classification's content  

[drop](./drop_help.md) and [fold](./fold_help.md) also have a **dump** task for exorting content into the current directory.

## INSTALL
To install a $MOLD\_ROOT for the first time run  
`$ mold --install` and follow along with the interactive installer.

For custom installations see the mold github repository  
https://github.com/slugbyte/mold

#### SETUP FROM AN EXISTING MOLD\_ROOT REPOSITORY
To install an existing MOLD\_ROOT run   
`$ mold --clone [GIT_URI]`

## CONFIGURATION
#### GIT REMOTE
To change your $MOLD\_ROOT's git remote origin run   
<span/>`$ mold --set-remote [GIT_URI]`

#### TEXT EDITOR
To change the text editor mold uses for editing file and git commits set the $EDITOR in your shell configuration.  
e.g. `export EDITOR = /usr/local/bin/vim`

## FLAGS
mold flags are boolean values that can turn on and off different behaviors. The order flags are passed into mold does not matter.

* **-v** will create verbose output
* **--color** will force color output even with piped output  
* **-h**, **--help**, and **help** will print help 

## HELP
To find information about a mold comand or task just add **help**, **--help**, or **-h** anywhere and a help dialog will be printed.   
`mold help`, `mold --help`, and `mold -h` are identical.

Because help is treated as a flag the order of the help arguments do not matter.  
`mold help conf make` and `mold conf make --help` are identical.

## MOLD COMMANDS
* [help](./README.md) -- show this help  
* [sync](./sync_help.md) -- manage MOLD\_ROOT's git
* [fold](./fold_help.md) -- manage project scaffolding templates
* [drop](./drop_help.md) -- manage file asset templates
* [plug](./plug_help.md) -- manage shell script plugins
* [conf](./conf_help.md) -- manage configuration files
* [exec](./exec_help.md) -- manage executables

<3 Bug reports are much appreciated https://github.com/slugbyte/mold/issues
