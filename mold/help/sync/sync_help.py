text = '''
USAGE: mold sync [task] [arg] 
    mold sync is a wrapper for a few git commands. For all of the sync tasks
    the arg is optional.

WARNING:
    Tasks this start with -- are slightly dangerous, they have the potentail
    to remove data in a way that can not be undone. Use them with caution.

TASKS:
    NO ARGS:
    add: -- will run 'git add -A'

    log: -- will run 'git log'

    status: -- will run 'git status'

    pull: -- will run 'git pull origin HEAD' witch will pull from what 
            ever branch you have checked out.

    push: -- will run 'git push origin HEAD' witch will push to the 
            current branch'

    branch: -- will run 'git branch -avv' and list the current branches.

    WITH ARGS:
    diff: [arg] -- will run 'git diff [arg]', and the arg is optional.

    commit: [message] -- will run git commit with an optional message. 
                     no message is provided git will open your text 
                     editor and you can compose a commit message there. 

    DANGER:
    --force-push: -- DANGER: this will run 'git push origin HEAD ---force'
                    it will overwrite your remote with the current HEAD.

    --hard-reset: [arg] -- DANGER: this will run 'git reset --hard [arg]'
                          this will roll you branch back. If you dont 
                          provide an arg it will default to HEAD.
    --new-branch: [name] -- 
    --delete-branch: [name] -- 
    --checkout: [name] --


    auto: [message] -- command with pull, add -A, commit [message], 
            push.  If a message is provided it will be used as the commit 
            message. If no message is provied git will open your text 
            editor and you can compose a commit message there. This will 
            likely be the most useful command.

e.g. 
    Pull Add Commit Push:   mold sync auto
'''.strip()
