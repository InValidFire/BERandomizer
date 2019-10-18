import json, os, random, time, subprocess, sys
from modules import dirs, recipes, autoupdate
from modules.debug import debug

#dirsetup - making sure nothing breaks
dirs.cleanup(dirs.tempFolder)
dirs.makedir(dirs.home+dirs.dataFolder)
subdirs = [o for o in os.listdir(dirs.dataDir) if os.path.isdir(os.path.join(dirs.dataDir,o))]

#controls the header
def header():
    subprocess.run("cls",shell=True)
    print("-----BERandomizer-----")
    print("Made by @InValidFire")
    print("Version: "+autoupdate.currentString)
    print("Automatic Updates: "+str(autoupdate.updateVar))
    print("Seed: "+str(dirs.seed))
    print("Successfully loaded "+str(len(subdirs))+" dataset(s)")
    print("Selected dataset: "+str(dirs.datasetFolder.replace("\\","")))
    print("----------------------")

#update check
autoupdate.update()
header()

#directory handling - move to its own file
if(len(subdirs)==0):
    print("No data found in the"+dirs.dataFolder+"directory.\nExtract Behavior Pack data in a sub-folder of "+dirs.dataFolder+" to continue.")
    print("\nEx. "+dirs.dataFolder+"\\DATASETNAME\\(data contents)")
    exit()
if(os.path.exists(dirs.dataDir+"\\manifest.json")):
    print("Found a manifest.json in the "+dirs.dataFolder+" directory. Ensure you extracted into a subfolder of "+dirs.dataFolder+", not directly there.")
    print("\nEx. "+dirs.dataFolder+"\\DATASETNAME\\(data contents)")
    exit()
debug("Subdirs: "+str(subdirs))
datas = {}
if (len(subdirs)>1):
    i = 1
    for data in subdirs:
        datas[i] = data
        i = i+1
    print("Multiple datasets found:")
    for data in datas:
        print("\t"+str(data)+". "+str(datas[data]))
    debug("Keys: "+str(datas.keys()))
    dirs.setdatasetFolder(datas[int(input("Select a number to load dataset: "))])
    subprocess.run("cls",shell=True)
    debug(dirs.datasetFolder)
elif(len(subdirs)==1):
    dirs.setdatasetFolder(subdirs[0])
    debug(dirs.datasetFolder)

#seed initialize
seed = int(time.time())
dirs.setSeed(seed)

#welcome screen
header()
print("'help' to view commands\n")
#command system - move to its own file
while(True):
    command = input("Enter a command to continue: ")
    if(command.lower()=="help"):
        print("Available commands:\n\tseed - change the used seed\n\trandomize - start randomization process\n\texit - close program")
    elif(command.lower()=="seed"):
        seed = input("Enter seed to generate: ")
        if(len(seed)<=0): #if seed is blank, use system time.
            seed = int(time.time())
            dirs.setSeed(seed)
        dirs.setSeed(seed)
        random.seed(seed)
        header()
    elif(command.lower()=="randomize"): #starts recipe randomizing -> modules.recipes
        header()
        print("Found "+str(dirs.countDir(dirs.dataDir+"\\"+dirs.datasetFolder+"\\recipes"))+" recipes")
        print("Randomization Options")
        print("\t1. recipes")
        command = input("Select numbers to randomize: ")
        if("1" in command):
            header()
            recipes.recipestart()
        dirs.package()
        dirs.cleanup(dirs.tempFolder)
        sys.exit()
    elif(command.lower()=="exit"):
        sys.exit()
    else:
        print("Command not found, type 'help' for a list of commands.")

#pack it up! Call UPS!
dirs.package()
dirs.cleanup(tempDir)
print("Completed using seed: "+str(dirs.seed))
