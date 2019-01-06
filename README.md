# DOT
![breakfast grool](https://assets.slugbyte.com/github/github-header-00011.png)  

## Install
# TODO: publish to pipy
* To install run `pip3 install `dotdotdot`
* Then run `dot --install` to setup your configuration directory

## Usage 
* get help with append `help`, `--help`, or `-h` to your command of interes
* `dot help`, `dot -h`, and `dot --help` will print the general docs
* subcommands also have specialized docs 
    * `dot temp --help` and `dot temp load --help`

## Development 
* Requires [pipenv](https://github.com/pypa/pipenv)
* Clone code `git clone https://github.com/slugbyte/dot.git`
* Inside the repo run `pipenv shell` to start the virutal env 
* Then run `source scripts/dev.sh`
  * this will create an alias calld `dot` that runs `python3 -m dot`
  * the dot allias will be bound to an `_dot` bash completion function 
  * edit the code in dot/ and run `dot [OPTIONS] [FILENAME]` as you will 
* TODO: write integration tests
