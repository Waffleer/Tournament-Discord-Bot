import discord
import discord.ext
from discord.ext import commands #, tasks
from secrets import TOKEN
import json, requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def strToList(data):
    if "'" not in data and '"' not in data:
        return []
    data = data.strip("[]")
    data = data.replace("'","")
    data = data.replace('"',"")
    data = data.split(",")
    return(data)

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

def editServerPlayerRole(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    role = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerRole?user={user}&serverName={server}&playerName={name}&role={role}')
    context = resp.text.replace(")","#")
    return context

def editServerPlayerComplete(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#",")")
    rank = str(message.content).split(' ')[2].replace("#",")")
    age = str(message.content).split(' ')[3].replace("#",")")
    role = str(message.content).split(' ')[4].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerComplete?user={user}&serverName={server}&playerName={name}&rank={rank}&age={age}&role={role}')
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

def genTournament(message):
    user = str(message.author).replace("#",")")
    channel = message.channel.name
    server = str(message.guild).replace("#",")")

    leagueName = str(message.content).split(' ')[1]

    resp = requests.get(f'http://127.0.0.1:9101/genTournament?user={user}&serverName={server}&tournamentName={leagueName}')
    context = resp.text.replace(")","#")
    return context

#Utility Functions

def createChannel(message):
    pass


@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!createTeamChannels'):
        #should run an admin check
        user = str(message.author).replace("#",")")
        channel = str(message.channel.name)
        server = str(message.guild)
        
        teams = getTeams(message)
        teams = strToList(teams)

        usedCategories = message.guild.categories
        usedCategoriesNames = []
        for x in usedCategories:
            usedCategoriesNames.append(x.name)

        repeatCategories = []
        madeCategories = []
        num = 0
        for x in teams:
            if x in usedCategoriesNames:
                repeatCategories.append(x)
            else:
                num += 1
                madeCategories.append(x)
                category = await message.guild.create_category(name=x)
                await category.create_text_channel("general")
                await category.create_voice_channel("vibes")
                await category.create_voice_channel("match")



        if len(repeatCategories) > 0:
            await message.channel.send(f"Success in making {num} team channels - {madeCategories}\nThese Team channels already existed - {repeatCategories}")
        else:
            await message.channel.send(f"Success in making {num} team channels - {teams}")

    if message.content.startswith('!test1'):
        user = message.author
        channel = message.channel.name
        server = message.guild

        leagueName = str(message.content).split(' ')[1]


        usedCategories = server.categories
        usedCategoriesNames = []
        for x in usedCategories:
            usedCategoriesNames.append(x.name)

        if leagueName not in usedCategoriesNames:

            genTournament(message)

            adminRole = await server.create_role(name=f"{leagueName}-Admin", mentionable=True) # 
            leagueRole = await server.create_role(name=f"{leagueName}") # for general participents

            category = await server.create_category(name=leagueName)
            # add default pers so only people with league role
            adminChannel = await category.create_text_channel("adminChannel")
            #add perms and save to admin.txt
            general = await category.create_text_channel("general")

            await user.add_roles(adminRole, atomic=True)
            await adminChannel.set_permissions(adminRole, view_channel=True)
            await adminChannel.set_permissions(server.self_role, view_channel=True)
            await adminChannel.set_permissions(server.default_role, view_channel=False)

            await adminChannel.send(f"""
            @{user}
            Welcome to the Admin Channel: This is where all of the tournament commands can be run from

            **ONLY USERS WHO HAVE {leagueName}-Admin ROLE CAN SEE THIS CHANNEL AND CAN USE COMMANDS**

            Things to do next:
            Edit your tournament Config file - these command can only be run from this channel
                !config secondary True
            

        """)

            await message.channel.send(f"The league has been created, head over to the admin channel to see what to do next")
        else:
            await message.channel.send(f"This league Name is already in use")

            

        


    if message.content.startswith('!createTournament'):
        user = message.author
        channel = message.channel.name
        server = message.guild

        leagueName = str(message.content).split(' ')[1] #keep it short, will displayed with every role for league
        
        #genTournament(str(user).replace("#",")"), str(server), )
            #Creates file structure like genServer does


            #-- need to add leagueName to every method





            # tell them to run the commands from that channel to interact with this server

            # send the rest of info into the adminChannel

                # give user who ran commands perms in that channel

                # they can grant access to any roles who should have perms

            # if you want to make secondary commands usable only in secondary channels or all server channels

            # tell about the functions to grow league

                # add teams

                # add players

                    # add players from csv

                # add matches



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