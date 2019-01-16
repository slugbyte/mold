# CONTRIBUTING TO mold
I love and appreciate pull requests from everyone.   
By participating in this project, you agree to abide by the mold 
[code of conduct](./CODE_OF_CONDUCT.md).  

### DOCUMENTAION EDITS
I am extreemly dyslexic and need and love help with grammer and spelling. Feel free to follow the pull 
request guide below with any documentation edits. If your not sure how to change the `__version__` I can 
walk you through it or do it for you! <3  

### BUGS and PATCHES
If you find a bug you can report it using mold's [GitHub Issue Tracker](https://github.com/slugbyte/mold/issues).  

If you create a patch for a bug, THANK YOU!   
Open a pull request following the pull request guide below!   

### NEW FEATURES 
If you want to suggest a new feature open an [Issue](https://github.com/slugbyte/mold/issues) with a perposal and lets discuss it!   

Also, If you are expieramneting with the code on a fork and have questions you are welcome to open an [Issue](https://github.com/slugbyte/mold/issues), and I would be happy to help!  

### OPENING A PULL REQUEST
1) Make sure you have [pipenv](https://github.com/pypa/pipenv) installed.  

2) Fork, then clone the repo  
`git clone git@github.com:your-username/mold.git`   

3) Set up your machine:    
`soruce ./scripts/bootstrap`    
    * activates a virutalenv   
    * installs dependecies  

4) Make your changes   
    * Edit the code or the documentation
    * Add tests, if relevant
    * Update the `mold/__init__.py`'s `__verion__` using [semvar](https://semver.org/) (ask if you have any questions).
    * Use decriptive commit messages  

5) Push to your fork and submit a pull request.  

6) THANKs!!!! At this point you're waiting on me to do a review. I may request you to make some changes and re-review, then Boom PR merged. Your my hero.  

##### NOTE  
Some things that will increase the chance that your pull request is accepted:  
* Write tests.
* Write a good commit message.
* Have a discussion using the [issue tracker](https://github.com/slugbyte/mold/issues) about adding new fetures before opening the PR.
    * If a new feature hasn't been discussed and agreed on the PR may be denied. 
