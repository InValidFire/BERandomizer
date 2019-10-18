import os, shutil, json, uuid
from modules.debug import debug
home = os.getcwd()
tempFolder = "\\tmp"
tempDir = home+tempFolder
dataFolder = "\\data"
dataDir = home+dataFolder
datasetFolder = "Not loaded"
# below is needed to stop compiler warnings, not needed for code functionality
seed = None
randomized = None
vanilla = None

def setSeed(value):
    global seed
    seed = value

def setdatasetFolder(name):
    global datasetFolder
    global randomized
    global vanilla
    datasetFolder="\\"+name
    debug("updated datasetFolder to "+datasetFolder)
    randomized = tempDir+datasetFolder+"\\randomized.txt"
    vanilla = tempDir+datasetFolder+"\\vanilla.txt"

def copydir(source,dest):
    print("Copying "+source+" to "+dest)
    shutil.copytree(source,dest)

def makedir(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

def deldir(path):
    if(os.path.exists(home+path)):
        shutil.rmtree(home+path)

def copy(source,dest):
    shutil.copy(source,dest)

def countDir(path):
    i = 0
    for item in os.listdir(path):
        i = i+1
    return i

def archive(source,dest):
    shutil.make_archive(dest,"zip",source)

def package():
    print("Copying manifest")
    copy(home+dataFolder+datasetFolder+"\\manifest.json",tempDir+datasetFolder)
    print("Modifying manifest")
    with open(tempDir+datasetFolder+"\\manifest.json","r") as json_file:
        jsondata = json.load(json_file)
        json_file.close()
    with open(tempDir+datasetFolder+"\\manifest.json","w") as json_file:
        jsondata['header']['uuid'] = str(uuid.uuid4())
        jsondata['header']['name'] = "RandomRock - Seed: "+str(seed)
        jsondata['header']['description'] = "Made by @InValidFire"
        jsondata['modules'][0]['uuid'] = str(uuid.uuid4())
        jsondata['modules'][0]['description'] = "Made by @InValidFire"
        json.dump(jsondata,json_file,indent=4)
        json_file.close()
    print("Archiving into .mcpack")
    archive(tempDir+datasetFolder,home+"\\BERandomizer - "+str(seed)+" - "+datasetFolder.replace("\\",""))
    os.rename(home+"\\BERandomizer - "+str(seed)+" - "+datasetFolder.replace("\\","")+".zip",home+"\\BERandomizer - "+str(seed)+" - "+datasetFolder.replace("\\","")+".mcpack")

def cleanup(path):
    print("Cleaning up")
    deldir(path)