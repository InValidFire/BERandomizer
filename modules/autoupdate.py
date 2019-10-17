from urllib.request import urlopen

def updateCheck():
    link = "https://raw.githubusercontent.com/InValidFire/BERandomizer/update/version.txt"
    f = urlopen(link)
    version = f.read()
    print(version)