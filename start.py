import json, os, shutil, random, uuid, time
from modules import dirs
from modules import recipes
from modules.debug import debug

#directory handling
subdirs = [o for o in os.listdir(dirs.data) if os.path.isdir(os.path.join(dirs.data,o))]
debug("Subdirs: "+str(subdirs))
datas = {}
if (len(subdirs)>1):
    i = 1
    for data in subdirs:
        datas[i] = data
        i = i+1
    print("Multiple data directories found:\n")
    for data in datas:
        print(str(data)+" - "+str(datas[data]))
    debug("Keys: "+str(datas.keys()))
    dirs.setDataFolder(datas[int(input("Enter the folder's number to load data: "))])
    debug(dirs.dataFolder)
elif(len(subdirs)==1):
    dirs.setDataFolder(subdirs[0])
    debug(dirs.dataFolder)

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
