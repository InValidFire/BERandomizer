import os, shutil, json, uuid
from modules.debug import debug
home = os.getcwd()
data = home+"\\data"
newdata = home+"\\newdata"

# below is needed to stop compiler warnings, not needed for code functionality
seed = None
dataFolder = None
randomized = None
vanilla = None

def setSeed(value):
    global seed
    seed = value

def setDataFolder(name):
    global dataFolder
    global randomized
    global vanilla
    dataFolder=name
    debug("updated dataFolder to "+dataFolder)
    randomized = newdata+"\\"+dataFolder+"\\randomized.txt"
    vanilla = newdata+"\\"+dataFolder+"\\vanilla.txt"

def copydir(source,dest):
    print("Copying "+source+" to "+dest)
    shutil.copytree(source,dest)

def testdir(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

def deldir(path):
    shutil.rmtree(home+path)

def copy(source,dest):
    shutil.copy(source,dest)

def archive(source,dest):
    shutil.make_archive(dest,"zip",source)

def package():
    print("Copying manifest")
    copy(home+"\\data\\"+dataFolder+"\\manifest.json",home+"\\newdata\\"+dataFolder)
    print("Modifying manifest")
    with open(home+"\\newdata\\"+dataFolder+"\\manifest.json","r") as json_file:
        jsondata = json.load(json_file)
        json_file.close()
    with open(home+"\\newdata\\"+dataFolder+"\\manifest.json","w") as json_file:
        jsondata['header']['uuid'] = str(uuid.uuid4())
        jsondata['header']['name'] = "RandomRock - Seed: "+str(seed)
        jsondata['header']['description'] = "Made by InValidFire"
        jsondata['modules'][0]['uuid'] = str(uuid.uuid4())
        jsondata['modules'][0]['description'] = "Made by InValidFire"
        json.dump(jsondata,json_file,indent=4)
        json_file.close()
    print("Archiving into .mcpack")
    archive(home+"\\newdata\\"+dataFolder,home+"\\RandomRock - "+str(seed))
    #shutil.make_archive(home+"\\Randomized Recipes - "+str(seed),"zip",home+"\\newdata\\"+dataFolder)
    os.rename(home+"\\RandomRock - "+str(seed)+".zip",home+"\\RandomRock - "+str(seed)+".mcpack")

def cleanup(path):
    print("Cleaning up")
    deldir(path)