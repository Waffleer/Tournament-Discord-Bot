from http import server
from fastapi import FastAPI
import os
import datetime

api = FastAPI()


def genNum(num, list):
    returnNumber = ""
    for x in range(num):
        returnNumber = returnNumber + str()
    if returnNumber in list:
        returnNumber = genNum(num, list)
    return returnNumber

@api.get("/ping")
async def ping():
    return {"string": "Pong"}

@api.get("/genServer")
async def gen(serverName):
    serverName = str(serverName)
    if not os.path.exists(f"servers/{serverName}"):
        os.makedirs(f"servers/{serverName}")
        os.makedirs(f"servers/{serverName}/match")
        os.makedirs(f"servers/{serverName}/player")
        os.makedirs(f"servers/{serverName}/teams")
        f = open(f"servers/{serverName}/admin.txt","x")
        f = open(f"servers/{serverName}/secondary.txt","x")
        f = open(f"servers/{serverName}/info.txt","x")
        f = open(f"servers/{serverName}/logs.txt","x")
        f.write(f"Server created - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        f = open("servers.txt","a")
        f.write(f"{serverName} - {datetime.date.today()}")
        f.close()

        return f"Server Created - {serverName}"
    else:
        return f"Server Already Exists - {serverName}"

