# MOLD  
> A CLI for managing dotfiles, shell scripts, executables, project scaffolds, and file templates  

![breakfast grool](https://assets.slugbyte.com/github/github-header-00011.png)  

## About mold
`mold` is is a cli for helping programmers mold thier shell environment to be more fun and productive to write
code in. Its goal is to enable users to bring all of the tools, scripts, and templates that make their programing 
environment feel like home and take them anywhere. Mold has a consistant interface for doing [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) oprations to the content it tracks, and a small but effective set of git helper tasks for syncing configurations.  

Mold is not a really meant to be shell plugin manager, instead it aims to help users write and mangange their own configuration files and scripts. However, mold also believes that [dotfiles are ment to be forked](https://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/) and supports cloning mold-roots, tracking a git remote upstream, as well as dowloading content from urls. Mold can even be used along side acutal shell plugin managers like
[antigen](https://github.com/zsh-users/antigen) or [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh), without any hastel. 

Mold has a few opinionated limitations that aim to help programmers be more productive, by spending less time 
configuring their enviroment and more time working on their projects. It does this by narrowing down system-configuration
into five content classifcations which each have slightly different behaviors. Mold stores its content in a git repoistory 
called a mold-root, and uses the environment variable $MOLD\_ROOT to determine it's location. Mold content is split into the  classifications below, that each have their own directory in the the mold-root. 

##### conf 
Mold confs are dotfiles. Each time a mold conf is loaded or created it is automaticly hard linked to the $HOME directory.
By using hard links no matter where you edit the file, changes are tracked by the mold-roots git. All of the mold conf files are stored in $MOLD\_ROOT/conf .  

##### plug 
Mold plugs are single-file shell scripts that act as shell plugins. Each time a shell is created it will loop though the mold-root plug directory and source each plug. All of the mold plug files are stored in $MOLD\_ROOT/plug.   

#### exec
Mold execs are single-file executable scripts. Each time an exec is loaded or created it will be automaticly be given executable persions. All of the mold exec files are stored in $MOLD\_ROOT/exec, which is added to the begging of $PATH .

#### fold
Mold folds are directory scaffold templates. Folds can be used to setup project boiler plate code so that the overhead of getting to work on a new project will be cut down. Mold folds can be expored from the the mold-root into the current working directory. All of the mold folds are stored in $MOLD\_ROOT/fold .

#### leaf 
Mold leafs are file tempaltes. Leafs can be used to store things like licenses, markdown-templates, .gitignores, and anything you find your self adding to projects regularly. Mold leafs can be expored from the mold-root into the current working directory. all of the mold leafs
are store in $MOLD\_ROOT/leaf. 

## Warning Unstable
Mold is under active development and not ready for production use.

### Install
First you need to install the mold CLI and then use the mold cli to create a mold-root. A mold-root is 
a git repository that mold uses for storing all of your system configuration, shell scripts, and templates.
By default the installers will install your mold-root to **~/.mold**. mold uses the environment vairable 
$MOLD\_ROOT to determine where your mold-root has been installed.

## Features
* A consistant CRUD interface for content management 
* A small but effective interface for managing the mold-root's git repository
    * Including tasks for managing origin and upstream remotes
* Ability to download add content from a URL
* A color coded help logger
* Bash and Zsh tab completion

## TODO: Install Mold
### Download the CLI
### Setup a Mold-Root
##### Mold-Root Interative Installer
##### Mold-Root Quick Install
##### Cloning a Mold-Root 

## USING MOLD
`USAGE: mold  (command) (task) [...options] [--flags]`  
Mold's arguments are broken down in to the four categorys commands, tasks, options, and flags.
mold allways requires a command, and with the exception of `--version` all commands require a task.
Tasks very in the number of options they require and flags they support. Flags are allways 
boolean truthy values, and can be written in mold's arguments in any order (begining, middle, end).  

Mold commands and their uses.
* `--verson ` -- Print mold's version 
* `root` -- Setup and manage the mold-root directory (install, clone, ect.)
* `conf` -- Manage dotfiles (CRUD + hard link to $HOME)
* `plug` -- Manage single-file shell scripts (CRUD + sorced by new shells)
* `exec` -- Manage executable files (CRUD + add them to a directory on $PATH)
* `leaf` -- Manage file templates (CRUD + export to anywhere you need to use them)
* `fold` -- Manage project directory scaffolds (CRUD + export to anywhere you need to use them)
* `sync` -- Git helper tasks for interacting with the mold-root's git repository

####  GETTING  HELP
Mold treats `-h`, `--help`, and `help` as mold flags that trigger help logs. All of mold's commands and tasks have color coded 
help logs. Also, If a you try to run a mold command or task with out the proper arguments mold will automaticly log a short `Usage:` summary. When reading mold *help* and *usage* logs arguments wraped in parens are `(required)`, and arguments wraped in square brackets are `[optional]`.   

Because mold help flags are truthy boolean flags they can be applied to mold arguments in any order. This means that the following statements have identical behavior.   
`mold conf load help`    
`mold conf load --help`  
`mold conf load -h`  
`mold -h conf load`  
`mold conf help load`  
ect.  

#### Managing Content
Mold's main utility is to manage configuration files. It does this though providing an interface to create, load, edit, destroy, export, and list files in the mold-root. Molds content managing commands are `conf`, `plug`, `exec`, `leaf`, and `fold`. These comands have the following tasks for content managment opperations.  
* `make` -- Create new a new file in the mold-root
* `load` -- Import a file from a path or a URL into the mold-root
* `list` -- List files in the mold-root
* `edit` -- Edit a file in the mold-root
* `drop` -- Delete a file in the mold-root
* `take` -- Export a file from the mold-root into the current directory (take is only supported by `fold` and `leaf`)

##### Important notes
* When the `fold` command applys tasks it will create, list, update, delete, and export directorys instead of 
files.
* When the `conf` command applys the `make` or `load` tasks it will automaticly hard-link the new conf
to your $HOME directory, unless you use the `--no-linking` flag (Documented below)
* When the `exec` command applys the `make` or `load` tasks it will automaticly give the new content 
executable permissions [(755)](https://thegeeksalive.com/linux-file-permissions-explained/)

###### Content Managment Examples 
``` bash
# Import an existing .bashrc 
mold conf load ~/.bashrc 

# Create a shell plugin for managing your aliases
mold plug make aliases.sh 

# Edit the aliases.sh plug
mold plug edit aliases.sh 

# Create a leaf by Downloading a url and naming its content node.gitignore 
mold leaf load https://www.gitignore.io/api/vim,osx,node,linux,windows node.gitignore 

# Export the node.gitignore leaf to the current directory and rename it .gitignore
mold leaf take node.gitignore .gitignore

# Delete the aliases.sh plug
mold leaf drop aliases.sh 
```

#### SYNC -- MOLD\_ROOT git management
##### SYNC TASKS
* `auto` -- pull add commit push (commit message from argv or text editor) 
* git wrappers for mold root
    * `log` 
    * `add -A` 
    * `commit` 
    * `pull` 
    * `push`  
    * `diff`  
    * `status`  
    * `branch`  
    * `remote`  
    * `--soft-reset`  
    * `--hard-reset`  
    * `--new-branch`  
    * `--checkout`  
    * `--force-push`  
    * `--merge`  

## ROOT -- MOLD\_ROOT management 
##### ROOT TASKS
* `--install` -- interactive installer 
   * `--set-origin` automatically set the git remote origin with out prompting the user 
* `--quick-install` install without prompting 
* `--clone` -- create mold root from existing repo 
   * `--force` will delete a moldroot without prompting
* `--set-origin` -- set the mold-root's git remote origin 
* `--check` -- check the MOLD\_ROOT directory stucture
* `--fix` -- fix the MOLD\_ROOT directory stucture
    
#### FLAGS -- SUPLAMENTAL BEHAVIORS
* `--color | MOLD_COLOR=true` -- force color when piping 
* `--complete` -- generate smart tab completion for a posix shell like bash or zsh  
* `--no-linking` -- stop a mold command from auto-maticly linking the conf files
* `--help | -h` -- show help

### ENV
* `MOLD_ROOT` -- sets the directory that mold will use to install and manage everything 
* `MOLD_DEBUG` -- allow errors to be thrown without being cought 
* `MOLD_COLOR` -- force mold to print color even when piped into other programs

## NON-GOALS 
* Adding support for multi-file plugs
  * In the past I have spent a lot of time maintaining my own large-ish milti-file shell script projects and have decited that to stop for various reasons. I find the shell shines a automating short tasks and when lots of complexity is involed its more maintable and portable to solve a problem in a programming lanuguage like python, go, rust, c, ruby, ect. 
* Adding support for os or hostname specic detection
    * My [old mold like tools](https://github.com/slugbyte/mold/wiki/mold-prequels-and-their-lessons) had this feature, and I felt it over complicated the maintnece of my system configuration. 
    * Instead plugs, confs, and execs can implament their own condional logic [example](https://github.com/slugbyte/config/blob/master/config/.bashrc) or you can have more than one MOLD\_ROOT repository
    * Instead plugs, confs, and execs can implament their own condional logic [example](https://github.com/slugbyte/config/blob/master/config/.bashrc)
* Having the base install add premade configurration files
    * I don't follow the belief that systyem configurations can't be shared, because systems like [oh-my-zsh](https://ohmyz.sh/) work great for many people. However, molds goal is to help myself and others maintain their **personal** system configurations.
    * There is an option to Install from an existing mold_root on github, and I plan to make a *lite* oh-my-zsh like starter-kit mold_root repository at some point.

## IDEAS?
* create a `name` task to rename content 
* `-v | --verbose` -- make logging more verbose
* create a mold --shell-activate that will return a shell script for loading plugins (could be smart about which shell to use)
* make a tool to publish a new version to PyPi, brew, apt, and the arch-aur 
* write a markdown parser/transformner for tui output so that the help logs can be written in markdown
* (drop, plug, conf, exec) load -- suport for urls 
* fold load -- suport for github repositorys ? -> submodule support? 
* Build a start mold_root for beginners to using a shell (a oh-my-zsh/bash lite)
* Detect [fish](https://github.com/fish-shell/fish-shell) and return a differnt plug loader from --install
* Create a prety Documentation website
  * Maby add a feature for hosing files that people can `mold [command] load URL`
