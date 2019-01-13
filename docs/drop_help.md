mold drop
====

> drop is a mold command for managing file templates

## USAGE
`$ mold drop task [options] [--flags]`

## SYNOPSIS  
mold drops are file templates. You can use mold drop to create
or load a file template, and later when you want a copy of
your drop back.

## EXAMPLES
Load and rename two licenses as drops.  
<span />`$ mold drop load ./LICENSE.md mit.md`    
<span />`$ mold drop load ./LICENSE.md cc-share-alike.md`    
copy a drop into the current directory.   
<span />`$ mold drop dump mit.md ./LICENSE.md`   

## TASKS
* [list](drop_list_help.md) -- will print a list of your drops
* [make](drop_make_help.md) -- will create a drop using $EDITOR
* [load](drop_load_help.md) -- will copy an a drop into $MOLD_ROOT
* [edit](drop_edit_help.md) -- will edit a drop with $EDITOR
* [nuke](drop_nuke_help.md) -- will delete a drop
* [dump](drop_dump_help.md) -- copy a drop into your current directory
