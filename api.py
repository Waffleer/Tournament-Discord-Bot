from http import server
from fastapi import FastAPI
import os
import datetime

api = FastAPI()



@api.get("/ping")
async def ping(text):
    return {"string" : text}


