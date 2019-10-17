import json, os, shutil, random, time, subprocess, sys
from modules import dirs, recipes, autoupdate
from modules.debug import debug

#update check
autoupdate.update()

#directory handling
dirs.testdir(dirs.home+"\\data")
subdirs = [o for o in os.listdir(dirs.data) if os.path.isdir(os.path.join(dirs.data,o))]
if(len(subdirs)==0):
    print("No data found in the \\data directory.\nExtract Behavior Pack data in a sub-folder of \\data to continue.")
    print("\nEx. data/DATASETNAME/(data contents)")
    exit()
if(os.path.exists(dirs.data+"\\manifest.json")):
    print("Found a manifest.json in the data\\ directory. Ensure you extracted into a subfolder of data\\, not directly there.")
    print("\nEx. data/DATASETNAME/(data contents)")
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
    dirs.setDataFolder(datas[int(input("Select a number to load dataset: "))])
    subprocess.run("cls",shell=True)
    debug(dirs.dataFolder)
elif(len(subdirs)==1):
    dirs.setDataFolder(subdirs[0])
    debug(dirs.dataFolder)

#welcome screen
print("-----BERandomizer-----")
print("Made by @InValidFire")
print("Version: "+autoupdate.currentString)
print("Automatic Updates: "+str(autoupdate.updateVar))
print("Successfully loaded "+str(len(subdirs))+" datasets.")
print("Selected dataset: "+dirs.dataFolder)
print("Found "+str(dirs.countDir(dirs.data+"\\"+dirs.dataFolder+"\\recipes"))+" recipes")

#seed randomizing
seed = input("Enter seed to generate (leave blank for random seed): ")
if(len(seed)<=0): #if seed is blank, use system time.
    seed = int(time.time())
dirs.setSeed(seed)
random.seed(seed)

#starts recipe randomizing -> modules.recipes
recipes.recipestart()

#pack it up! Call UPS!
dirs.package()
dirs.cleanup("\\newdata")
print("Completed using seed: "+dirs.seed)
