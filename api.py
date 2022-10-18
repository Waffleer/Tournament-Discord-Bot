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


@api.get("/ping")
async def ping():
    return {"string": "Pong"}


