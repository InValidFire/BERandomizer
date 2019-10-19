import os, json, random, subprocess
from modules.debug import debug
from modules import dirs
loadlist = {
    'minecraft:recipe_shaped': 'result',
    'minecraft:recipe_shapeless': 'result',
    'minecraft:recipe_furnace': 'output',
    'minecraft:recipe_brewing_mix': 'output',
    'minecraft:recipe_brewing_container': 'reagent'
}

outcomes = []
scrambles = []
def loaddata(data,store,path):
    datakeys = data.keys()
    for key in loadlist:
        if(key in datakeys):
            id = data[key]['description']['identifier']
            outcome = data[key][loadlist[key]]
            dirs.makedir(dirs.tempDir+"\\"+dirs.datasetFolder) #make temp folder
            if(isinstance(outcome,list)): #if output is list of dicts
                items = [] #create list of items
                for item in outcome: #add each item to list
                    items.append(item['item'])
                store.append(items)
                items = ",".join(items) #turn items into string
                document(id,str(items),path)
            elif(isinstance(outcome,dict)): #if output is one dict
                store.append(outcome) #store the item
                document(id,outcome['item'],path)
            elif(isinstance(outcome,str)):
                store.append(outcome)
                document(id,outcome,path)
        debug(str(len(outcomes))+"/"+str(dirs.countDir(dirs.dataDir+"\\"+dirs.datasetFolder+"\\recipes"))+" outcomes loaded.")

def document(recipe,result,path): #used to create recipe documentation 
    message = recipe+" = "+result+"\n"
    with open(path,"a+") as file:
        file.write(message)

def scrambledatanew(data,store,path):
    datakeys = data.keys()
    new_outcome = random.choice(outcomes)
    for key in loadlist:
        if(key in datakeys):
            id = data[key]['description']['identifier']
            data[key][loadlist[key]] = new_outcome
            if(isinstance(new_outcome,list)): #if output is list of dicts
                debug(str(id)+" - "+str(new_outcome))
                items = [] #create list of items
                for item in new_outcome: #add each item to list
                    try:
                        items.append(item['item'])
                    except:
                        items.append(item[item.index(item)])
                store.append(items)
                items = ",".join(items) #turn items into string
                document(id,items,path)
            elif(isinstance(new_outcome,dict)): #if output is one dict
                store.append(new_outcome['item'])
                document(id,new_outcome['item'],path)
            elif(isinstance(new_outcome,str)): #if output is string
                store.append(new_outcome)
                document(id,new_outcome,path)
            outcomes.remove(new_outcome)
            debug("Scrambled: "+str(len(scrambles)))
    return data

def load():
    #load data
    print("Loading outcomes from data... ",end="",flush=True)
    for file in os.listdir(dirs.dataDir+dirs.datasetFolder+"\\recipes"):
        with open(dirs.dataDir+dirs.datasetFolder+"\\recipes\\"+file) as json_file:
            data = json.load(json_file)
            loaddata(data,outcomes,dirs.vanilla)
    print("Loaded "+str(len(outcomes))+" outcomes.")

def scramble():
    #scrambles data
    print("Scrambling data... ",end="",flush=True)
    for file in os.listdir(dirs.tempDir+dirs.datasetFolder+"\\recipes"):
        with open(dirs.tempDir+dirs.datasetFolder+"\\recipes\\"+file,"r") as json_file:
            data = json.load(json_file)
        with open(dirs.tempDir+dirs.datasetFolder+"\\recipes\\"+file,"w+") as json_file:
            json.dump(scrambledatanew(data,scrambles,dirs.randomized),json_file,indent=4)
    print("Scrambled "+str(len(scrambles))+" outcomes.")

def recipestart():
    print("Starting recipe randomization")
    load()
    dirs.copydir(dirs.dataDir+dirs.datasetFolder+"\\recipes",dirs.tempDir+dirs.datasetFolder+"\\recipes")
    document("Seed",str(dirs.seed),dirs.randomized)
    scramble()