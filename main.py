import discord
import discord.ext
from discord.ext import commands #, tasks
from secrets import TOKEN
import json, requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def addServerTeam(message):
    user = str(message.author).replace("#","_")
    channel = str(message.channel.name)
    server = str(message.guild)
    content = str(message.content).split(' ', 1)[1]
    print(user)
    print(server)
    print(content)
    resp = requests.get(f'http://127.0.0.1:9101/addServerTeam?user={user}&serverName={server}&teamName={content}')
    context = resp.text.replace(")","#")
    return context
    
def addServerPlayer(message): 
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    content = str(message.content).split(' ', 1)[1].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/addServerPlayer?user={user}&serverName={server}&playerName={content}')
    context = json.loads(resp.text).replace(")","#")
    return context

""" Ignore this block
def editServerPlayerTeam(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    team = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerTeam?user={user}&serverName={server}&playerName={name}&team={team}')
    context = json.loads(resp.text).replace(")","#")
    return context
"""
def editServerPlayerRank(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    rank = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerRank?user={user}&serverName={server}&playerName={name}&rank={rank}')
    context = resp.text.replace(")","#")
    return context

def editServerPlayerAge(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    age = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerAge?user={user}&serverName={server}&playerName={name}&age={age}')
    context = resp.text.replace(")","#")
    return context

def editServerPlayerComplete(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    #team = str(message.content).split(' ')[2].replace("#",")")
    rank = str(message.content).split(' ')[2].replace("#",")")
    age = str(message.content).split(' ')[3].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerComplete?user={user}&serverName={server}&playerName={name}&rank={rank}&age={age}')
    context = resp.text.replace(")","#")
    return context

def addTeamPlayer(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    team = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/addTeamPlayer?user={user}&serverName={server}&playerName={name}&teamName={team}')
    context = resp.text.replace(")","#")
    return context

def removeTeamPlayer(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    team = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/removeTeamPlayer?user={user}&serverName={server}&playerName={name}&teamName={team}')
    context = resp.text.replace(")","#")
    return context

def addMatch(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    date = str(message.content).split(' ')[1].replace("#",")")
    time = str(message.content).split(' ')[2].replace("#",")")
    team1 = str(message.content).split(' ')[3].replace("#",")")
    team2 = str(message.content).split(' ')[4].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/addMatch?user={user}&serverName={server}&date={date}&time={time}&team1={team1}&team2={team2}')
    context = resp.text.replace(")","#")
    return context

def removeMatch(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    matchTag = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/removeMatch?user={user}&serverName={server}&matchTag={matchTag}')
    context = resp.text.replace(")","#")
    return context





def getTeams(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    resp = requests.get(f'http://127.0.0.1:9101/getTeams?&serverName={server}')
    context = resp.text.replace(")","#")
    return context

def getPlayers(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    resp = requests.get(f'http://127.0.0.1:9101/getPlayers?&serverName={server}')
    context = resp.text.replace(")","#")
    return context

def getMatches(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    resp = requests.get(f'http://127.0.0.1:9101/getMatches?&serverName={server}')
    context = resp.text.replace(")","#")
    return context

def getServerPlayerInfo(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    playerName = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/getServerPlayerInfo?&serverName={server}&playerName={playerName}')
    context = resp.text.replace(")","#")
    return context

def getTeamMatches(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    teamName = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/getTeamMatches?&serverName={server}&teamName={teamName}')
    context = resp.text.replace(")","#")
    return context

def getTeamRoster(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    teamName = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/getTeamRoster?&serverName={server}&teamName={teamName}')
    context = resp.text.replace(")","#")
    return context



@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #print(message.content)
    if message.content.startswith('!addServerTeam'):
        await message.channel.send(addServerTeam(message))

    if message.content.startswith('!addServerPlayer'):
        await message.channel.send(addServerPlayer(message))

    #if message.content.startswith('!editServerPlayerTeam'):
    #    await message.channel.send(editServerPlayerTeam(message))

    if message.content.startswith('!editServerPlayerRank'):
        await message.channel.send(editServerPlayerRank(message))

    if message.content.startswith('!editServerPlayerAge'):
        await message.channel.send(editServerPlayerAge(message))

    if message.content.startswith('!editServerPlayerComplete'):
        await message.channel.send(editServerPlayerComplete(message))

    if message.content.startswith('!addTeamPlayer'):
        await message.channel.send(addTeamPlayer(message))

    if message.content.startswith('!removeTeamPlayer'):
        await message.channel.send(removeTeamPlayer(message))

    if message.content.startswith('!addMatch'):
        await message.channel.send(addMatch(message))

    if message.content.startswith('!removeMatch'):
        await message.channel.send(removeMatch(message))




    if message.content.startswith('!getTeams'):
        await message.channel.send(getTeams(message))

    if message.content.startswith('!getPlayers'):
        await message.channel.send(getPlayers(message))

    #if message.content.startswith('!getMatches'):
    #    await message.channel.send(getMatches(message))

    if message.content.startswith('!getServerPlayerInfo'):
        await message.channel.send(getServerPlayerInfo(message))

    if message.content.startswith('!getTeamMatches'):
        await message.channel.send(getTeamMatches(message))

    if message.content.startswith('!getTeamRoster'):
        await message.channel.send(getTeamRoster(message))







client.run(TOKEN)


"""
import json
import requests

resp = requests.get('http://127.0.0.1:9101/genServer?user=testUser,serverName=Bacon')
respDict = json.loads(resp.text)
"""