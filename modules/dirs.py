import os, shutil, json, uuid, random
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
    '''Sets the seed used to randomize'''
    global seed
    seed = str(value)
    random.seed(seed) #oops

def setdatasetFolder(name):
    '''Set the dataset folder to use'''
    global datasetFolder
    global randomized
    global vanilla
    datasetFolder="\\"+name
    debug("updated datasetFolder to "+datasetFolder)
    randomized = tempDir+datasetFolder+"\\randomized.txt"
    vanilla = tempDir+datasetFolder+"\\vanilla.txt"

def copydir(source,dest):
    '''Copy directory'''
    print("Copying "+source+" to "+dest)
    shutil.copytree(source,dest)

def makedir(path):
    '''Make a directory'''
    if(not os.path.exists(path)):
        os.makedirs(path)

def deldir(path):
    '''Delete a directory'''
    if(os.path.exists(home+path)):
        shutil.rmtree(home+path)

def copy(source,dest):
    '''Copy a file'''
    shutil.copy(source,dest)

def countDir(path):
    '''Count items in directory'''
    i = 0
    for item in os.listdir(path):
        i = i+1
    return i

def archive(source,dest):
    '''Archive directory'''
    shutil.make_archive(dest,"zip",source)

def package():
    '''Package into .mcpack'''
    print("Copying manifest")
    copy(home+dataFolder+datasetFolder+"\\manifest.json",tempDir+datasetFolder)
    print("Modifying manifest")
    with open(tempDir+datasetFolder+"\\manifest.json","r") as json_file:
        jsondata = json.load(json_file)
        json_file.close()
    with open(tempDir+datasetFolder+"\\manifest.json","w") as json_file:
        jsondata['header']['uuid'] = str(uuid.uuid4())
        jsondata['header']['name'] = "BERandomizer - Seed: "+str(seed)
        jsondata['header']['description'] = "Made by @InValidFire"
        jsondata['modules'][0]['uuid'] = str(uuid.uuid4())
        jsondata['modules'][0]['description'] = "Made by @InValidFire"
        jsondata['dependencies'] = []
        json.dump(jsondata,json_file,indent=4)
        json_file.close()
    print("Archiving into .mcpack")
    archive(tempDir+datasetFolder,home+"\\BERandomizer - "+str(seed)+" - "+datasetFolder.replace("\\",""))
    os.rename(home+"\\BERandomizer - "+str(seed)+" - "+datasetFolder.replace("\\","")+".zip",home+"\\BERandomizer - "+str(seed)+" - "+datasetFolder.replace("\\","")+".mcpack")

def cleanup(path):
    print("Cleaning up")
    deldir(path)