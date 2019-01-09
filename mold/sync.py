'''
sync defines the logic for maintaining a MOLD_ROOT using git 
'''

# sync auto 
    # (pull add commit push)
# sync push 
# sync pull 
# sync commit

import mold.git as git 
def auto(message):
    if not git.pull():
        print('UHHHG, unable to pull origin')
        return False
    if not git.add():
        print('DARN, unable to add changes')
        return False
    if not git.commit(message):
        print('FOOY, git commit failed')
        return False
    if not git.push():
        print('GUESS WHUT, FAIL now? ... push to origin')
        return False
    return True

