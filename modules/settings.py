import json, os
from modules import dirs
settings = {
    'recipeBlacklist': [],
    'autoUpdate': True,
    }

def setUpdate(mode=bool):
    settings['autoUpdate'] = mode

def editrecipeFilter(mode,recipetype):
    if(mode=="add"):
        settings['recipeBlacklist'].append(recipetype)
    if(mode=="remove"):
        settings['recipeBlacklist'].remove(recipetype)

def loadSettings(path):
    global settings
    if(os.path.exists(path)):
        with open(path,"r+") as json_file:
            data = json.load(json_file)
            settings = data
    if(not os.path.exists(path)):
        with open(path,"w+") as json_file:
            json.dump(settings,json_file,indent=4)

def writeSettings(path):
    with open(path,"w+") as json_file:
        json.dump(settings,json_file,indent=4)