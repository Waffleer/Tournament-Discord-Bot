import discord
import discord.ext
from discord.ext import commands #, tasks
from secrets import TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('!URL'):
    #username = str(message.author).split("#")[0]
    #channel = str(message.channel.name)
    #user_message = str(message.content)
       
        await message.channel.send(f'Worked')

client.run(TOKEN)


"""
import json
import requests

resp = requests.get('http://127.0.0.1:9101/genServer?user=testUser,serverName=Bacon')
respDict = json.loads(resp.text)
"""