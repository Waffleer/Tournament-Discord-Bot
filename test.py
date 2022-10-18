import os
import datetime

def genNum(num, list): # generates a random number "num" digits that isn't on the inputted list
    returnNumber = ""
    for x in range(num):
        returnNumber = returnNumber + str()
    if returnNumber in list:
        returnNumber = genNum(num, list)
    return returnNumber

def logServer(serverName, logStr): # logs to server log file as well as system
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
        return logSystem(serverName, f"{user} - Server Already Exists - {serverName} - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
genServer("TestUser","testing")

def getServers(): # gets list of servers
    return os.listdir("servers")
#getServers()

def addServerTeams(user, serverName, teamName): # adds team to a server
    teamList = os.listdir(f"servers/{serverName}/teams")
    if not teamName in teamList:
        os.makedirs(f"servers/{serverName}/teams/{teamName}")
        f = open(f"servers/{serverName}/teams/{teamName}/players.txt","x")
        f = open(f"servers/{serverName}/teams/{teamName}/matches.txt","x")
        f.close()
        return logServer(serverName, f'{user} - Team "{teamName}" has been added - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    else:
        return logServer(serverName, f'{user} - Team "{teamName}" already exists - {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#addServerTeams("testUser", "testing", "testTeam")

