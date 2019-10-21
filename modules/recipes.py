import os, json, random, subprocess
from modules.debug import debug
from modules import dirs, settings
loadlist = {
    'minecraft:recipe_shaped': 'result',
    'minecraft:recipe_shapeless': 'result',
    'minecraft:recipe_furnace': 'output',
    'minecraft:recipe_brewing_mix': 'output',
    'minecraft:recipe_brewing_container': 'reagent'
}
dataload = {
    'minecraft:dye' : 'dyes',
    'minecraft:carpet' : 'colors',
    'minecraft:wool' : 'colors',
    'minecraft:bucket' : 'bucket',
    'minecraft:log' : 'log',
    'minecraft:log2' : 'log2',
    'minecraft:concrete_powder' : 'colors',
    'minecraft:banner' : 'colors',
    'minecraft:stained_glass' : 'colors',
    'minecraft:stained_glass_pane' : 'colors',
    'minecraft:red_flower' : 'flowers',
    'minecraft:fence' : 'wood',
    'minecraft:planks' : 'wood',
    'minecraft:wood' : 'wood',
    'minecraft:stained_hardened_clay' : 'colors',
    'minecraft:anvil' : 'anvil',
    'minecraft:banner_pattern' : 'banner_pattern',
    'minecraft:stone' : 'stone',
    'minecraft:boat' : 'wood',
    'minecraft:stonebrick' : 'stonebrick',
    'minecraft:cobblestone_wall' : 'wall',
    'minecraft:wooden_slab' : 'wood',
    'minecraft:emptymap' : 'map',
    'minecraft:dirt' : 'dirt',
    'minecraft:sandstone' : 'sandstone',
    'minecraft:red_sandstone' : 'sandstone',
    'minecraft:prismarine' : 'prismarine',
    'minecraft:coal' : 'coal',
    'minecraft:golden_apple' : 'gapple',
    'minecraft:stone_slab' : 'stone_slab',
    'minecraft:stone_slab2' : 'stone_slab2',
    'minecraft:stone_slab3' : 'stone_slab3',
    'minecraft:stone_slab4' : 'stone_slab4',
    'minecraft:double_stone_slab' : 'stone_slab',
    'minecraft:double_stone_slab2' : 'stone_slab2',
    'minecraft:double_stone_slab3' : 'stone_slab3',
    'minecraft:double_stone_slab4' : 'stone_slab4',
    'minecraft:quartz_block' : 'quartz',
    'minecraft:stone_button' : 'ignore',
    'minecraft:dropper' : 'ignore'
}

documentation = {
    'dyes' : {
        0 : 'ink sac',
        1 : 'red',
        2 : 'green',
        3 : 'cocoa beans',
        4 : 'lapis',
        5 : 'purple',
        6 : 'cyan',
        7 : 'light gray',
        8 : 'gray',
        9 : 'pink',
        10 : 'lime',
        11 : 'yellow',
        12 : 'light blue',
        13 : 'magenta',
        14 : 'orange',
        15 : 'bonemeal',
        16 : 'black',
        17 : 'brown',
        18 : 'blue',
        19 : 'white'
    },
    'colors' : {
        0 : 'white',
        1 : 'orange',
        2 : 'magenta',
        3 : 'light blue',
        4 : 'yellow',
        5 : 'lime',
        6 : 'pink',
        7 : 'gray',
        8 : 'light gray',
        9 : 'cyan',
        10 : 'purple',
        11 : 'blue',
        12 : 'brown',
        13 : 'green',
        14 : 'red',
        15 : 'black'
    },
    'bucket' : {
        0 : 'empty',
        1 : 'milk',
        2 : 'cod',
        3 : 'salmon',
        4 : 'tropical',
        5 : 'pufferfish',
        8 : 'water',
        10 : 'lava'
    },
    'log' : {
        0 : 'oak',
        1 : 'spruce',
        2 : 'birch',
        3 : 'jungle'
    },
    'log2' : {
        0 : 'acacia',
        1 : 'dark oak'
    },
    'wood' : {
        0 : 'oak',
        1 : 'spruce',
        2 : 'birch',
        3 : 'jungle',
        4 : 'acacia',
        5 : 'dark oak',
        8 : 'stripped oak',
        9 : 'stripped spruce',
        10 : 'stripped birch',
        11 : 'stripped jungle',
        12 : 'stripped acacia',
        13 : 'stripped dark oak'
    },
    'flowers' : {
        0 : 'poppy',
        1 : 'blue orchid',
        2 : 'allium',
        3 : 'azure bluet',
        4 : 'red tulip',
        5 : 'orange tulip',
        6 : 'white tulip',
        7 : 'pink tulip',
        8 : 'oxeye daisy',
        9 : 'cornflower',
        10 : 'lily of the valley'
    },
    'anvil' : {
        0 : 'undamaged',
        1 : 'slightly damaged',
        2 : 'very damaged'
    },
    'banner_pattern' : {
        0 : 'creeper charge',
        1 : 'skull charge',
        2 : 'flower charge',
        3 : 'thing',
        4 : 'field masoned',
        5 : 'bordure indented'
    },
    'stone' : {
        0 : 'stone',
        1 : 'granite',
        2 : 'polished granite',
        3 : 'diorite',
        4 : 'polished diorite',
        5 : 'andesite',
        6 : 'polished andesite'
    },
    'stonebrick' : {
        0 : 'stone brick',
        1 : 'mossy brick',
        2 : 'cracked brick',
        3 : 'chiseled brick'
    },
    'wall' : {
        0 : 'cobble',
        1 : 'mossycobble',
        2 : 'granite',
        3 : 'diorite',
        4 : 'andesite',
        5 : 'sandstone',
        6 : 'brick',
        7 : 'stonebrick',
        8 : 'mossybrick',
        9 : 'endbrick',
        10 : 'netherbrick',
        11 : 'prismarine',
        12 : 'redsandstone',
        13 : 'rednetherbrick'
    },
    'map' : {
        0 : 'normal',
        2 : 'locator'
    },
    'dirt' : {
        0 : 'dirt',
        1 : 'coarse'
    },
    'coal' : {
        0 : 'coal',
        1 : 'charcoal'
    },
    'prismarine' : {
        0 : 'prismarine',
        1 : 'dark prismarine',
        2 : 'prismarine bricks'
    },
    'sandstone' : {
        0 : 'normal',
        1 : 'chiseled',
        2 : 'cut',
        3 : 'smooth'
    },
    'gapple' : {
        0 : 'normal',
        1 : 'enchanted'
    },
    'stone_slab' : {
        0 : 'smooth',
        1 : 'sandstone',
        2 : 'wooden',
        3 : 'cobblestone',
        4 : 'bricks',
        5 : 'stonebrick',
        6 : 'quartz',
        7 : 'netherbrick'
    },
    'stone_slab2' : {
        0 : 'red_sandstone',
        1 : 'purpur',
        2 : 'prismarine',
        3 : 'prismarine brick',
        4 : 'dark prismarine',
        5 : 'mossy cobble',
        6 : 'smooth sandstone',
        7 : 'red netherbrick',
    },
    'stone_slab3' : {
        0 : 'end brick',
        1 : 'smooth red sandstone',
        2 : 'polished andesite',
        3 : 'andesite',
        4 : 'diorite',
        5 : 'polished_diorite',
        6 : 'granite',
        7 : 'polished granite'
    },
    'stone_slab4' : {
        0 : 'mossy brick',
        1 : 'smooth quartz',
        2 : 'stone',
        3 : 'cut sandstone',
        4 : 'cut red sandstone'
    },
    'ignore' : 'ignore',
    'quartz' : {
        0 : 'normal',
        1 : 'chiseled',
        2 : 'pillar',
        3 : 'smooth',
        5 : 'chiseled',
        6 : 'pillar',
        9 : 'chiseled',
        10 : 'pillar',
        13 : 'chiseled',
        14 : 'pillar'
    }
}

outcomes = []
scrambles = []

def blacklistcheck(blacklist,rtype):
    if(rtype in blacklist):
        return(True)
    else:
        return(False)

def loaddata(data,store,path):
    '''Loads data given to it'''
    datakeys = data.keys()
    for key in loadlist:
        itemData = None
        if(key in datakeys):
            id = data[key]['description']['identifier']
            if(blacklistcheck(settings.settings['recipeBlacklist'],key)==False):
                outcome = data[key][loadlist[key]]
                dirs.makedir(dirs.tempDir+"\\"+dirs.datasetFolder) #make temp folder
                if(isinstance(outcome,list)): #if output is list of dicts
                    items = [] #create list of items
                    for item in outcome: #add each item to list
                        if('data' in item):
                            itemData = item['data']
                            items.append(item['item']+"["+str(documentation[dataload[item['item']]][itemData])+"]")
                        else:
                            items.append(item['item'])
                    store.append(items)
                    items = ",".join(items) #turn items into string
                    itemData = None
                    document(id,str(items),path,itemData)
                elif(isinstance(outcome,dict)): #if output is one dict
                    if('data' in outcome):
                        itemData = data[key][loadlist[key]]['data']
                    store.append(outcome) #store the item
                    document(id,outcome['item'],path,itemData)
                elif(isinstance(outcome,str)):
                    store.append(outcome)
                    document(id,outcome,path,itemData)
            if(blacklistcheck(settings.settings['recipeBlacklist'],key)==True):
                print("Skipped blacklisted recipe "+id)
            debug(str(len(outcomes))+"/"+str(dirs.countDir(dirs.dataDir+"\\"+dirs.datasetFolder+"\\recipes"))+" outcomes loaded.")

def document(recipe,result,path,extradata): #used to create recipe documentation
    '''Creates recipe documentation'''
    if(extradata is None): 
        message = recipe+" = "+result+"\n"
    else:
        try:
            if(documentation[dataload[result]] is 'ignore'):
                message = recipe+" = "+result+"\n"
        except:
            pass
        try:
            message = recipe+" = "+result+"["+documentation[dataload[result]][extradata]+"]\n"
        except:
            message = recipe+" = "+result+"\n"
            print("Data error with recipe "+recipe+" and data "+str(extradata))
    with open(path,"a+") as file:
            file.write(message)

def scrambledata(data,store,path):
    '''Scrambles data given to it'''
    datakeys = data.keys()
    new_outcome = random.choice(outcomes)
    for key in loadlist:
        itemData = None
        if(key in datakeys):
            id = data[key]['description']['identifier']
            data[key][loadlist[key]] = new_outcome
            if(isinstance(new_outcome,list)): #if output is list of dicts
                items = [] #create list of items
                for item in new_outcome: #add each item to list
                    if('data' in item):
                        itemData = item['data']
                        items.append(item['item']+"["+str(documentation[dataload[item['item']]][itemData])+"]")
                    else:
                        items.append(item)
                store.append(items)
                items = ",".join(items) #turn items into string
                itemData = None
                document(id,items,path,itemData)
            elif(isinstance(new_outcome,dict)): #if output is one dict
                if('data' in new_outcome):
                        itemData = data[key][loadlist[key]]['data']
                store.append(new_outcome['item'])
                document(id,new_outcome['item'],path,itemData)
            elif(isinstance(new_outcome,str)): #if output is string
                store.append(new_outcome)
                document(id,new_outcome,path,itemData)
            outcomes.remove(new_outcome)
            debug("Scrambled: "+str(len(scrambles)))
    return data

def load():
    '''Load recipes from data'''
    #load data
    print("Loading outcomes from data... ",end="",flush=True)
    for file in os.listdir(dirs.dataDir+dirs.datasetFolder+"\\recipes"):
        with open(dirs.dataDir+dirs.datasetFolder+"\\recipes\\"+file) as json_file:
            data = json.load(json_file)
            loaddata(data,outcomes,dirs.vanilla)
    print("Loaded "+str(len(outcomes))+" outcomes.")

def scramble():
    '''Scramble recipes'''
    #scrambles data
    print("Scrambling data... ",end="",flush=True)
    for file in os.listdir(dirs.tempDir+dirs.datasetFolder+"\\recipes"):
        deletefile = False
        with open(dirs.tempDir+dirs.datasetFolder+"\\recipes\\"+file,"r") as json_file:
            data = json.load(json_file)
            datakeys = data.keys()
        for key in datakeys: #checks if file is in blacklist
            if(blacklistcheck(settings.settings['recipeBlacklist'],key)==True):
                json_file.close()
                deletefile = True
        if(deletefile==True):
            os.remove(json_file.name)
            debug("Removed "+json_file.name)
            continue
        with open(dirs.tempDir+dirs.datasetFolder+"\\recipes\\"+file,"w+") as json_file:
            json.dump(scrambledata(data,scrambles,dirs.randomized),json_file,indent=4)
    print("Scrambled "+str(len(scrambles))+" outcomes.")

def recipestart():
    '''Start randomizing recipes'''
    print("Starting recipe randomization")
    load()
    dirs.copydir(dirs.dataDir+dirs.datasetFolder+"\\recipes",dirs.tempDir+dirs.datasetFolder+"\\recipes")
    document("Seed",str(dirs.seed),dirs.randomized,None)
    scramble()