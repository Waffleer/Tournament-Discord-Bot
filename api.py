from http import server
from fastapi import FastAPI
import os
import datetime

api = FastAPI()



@api.get("/ping")
async def ping(text):
    return {"string" : text}


import os
import datetime
import json
import random


def genNum(num, list): # generates a random number "num" digits that isn't on the inputted list
    returnNumber = ""
    for x in range(num):
        returnNumber = returnNumber + str(random.randint(0, 9))
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
    f.write(f"\n{logStr}")
    f.close()
    return logStr

def strToList(data):
    #['waffleer#URMOM', 'pfunk', 'fellstar']

    if "'" not in data:
        return []
    data = data.strip("[]")
    data = data.replace("'","")
    data = data.split(", ")
    return(data)

@api.get("/genTournament")
def genTournament(user, serverName, tournamentName): # Generates a server and file structure
    serverName = str(serverName)
    if not os.path.exists(f"servers/{serverName}/{tournamentName}"):
        os.makedirs(f"servers/{serverName}/{tournamentName}")
        os.makedirs(f"servers/{serverName}/{tournamentName}/players")
        os.makedirs(f"servers/{serverName}/{tournamentName}/teams")
        os.makedirs(f"servers/{serverName}/{tournamentName}/matches")
        f = open(f"servers/{serverName}/{tournamentName}/config.txt","x")
        config = {
            "allChannels": False,
        }
        f.write(str(config).replace("'",'"'))
        f.close()
        return logServer(serverName, f'{user} - Tournament Created - "{tournamentName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logSystem(f'{user} - Tournament Already Exists - "{tournamentName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')

@api.get("/getTournament")
def getTournament(serverName):
    return os.listdir(f"servers/{serverName}/")

@api.get("/genServer")
def genServer(user, serverName): # Generates a server and file structure
    serverName = str(serverName)
    if not os.path.exists(f"servers/{serverName}"):
        f = open(f"servers/{serverName}/logs.txt","x")
        f = open(f"servers/{serverName}/config.txt","x")
        f.close()
        return logServer(serverName, f'{user} - Server Created - "{serverName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logSystem(f'{user} - Server Already Exists - "{serverName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')


#genServer("TestUser","testing")

@api.get("/getServers")
def getServers(): # gets list of servers
    return os.listdir("servers")
#getServers()



@api.get("/getPlayers")
def getPlayers(serverName, tournamentName): # gets list of players on a server
    context = os.listdir(f"servers/{serverName}/{tournamentName}/players")
    context2 = []
    for x in context:
        context2.append(str(x).split(".")[0])
    return context2
#print(getPlayers("testing"))

@api.get("/getMatches")
def getMatches(serverName, tournamentName): # gets list of matches on a server
    matchList = os.listdir(f"servers/{serverName}/{tournamentName}/Matches")
    context = []
    for x in matchList:
        context.append(x.replace(".txt",""))
    return context
#print(getMatches("testing"))




@api.get("/addServerPlayer")
def addServerPlayer(user, serverName, tournamentName,playerName): # adds player to server with empty data structure
    if not str(playerName)+".txt" in getPlayers(serverName, tournamentName):
        f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt","x")
        playerDict = {
            "name": playerName,
            "dateAdded": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            "team": "free",
            "age": "",
            "rank": "",
            "role": "",
            "discordName": "",
        }
        playerDict = str(playerDict).replace("'",'"')
        f.write(playerDict)
        f.close()
        return logServer(serverName, f'{user} - Player "{playerName}" has been added to server- {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Player "{playerName}" already exists on server- {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(addServerPlayer("testUser","testing","waffleer#URMOM"))

@api.get("/getServerPlayerInfo")
def getServerPlayerInfo(serverName, tournamentName, playerName): # returns player information in a dict
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "r")
    read = f.read()
    read = strToDict(read)
    f.close()
    return read
#getServerPlayerInfo("testing", "waffleer#URMOM")

@api.get("/editServerPlayerTeam")
def editServerPlayerTeam(user, serverName, tournamentName, playerName, team): # edits player team, team name is not used to determine players on each team
    info = getServerPlayerInfo(serverName, tournamentName, playerName)
    info.update({"team": team})
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    if team == "":
        team = "blank"
    return logServer(serverName, f'{user} - Team for player "{playerName}" has been updated to "{team}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerTeam("testUser", "testing", "waffleer#URMOM", "testTeam"))

@api.get("/editServerPlayerRank")
def editServerPlayerRank(user, serverName, tournamentName, playerName, rank): # edits player rank
    info = getServerPlayerInfo(serverName, tournamentName, playerName)
    info.update({"rank": rank})
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Rank for player "{playerName}" has been updated to "{rank}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerRank("testUser", "testing", "waffleer#URMOM", "Diamond 2"))


@api.get("/editServerPlayerDiscordName")
def editServerPlayerRank(user, serverName, tournamentName, playerName, discordName): # edits player rank
    info = getServerPlayerInfo(serverName, tournamentName, playerName)
    info.update({"discordName": discordName})
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Discord Name for player "{playerName}" has been updated to "{discordName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerRank("testUser", "testing", "waffleer#URMOM", "Diamond 2"))




@api.get("/editServerPlayerAge")
def editServerPlayerAge(user, serverName, tournamentName, playerName, age): # edits player age
    info = getServerPlayerInfo(serverName, tournamentName, playerName)
    info.update({"age": age})
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Age for player "{playerName}" has been updated to "{age}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerAge("testUser", "testing", "waffleer#URMOM", "18"))

@api.get("/editServerPlayerComplete")
def editServerPlayerComplete(user, serverName, tournamentName, playerName, rank, age, role, discordName): # edits player team, rank, age
    info = getServerPlayerInfo(serverName, tournamentName, playerName)
    info.update({
        "rank": rank,
        "age": age,
        "role": role,
        "discordName": discordName,
        })
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Role, Rank, Age and Discord Name for player "{playerName}" has been updated to "{role}", "{rank}", "{age}", "{discordName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(editServerPlayerComplete("testUser", "testing", "waffleer#URMOM", "freeAgent", "Diamond 2", "18"))

@api.get("/editServerPlayerRole")
def editServerPlayerRole(user, serverName, tournamentName, playerName, role):
    info = getServerPlayerInfo(serverName, tournamentName, playerName)
    info.update({"role": role})
    f = open(f"servers/{serverName}/{tournamentName}/players/{playerName}.txt", "w")
    f.write(str(info).replace("'",'"')) # changes ' to " in string to not make the json loader break
    f.close()
    return logServer(serverName, f'{user} - Role for player "{playerName}" has been updated to "{role}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')


@api.get("/getTeams")
def getTeams(serverName, tournamentName): # gets list of teams on a server
    return os.listdir(f"servers/{serverName}/{tournamentName}/teams")
#print(getTeams("testing"))

@api.get("/addServerTeam")
def addServerTeam(user, serverName, tournamentName, teamName): # adds team to a server
    if not teamName in getTeams(serverName, tournamentName):
        os.makedirs(f"servers/{serverName}/{tournamentName}/teams/{teamName}")
        f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/players.txt","x")
        f.write("[]")
        f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/matches.txt","x")
        f.close()
        return logServer(serverName, f'{user} - Team "{teamName}" has been added - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Team "{teamName}" already exists - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(addServerTeams("testUser", "testing", "testTeam2"))

@api.get("/addTeamPlayer")
def addTeamPlayer(user, serverName, tournamentName, teamName, playerName): # adds a player under a team, changes player information to the team as well
    f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/players.txt","r")
    data = f.read()
    data = strToList(data)
    if playerName not in data:
        data.append(str(playerName))
        f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/players.txt","w")
        f.write(str(data))
        f.close()
        print(editServerPlayerTeam(user, serverName, tournamentName, playerName, teamName))
        return logServer(serverName, f'{user} - Player "{playerName}" has been added to "{teamName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Player "{playerName}" was already in "{teamName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(addTeamPlayer("testUser", "testing","testTeam","waffleer#URMOM"))

@api.get("/removeTeamPlayer")
def removeTeamPlayer(user, serverName, tournamentName, teamName, playerName): # adds a player under a team, changes player information to the team as well
    f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/players.txt","r")
    data = f.read()
    data = strToList(data)
    if playerName in data:
        try:
            for x in range(0, len(data)):
                #print(x)
                if data[x] == str(playerName):
                    #print(f"\n\n\n removed \n\n\n")
                    data.pop(x)
            f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/players.txt","w")
            f.write(str(data))
            f.close()
        except IndexError:
            pass
        #print(editServerPlayerTeam(user, serverName, tournamentName, playerName, ""))
        return logServer(serverName, f'{user} - Player "{playerName}" has been removed from "{teamName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Player "{playerName}" was not found in "{teamName}" - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(removeTeamPlayer("testUser", "testing","testTeam","waffleer#URMOM"))

@api.get("/getTeamRoster")
def getTeamRoster(serverName, tournamentName, teamName): # returns all of the player's data for a team
    f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/players.txt","r")
    playerList = f.read()
    f.close()
    #print(playerList)
    if "," not in playerList and "'" not in playerList:
        return None
    playerList = strToList(playerList)

    context = []
    """
    try:
        for x in range(0, len(playerList)):
            el = playerList[x]
            if "#" in el or ")" in el:
                pass
            else:
                playerList.pop(x)
    except IndexError:
            pass
    """
    for x in playerList:
        context.append(getServerPlayerInfo(serverName, tournamentName,  x))
    


    return context
#print(getTeamRoster("testing", "testTeam"))





@api.get("/getTeamMatches")
def getTeamMatches(serverName, tournamentName, teamName): # returns the dictionaries for all of the matches assosiated with a team
    f = open(f"servers/{serverName}/{tournamentName}/teams/{teamName}/matches.txt","r")
    matchList = f.read()
    matchList = matchList.split("\n")
    try:
        for x in range(0, len(matchList)):
            el = matchList[x]
            if "1" in el or "2" in el or "3" in el or "4" in el or "5" in el or "6" in el or "7" in el or "8" in el or "9" in el or "0" in el:
                pass
            else:
                matchList.pop(x)
        f.close()
    except IndexError:
            pass

    context = []
    for x in matchList:
        f = open(f"servers/{serverName}/{tournamentName}/matches/{x}.txt","r")
        data = f.read()
        data = strToDict(data)
        context.append(data)
    return context
#print(getTeamMatches("testing", "testTeam"))

@api.get("/addMatch")
def addMatch(user, serverName, tournamentName, date, time, team1, team2): # Adds match object to the matches folder, then adds the matches to the related teams, date should be in a dd/mm/year format, time should be in a hour:day format in military time
    matchList = getMatches(serverName, tournamentName)
    for x in matchList:
        x = x.strip(".txt")
        x = int(x)
    key = genNum(6, matchList)
    date = date.split("/")
    day = date[0]
    month = date[1]
    year = date[2]

    time = time.split(":")
    hour = time[0]
    minute = time[1]

    f = open(f"servers/{serverName}/{tournamentName}/matches/{key}.txt","x")
    matchDict = {
        "name": key,
        "dateAdded": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "time": {"hour": hour, "minute": minute},
        "date": {"year": year, "month": month, "day": day},
        "team1": team1,
        "team2": team2
    }
    matchDict = str(matchDict).replace("'",'"')
    f.write(matchDict)
    f.close()

    f = open(f"servers/{serverName}/{tournamentName}/teams/{team1}/matches.txt","a")
    f.write(f"\n{key}")
    f.close

    f = open(f"servers/{serverName}/{tournamentName}/teams/{team2}/matches.txt","a")
    f.write(f"\n{key}")
    f.close

    return logServer(serverName, f'{user} - Match Tag : {key} - A Match between {team1} and {team2} has been added on {date}, at {time} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(addMatch("testUser", "testing", "20/10/2022", "14:30", "testTeam", "testTeam2"))

@api.get("/removeMatch")
def removeMatch(user, serverName, tournamentName, matchTag): # Removes a match object to the matches folder, then removes the matches in the related teams
    try:
        f = open(f"servers/{serverName}/{tournamentName}/matches/{matchTag}.txt","r")
    except:
        return logServer(serverName, f'{user} - The match that was suppose to be deleted could not be found - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    data = f.read()
    data = strToDict(data)

    team1 = data["team1"]
    team2 = data["team2"]
    date = data["date"]
    time = data["time"]
    
    f = open(f"servers/{serverName}/{tournamentName}/teams/{team1}/matches.txt","r")
    matchList = f.read()
    f.close()
    os.remove(f"servers/{serverName}/{tournamentName}/teams/{team1}/matches.txt")
    f = open(f"servers/{serverName}/{tournamentName}teams/{team1}/matches.txt","a")
    try:
        matchList = matchList.split("\n")
        for x in range(0, len(matchList)):
            el = matchList[x]
            if "1" in el or "2" in el or "3" in el or "4" in el or "5" in el or "6" in el or "7" in el or "8" in el or "9" in el or "0" in el:
                if str(matchTag) == str(el):
                    matchList.pop(x)
                else:
                    f.write(f"\n{el}")
            else:
                matchList.pop(x)
        f.close()
    except IndexError:
        pass


    f = open(f"servers/{serverName}/{tournamentName}/teams/{team2}/matches.txt","r")
    matchList = f.read()
    f.close()
    os.remove(f"servers/{serverName}/{tournamentName}/teams/{team2}/matches.txt")
    f = open(f"servers/{serverName}/{tournamentName}/teams/{team2}/matches.txt","a")
    matchList = matchList.split("\n")
    try:
        for x in range(0, len(matchList)):
            el = matchList[x]
            if "1" in el or "2" in el or "3" in el or "4" in el or "5" in el or "6" in el or "7" in el or "8" in el or "9" in el or "0" in el:
                if str(matchTag) == str(el):
                    matchList.pop(x)
                else:
                    f.write(f"\n{el}")
            else:
                matchList.pop(x)
        f.close()
    except IndexError:
        pass
    os.remove(f"servers/{serverName}/{tournamentName}/matches/{matchTag}.txt")

    return logServer(serverName, f'{user} - A Match between {team1} and {team2} has been removed on {date}, at {time} - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#print(removeMatch("testUser", "testing", "918770"))

