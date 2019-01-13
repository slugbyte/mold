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
To load a your ~/.bashrc into *$MOLD_ROOT/conf* run    
`mold conf load ~/.bashrc`    

To edit the .bashrc you have allready loaded run   
`mold conf load .bashrc`  

To import a conf from a URL into *MOLD_ROOT/conf* and rename it .tmux.conf  run     
`mold load load http://www.example.com/tmux-config .tmux.conf`  

## TASKS  
* **list** -- will print a list all of your conf files.  

* **make** -- will first create a new conf file and link it to your *$HOME* directory then open it in using  *$EDITOR*.  

* **load** -- will copy a file into *$MOLD_ROOT/conf* and then link it to your *$HOME* directory. When loading a conf you can provide second argument to rename the conf.  

* **edit** -- will open an existing conf with your using *$EDITOR*.  

* **nuke** -- will delete a conf file from your *$MOLD_ROOT*, but it will NOT remove it from your *$HOME* directory.  
