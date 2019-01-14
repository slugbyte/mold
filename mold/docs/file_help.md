mold file
====

> file is a mold command for managing file templates

## USAGE
`$ mold file task [options] [--flags]`

## SYNOPSIS  
mold files are file templates. You can use mold file to create
or load a file template, and later when you want a copy of
your file back.

## EXAMPLES
Load and rename two licenses as files.  
<span />`$ mold file load ./LICENSE.md mit.md`    
<span />`$ mold file load ./LICENSE.md cc-share-alike.md`    
copy a file into the current directory.   
<span />`$ mold file take mit.md ./LICENSE.md`   

## TASKS
* [list](file_list_help.md) -- will print a list of your files
* [make](file_make_help.md) -- will create a file using $EDITOR
* [load](file_load_help.md) -- will copy an a file into $MOLD_ROOT
* [edit](file_edit_help.md) -- will edit a file with $EDITOR
* [nuke](file_nuke_help.md) -- will delete a file
* [take](file_take_help.md) -- copy a file into your current directory
