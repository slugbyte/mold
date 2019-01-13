mold conf  
====

> conf is a mold command for managing dotfiles  

## USAGE  
`mold conf [task] [filepath] [rename]`  

## SYNOPSIS  
A mold conf is a dotfile. When you create or load a conf it
will be hard linked to your home directory. Hard links are
filesystem references to the same file. Editing the file in
your home directory will also edit the file in your config
repository, and vice versa.  

## NOTE  
If you run the nuke task it will only delete the file from
your config repository. It will NOT remove it from your
home directory.  

## EXAMPLES  
To load a your ~/.bashrc into *$MOLD_ROOT/conf*  
<span/>`$ mold conf load ~/.bashrc`    

To edit the .bashrc you have allready loaded  
<span/>`$ mold conf load .bashrc`  

To download a conf into *MOLD_ROOT/conf* and rename it .tmux.conf  
<span/>`$ mold load load http://www.iexample.com/tmux-config .tmux.conf`  

## TASK REFERENCE
* **list** -- will print a list all of your conf files.  

* **make** -- will create a new conf file.

* **load** -- will copy a file into *$MOLD_ROOT/conf*.

* **edit** -- will open a conf file using *$EDITOR*.  

* **nuke** -- will delete a conf file.
