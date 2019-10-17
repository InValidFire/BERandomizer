from urllib.request import urlopen
currentString = ""
branchString = ""
updateVar = True
def updateToggle(mode=bool):
    global updateVar
    updateVar = mode

def updateCheck():
    if(updateVar==True):
        global currentString
        global branchString
        link = "https://raw.githubusercontent.com/InValidFire/BERandomizer/update/version.txt"
        try:
            with open("version.txt") as file:
                currentVersion = file.read().split('.')
                currentMajor = int(currentVersion[0])
                currentMinor = int(currentVersion[1])
                currentPatch = int(currentVersion[2])
                currentString = ".".join([str(currentMajor),str(currentMinor),str(currentPatch)])
        except:
            return(True)
        with urlopen(link) as branch:
            branchVersion = branch.read().decode('utf-8').split('.')
            branchMajor = int(branchVersion[0])
            branchMinor = int(branchVersion[1])
            branchPatch = int(branchVersion[2])
            branchString = ".".join([str(branchMajor),str(branchMinor),str(branchPatch)])

        #needs to catch if currentVersion is greater than branchVersion, and disable auto updating (for devs)
        if(branchMajor<=currentMajor and branchMinor<=currentMinor and branchPatch<=currentPatch):
            return(False)
        else:
            return(True)