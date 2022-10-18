import os
import datetime
import json

def genNum(num, list): # generates a random number "num" digits that isn't on the inputted list
    returnNumber = ""
    for x in range(num):
        returnNumber = returnNumber + str()
    if returnNumber in list:
        returnNumber = genNum(num, list)
    return returnNumber

def strToDict(string): # turns a string into a dict via json
    context = json.loads(string)
    return context

def logServer(serverName, logStr): # logs to server log file as well as system log file
    f = open("logsFull.txt", "a")
    f.write("\n"+logStr)
    f.close()
    f = open(f"servers/{serverName}/logs.txt","a")
    f.write("\n"+logStr)
    f.close()
    return logStr

def logSystem(logStr): # logs only to system log file
    f = open("logsFull.txt", "a")
    f.write(logStr)
    f.close()
    return logStr

def strToList(data):
    #['waffleer#URMOM', 'pfunk', 'fellstar']
    data = data.strip("[]")
    data = data.replace("'","")
    data = data.split(", ")
    return(data)


def genServer(user, serverName): # Generates a server and file structure
    serverName = str(serverName)
    if not os.path.exists(f"servers/{serverName}"):
        os.makedirs(f"servers/{serverName}")
        os.makedirs(f"servers/{serverName}/players")
        os.makedirs(f"servers/{serverName}/teams")
        os.makedirs(f"servers/{serverName}/matches")
        f = open(f"servers/{serverName}/admin.txt","x")
        f = open(f"servers/{serverName}/secondary.txt","x")
        f = open(f"servers/{serverName}/logs.txt","x")
        f.close()

        return logServer(serverName, f"{user} - Server Created - {serverName} - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        return logSystem(f"{user} - Server Already Exists - {serverName} - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
#genServer("TestUser","testing")

def getServers(): # gets list of servers
    return os.listdir("servers")
#getServers()




def getPlayers(serverName): # gets list of players on a server
    return os.listdir(f"servers/{serverName}/players")
#print(getPlayers("testing"))

def getMatches(serverName): # gets list of matches on a server
    return os.listdir(f"servers/{serverName}/Matches")
#print(getMatches("testing"))

def addServerPlayer(user, serverName, playerName): # adds player to server with empty data structure
    if not str(playerName)+".txt" in getPlayers(serverName):
        f = open(f"servers/{serverName}/players/{playerName}.txt","x")
        playerDict = {
            "name": playerName,
            "dateAdded": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            "team": "freeAgent",
            "age": "",
            "rank": ""
        }
        playerDict = str(playerDict).replace("'",'"')
        f.write(playerDict)
        f.close()
        return logServer(serverName, f'{user} - Player "{playerName}" has been added to server- {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Player "{playerName}" already exists on server- {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(addServerPlayer("testUser","testing","waffleer#URMOM"))

def getServerPlayerInfo(serverName, playerName): # returns player information in a dict
    f = open(f"servers/{serverName}/players/{playerName}.txt", "r")
    read = f.read()
    read = strToDict(read)
    f.close()
    return read

def editServerPlayerTeam(user, serverName, playerName, team): # edits player team, team name is not used to determine players on each team
    info = getServerPlayerInfo(serverName, playerName)
    info.update({"team": team})
    f = open(f"servers/{serverName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Team for player "{playerName}" has been updated to {team} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerTeam("testUser", "testing", "waffleer#URMOM", "testTeam"))

def editServerPlayerRank(user, serverName, playerName, rank): # edits player rank
    info = getServerPlayerInfo(serverName, playerName)
    info.update({"rank": rank})
    f = open(f"servers/{serverName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Rank for player "{playerName}" has been updated to {rank} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerRank("testUser", "testing", "waffleer#URMOM", "Diamond 2"))

def editServerPlayerAge(user, serverName, playerName, age): # edits player age
    info = getServerPlayerInfo(serverName, playerName)
    info.update({"age": age})
    f = open(f"servers/{serverName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Age for player "{playerName}" has been updated to {age} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerAge("testUser", "testing", "waffleer#URMOM", "18"))

def editServerPlayerComplete(user, serverName, playerName, team, rank, age): # edits player team, rank, age
    info = getServerPlayerInfo(serverName, playerName)
    info.update({
        "team": team,
        "rank": rank,
        "age": age,
        })
    f = open(f"servers/{serverName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Team, Rank, and Age for player "{playerName}" has been updated to {team}, {rank} ,{age} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerComplete("testUser", "testing", "waffleer#URMOM", "freeAgent", "Diamond 2", "18"))




def getTeams(serverName): # gets list of teams on a server
    return os.listdir(f"servers/{serverName}/teams")
#print(getTeams("testing"))

def addServerTeams(user, serverName, teamName): # adds team to a server
    if not teamName in getTeams(serverName):
        os.makedirs(f"servers/{serverName}/teams/{teamName}")
        f = open(f"servers/{serverName}/teams/{teamName}/players.txt","x")
        f.write("[]")
        f = open(f"servers/{serverName}/teams/{teamName}/matches.txt","x")
        f.close()
        return logServer(serverName, f'{user} - Team "{teamName}" has been added - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Team "{teamName}" already exists - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(addServerTeams("testUser", "testing", "testTeam2"))

def addTeamPlayer(user, serverName, teamName, playerName):
    f = open(f"servers/{serverName}/teams/{teamName}/players.txt","r")
    data = f.read()
    data = strToList(data)
    if playerName not in data:
        data.append(str(playerName))
        f = open(f"servers/{serverName}/teams/{teamName}/players.txt","w")
        f.write(str(data))
        f.close()
        return logServer(serverName, f'{user} - Player "{playerName}" has been added to {teamName} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Player "{playerName}" was already in {teamName} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')


print(addTeamPlayer("testUser", "testing","testTeam","fellfdsastfdsa"))

#print(getServerPlayerInfo("testing","waffleer#URMOM"))
#print(type(getServerPlayerInfo("testing","waffleer#URMOM")))
