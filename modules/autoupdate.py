from urllib.request import urlopen
import subprocess, sys, os
currentString = "Non-Git"
branchString = "Non-Git"
updateVar = True
def updateToggle(mode=bool):
    global updateVar
    updateVar = mode

def updateGit():
    if(updateVar==True):
        global currentString
        global branchString
        per = '%'
        subprocess.run('git fetch',shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        branchCommit = subprocess.check_output('git log -n 1 --date=raw-local --pretty=format:"'+per+'h '+per+'ad" origin/master',shell=True)
        localCommit = subprocess.check_output('git log -n 1 --date=raw-local --pretty=format:"'+per+'h '+per+'ad"',shell=True)
        branchCommit = branchCommit.split()
        localCommit = localCommit.split()
        branchString = branchCommit[0].decode('utf-8')
        currentString = localCommit[0].decode('utf-8')
        if(int(branchCommit[1])>int(localCommit[1])):
            return(True)
        else:
            return(False)

def update():
    if(os.path.exists('.git')==True):
        print("Checking for updates...", end="",flush=True)
        if(updateGit()==True):
            print("\tUpdate found")
            update = input("Would you like to install?")
            if('y' in update.lower()):
                subprocess.run(['python','update.py'],shell=True)
                sys.exit()
            if('n' in update.lower()):
                pass
        else:
            print("\tNo updates available")
    else:
        updateToggle(False)
        print("Automatic updates disabled, was not downloaded via 'git clone'.")