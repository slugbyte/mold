# MOLD  
![breakfast grool](https://assets.slugbyte.com/github/github-header-00011.png)  

## Install
# TODO: publish to pipy
* To install run `pip3 install `moldmoldmold`
* Then run `mold --install` to setup your configuration directory

## Usage 
* get help with append `help`, `--help`, or `-h` to your command of interes
* `mold help`, `mold -h`, and `mold --help` will print the general docs
* subcommands also have specialized docs 
    * E.g. `mold temp --help` and `mold temp load --help`

# NON-GOALS 
* Adding support for os or hostname specic detection
    * My [old mold like tools](https://github.com/slugbyte/mold/wiki/mold-prequels-and-their-lessons) had this feature, and I felt it over complicated the maintnece of my system configuration. 
    * Instead plugs, confs, and execs can implament their own condional logic TODO: add link to my bashrc[example]()
* Having the base install add premade configurration files
    * I don't follow the belief that systyem configurations can't be shared, because systems like [oh-my-zsh](https://ohmyz.sh/) work great for many people. However, molds goal is to help myself and others maintain their **personal** system configurations.
    * There is an option to Install from an existing mold_root on github, and I plan to make a *lite* oh-my-zsh like starter-kit mold_root repository at some point.

## Development 
* Requires [pipenv](https://github.com/pypa/pipenv)
* Clone code `git clone https://github.com/slugbyte/mold.git`
* Inside the repo run `pipenv shell` to start the virutal env 
* Then run `source scripts/dev.sh`
  * this will create an alias calld `mold` that runs `python3 -m mold`
  * the mold allias will be bound to an `\_mold` bash completion function 
  * edit the code in mold/ and run `mold [OPTIONS] [FILENAME]` as you will 
* TODO: write integration tests

# IDEAS?
* (drop, plug, conf, exec) load -- suport for urls 
* fold load -- suport for github repositorys ? -> submodule support? 
* Build a start mold_root for beginners to using a shell (a oh-my-zsh/bash lite)
