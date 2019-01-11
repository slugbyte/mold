# MOLD  
![breakfast grool](https://assets.slugbyte.com/github/github-header-00011.png)  

## FEATURES

` USAGE: mold [--flags] [command] [task] [options]`  

### ENV
* `MOLD_ROOT` -- sets the directory that mold will use to install and manage everything DONE
* `MOLD_DEBUG` -- allow errors to be thrown without being cought DONE
* `MOLD_COLOR` -- force mold to print color even when piped into other programs

### COMMANDS
* `help` -- genearl help
* `conf` -- manage dotfiles (CRUD + link to $HOME)
* `plug` -- manage bash scripts aka. plugins (CRUD + load on new shell)
* `exec` -- manage executable files (CRUD + add them in a dir on $PATH)
* `drop` -- manage file templates (CRUD + export to anywhere you want to use them)
* `fold` -- manage project scaffolds (CRUD + export to anywhere you want to use them)
* `sync` -- mangae the MOLD\_ROOT git repository

#### CORE -- MOLD\_ROOT file management 
The core commands are `conf`, `plug`, `exec`, `drop`, and `fold`. 

##### CORE TASKS
These tasks are applied to commands, and have suddly different behaviors based on the 
commands. e.g. if `mold conf make` will crate a file and then link it to $HOME, or 
`mold fold load` will load only directory instead of a file.
* `help` -- general help, command help, task help 
* `make` -- create a new file or dir DONE
* `load` -- import a file or dir DONE
* `list` -- list the files or dirs DONE
* `edit` -- edit files or dirs DONE
* `nuke` -- Delete files or dirs DONE
* `dump` -- (only for `fold` and `drop`) Export content into the current directory DONE

#### SYNC -- MOLD\_ROOT git management
##### SYNC TASKS
* `auto` -- pull add commit push (commit message from argv or text editor) DONE
* git wrappers for mold root
    * `log` DONE
    * `add -A` DONE
    * `commit` DONE
    * `pull` DONE
    * `push` DONE 
    * `diff` DONE 
    * `status` DONE 
    * `branch` DONE 
    * `--soft-reset` DONE 
    * `--hard-reset` DONE 
    * `--new-branch` DONE 
    * `--checkout` DONE 
    * `--force-push` DONE 
    * `--merge` DONE 
    
#### OTHER -- arbitrary tasks
* `--install` -- interactive installer DONE
   * `--remote-uri` automatically set the git remote origin with out prompting the user
* `--clone` -- create mold root from existing repo
* `--set-remote` -- set mold root's git origin remote
* `-v | --verbose` -- make logging more verbose 
* `--verson ` -- print mold version
* `--color | MOLD_COLOR=true` -- force color when piping


## NON-GOALS 
* Adding support for os or hostname specic detection
    * My [old mold like tools](https://github.com/slugbyte/mold/wiki/mold-prequels-and-their-lessons) had this feature, and I felt it over complicated the maintnece of my system configuration. 
    * Instead plugs, confs, and execs can implament their own condional logic TODO: add link to my bashrc [example](https://github.com/slugbyte/config/blob/master/config/.bashrc)
* Having the base install add premade configurration files
    * I don't follow the belief that systyem configurations can't be shared, because systems like [oh-my-zsh](https://ohmyz.sh/) work great for many people. However, molds goal is to help myself and others maintain their **personal** system configurations.
    * There is an option to Install from an existing mold_root on github, and I plan to make a *lite* oh-my-zsh like starter-kit mold_root repository at some point.

## IDEAS?
* (drop, plug, conf, exec) load -- suport for urls 
* fold load -- suport for github repositorys ? -> submodule support? 
* Build a start mold_root for beginners to using a shell (a oh-my-zsh/bash lite)
