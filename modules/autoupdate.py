from urllib.request import urlopen

def updateCheck():
    link = "https://raw.githubusercontent.com/InValidFire/BERandomizer/update/version.txt"
    #f = urlopen(link)
    #branchVersion = f.read().decode('utf-8')
    with urlopen(link) as f:
        branchVersion = f.read().decode('utf-8').split('.')
        branchMajor = int(branchVersion[0])
        branchMinor = int(branchVersion[1])
        branchPatch = int(branchVersion[2])
    try:
        with open("version.txt") as file:
            currentVersion = file.read().split('.')
            currentMajor = int(currentVersion[0])
            currentMinor = int(currentVersion[1])
            currentPatch = int(currentVersion[2])
    except: #if it can't find the file
        return(True)

    if(branchMajor==currentMajor and branchMinor==currentMinor and branchPatch==currentPatch):
        return(False)
    else:
        return(True)