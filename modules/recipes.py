import os, json, random
from modules.debug import debug
from modules import dirs
loadlist = {
    'minecraft:recipe_shaped': 'result',
    'minecraft:recipe_shapeless': 'result',
    'minecraft:recipe_furnace': 'output',
    'minecraft:recipe_brewing_mix': 'output'
}

outcomes = []
def loaddata(key,data,store): #loads keys from JSON data, storing it in a variable
    datakeys = data.keys()
    type = key.split(":") #set the type
    type = type[1]
    if(key in datakeys): #if it finds the key
        id = data[key]['description']['identifier'] #set the id
        output = data[key][loadlist[key]] #set the output
        dirs.testdir(dirs.newdata+"\\"+dirs.dataFolder)
        if(isinstance(output,list)): #if output is list of dicts
            items = [] #create list of items
            for item in output: #add each item to list
                store.append(item) #store the item
                items.append(item['item'])
            items = ",".join(items) #turn items into string
            debug("Added "+str(type)+" with ID "+str(id)+" producing "+items)
            document(id,items,dirs.vanilla)
        elif(isinstance(output,dict)): #if output is one dict
            store.append(output) #store the item
            debug("Added "+str(type)+" with ID "+str(id)+" producing "+str(output['item']))
            document(id,output['item'],dirs.vanilla)
        elif(isinstance(output,str)): #if output is string
            store.append(output) #store the item
            debug("Added "+str(type)+" with ID "+str(id)+" producing "+str(output))
            document(id,output,dirs.vanilla)

def document(recipe,result,path): #used to create recipe documentation 
    message = recipe+" = "+result+"\n"
    with open(path,"a+") as file:
        file.write(message)

def scrambledata(key,data,documentation):
    '''Test'''
    if(len(outcomes)>0):
            datakeys = data.keys()
            new_outcome = random.choice(outcomes)
            if(key in datakeys):
                type = key.split(":") #set the type
                type = type[1]
                id = data[key]['description']['identifier']
                data[key][loadlist[key]] = new_outcome
                #document(data['minecraft:recipe_shaped']['description']['identifier'],data['minecraft:recipe_shaped']['result'])
                if(isinstance(new_outcome,list)): #if output is list of dicts
                    items = [] #create list of items
                    for item in new_outcome: #add each item to list
                        items.append(item['item'])
                    items = ",".join(items) #turn items into string
                    debug("Added "+str(type)+" with ID "+str(id)+" producing "+items)
                    document(id,items,documentation)
                elif(isinstance(new_outcome,dict)): #if output is one dict
                    debug("Added "+str(type)+" with ID "+str(id)+" producing "+str(new_outcome['item']))
                    document(id,new_outcome['item'],documentation)
                elif(isinstance(new_outcome,str)): #if output is string
                    debug("Added "+str(type)+" with ID "+str(id)+" producing "+str(new_outcome))
                    document(id,new_outcome,documentation)
                outcomes.remove(new_outcome)
                return data

def load():
    #load data
    print("Loading outcomes from data")
    for file in os.listdir(dirs.data+"/"+dirs.dataFolder+"/recipes"):
        with open(dirs.data+"/"+dirs.dataFolder+"/recipes/"+file) as json_file:
            data = json.load(json_file)
            loaddata('minecraft:recipe_shaped',data,outcomes)
            loaddata('minecraft:recipe_shapeless',data,outcomes)
            loaddata('minecraft:recipe_furnace',data,outcomes)
            loaddata('minecraft:recipe_brewing_mix',data,outcomes)
    print("Possible outcomes loaded from data")

def scramble():
    #scrambles data
    print("Scrambling data")
    for file in os.listdir(dirs.newdata+"\\"+dirs.dataFolder+"\\recipes"):
        with open(dirs.newdata+"\\"+dirs.dataFolder+"\\recipes\\"+file,"r") as json_file:
            data = json.load(json_file)
        with open(dirs.newdata+"\\"+dirs.dataFolder+"\\recipes\\"+file,"w+") as json_file:
            try:
                json.dump(scrambledata('minecraft:recipe_shaped',data,dirs.randomized),json_file,indent=4)
                json.dump(scrambledata('minecraft:recipe_shapeless',data,dirs.randomized),json_file,indent=4)
                json.dump(scrambledata('minecraft:recipe_furnace',data,dirs.randomized),json_file,indent=4)
                json.dump(scrambledata('minecraft:recipe_brewing_mix',data,dirs.randomized),json_file,indent=4)
            except:
                debug("no action for "+file)
                pass
    print("Finished scrambling data")

def recipestart():
    print("Starting recipe randomizing")
    load()
    dirs.copydir(dirs.data+"\\"+dirs.dataFolder+"\\recipes",dirs.newdata+"\\"+dirs.dataFolder+"\\recipes")
    document("Seed",str(dirs.seed),dirs.randomized)
    scramble()