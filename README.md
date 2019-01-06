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
    * `mold temp --help` and `mold temp load --help`

## Development 
* Requires [pipenv](https://github.com/pypa/pipenv)
* Clone code `git clone https://github.com/slugbyte/mold.git`
* Inside the repo run `pipenv shell` to start the virutal env 
* Then run `source scripts/dev.sh`
  * this will create an alias calld `mold` that runs `python3 -m mold`
  * the mold allias will be bound to an `\_mold` bash completion function 
  * edit the code in mold/ and run `mold [OPTIONS] [FILENAME]` as you will 
* TODO: write integration tests
