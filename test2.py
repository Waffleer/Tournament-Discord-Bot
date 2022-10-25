string = '{"name":"baconLeader2","dateAdded":"24/10/2022 17:08:19","team":"salad","age":"55","rank":"basic","role":"something","discordName":"TheBetterNick","discordTag":"5462"}'
import json

def strToDict(string): # turns a string into a dict via json
    string.strip()
    context = json.loads(string)
    return context



print(type(strToDict(string)))