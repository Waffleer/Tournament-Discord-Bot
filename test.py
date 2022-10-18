import os
import datetime

def genNum(num, list):
    returnNumber = ""
    for x in range(num):
        returnNumber = returnNumber + str()
    if returnNumber in list:
        returnNumber = genNum(num, list)
    return returnNumber

def logServer(serverName, logStr):
    f = open("logsFull.txt", "a")
    f.write(logStr)
    f.close()
    f = open(f"servers/{serverName}/logs.txt","a")
    f.write(logStr)
    f.close()
    return logStr

def logFull(logStr):
    f = open("logsFull.txt", "a")
    f.write(logStr)
    f.close()
    return logStr


def gen(user, serverName):
    serverName = str(serverName)
    if not os.path.exists(f"servers/{serverName}"):
        os.makedirs(f"servers/{serverName}")
        os.makedirs(f"servers/{serverName}/players")
        os.makedirs(f"servers/{serverName}/teams")
        f = open(f"servers/{serverName}/admin.txt","x")
        f = open(f"servers/{serverName}/secondary.txt","x")
        f = open(f"servers/{serverName}/matchs.txt","x")
        f = open(f"servers/{serverName}/logs.txt","x")
        f.close()

        return logFull(f"{user} - Server Created - {serverName}")
    else:
        return logFull(f"{user} - Server Already Exists - {serverName}")
gen("TestUser","testing1")

def getServers():
    return os.listdir("servers")
#getServers()

def addServerTeams(user, serverName, teamName):
    teamList = os.listdir(f"servers/{serverName}/teams")
    if not teamName in teamList:
        os.makedirs(f"servers/{serverName}/teams/{teamName}")
        return logServer(serverName, f'{user} - Team "{teamName}" has been added')
    else:
        return logServer(serverName, f'{user} - Team "{teamName}" already exists')


def updateServerInfo():
    #name
    #number of players
    #teams
        #team rosters
        #match list
    #matchs
    #list of player Numbers

    #turn matchs into team matches
    pass

print(addServerTeams("testUser","testing", "nothin"))
