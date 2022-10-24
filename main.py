import discord
import discord.ext
from discord.ext import commands #, tasks
from secrets import TOKEN
import json, requests

intents = discord.Intents.default()
intents.message_content = True

from time import sleep

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
    leagueName = str(message.channel.category.name)


    content = str(message.content).split(' ', 1)[1]
    resp = requests.get(f'http://127.0.0.1:9101/addServerTeam?user={user}&serverName={server}&tournamentName={leagueName}&teamName={content}')
    context = resp.text.replace(")","#")
    return context
    
def addServerPlayer(message): 
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)
    content = str(message.content).split(' ', 1)[1].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/addServerPlayer?user={user}&serverName={server}&tournamentName={leagueName}&playerName={content}')
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
    leagueName = str(message.channel.category.name)
    name = str(message.content).split(' ')[1].replace("#",")")
    rank = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerRank?user={user}&serverName={server}&tournamentName={leagueName}&playerName={name}&rank={rank}')
    context = resp.text.replace(")","#")
    return context

def editServerPlayerAge(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)
    name = str(message.content).split(' ')[1].replace("#",")")
    age = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerAge?user={user}&serverName={server}&tournamentName={leagueName}&playerName={name}&age={age}')
    context = resp.text.replace(")","#")
    return context

def editServerPlayerRole(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)
    name = str(message.content).split(' ')[1].replace("#",")")
    role = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerRole?user={user}&serverName={server}&tournamentName={leagueName}&playerName={name}&role={role}')
    context = resp.text.replace(")","#")
    return context

def editServerPlayerComplete(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)
    name = str(message.content).split(' ')[1].replace("#",")")
    rank = str(message.content).split(' ')[2].replace("#",")")
    age = str(message.content).split(' ')[3].replace("#",")")
    role = str(message.content).split(' ')[4].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerComplete?user={user}&serverName={server}&tournamentName={leagueName}&playerName={name}&rank={rank}&age={age}&role={role}')
    context = resp.text.replace(")","#")
    return context





def addTeamPlayer(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)
    name = str(message.content).split(' ')[1].replace("#",")")
    team = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/addTeamPlayer?user={user}&serverName={server}&tournamentName={leagueName}&playerName={name}&teamName={team}')
    context = resp.text.replace(")","#")
    return context

def removeTeamPlayer(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)
    name = str(message.content).split(' ')[1].replace("#",")")
    team = str(message.content).split(' ')[2].replace("#",")")
    resp = requests.get(f'http://127.0.0.1:9101/removeTeamPlayer?user={user}&serverName={server}&tournamentName={leagueName}&playerName={name}&teamName={team}')
    context = resp.text.replace(")","#")
    return context

def addMatch(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    date = str(message.content).split(' ')[1].replace("#",")")
    time = str(message.content).split(' ')[2].replace("#",")")
    team1 = str(message.content).split(' ')[3].replace("#",")")
    team2 = str(message.content).split(' ')[4].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/addMatch?user={user}&serverName={server}&tournamentName={leagueName}&date={date}&time={time}&team1={team1}&team2={team2}')
    context = resp.text.replace(")","#")
    return context

def removeMatch(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    matchTag = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/removeMatch?user={user}&serverName={server}&tournamentName={leagueName}&matchTag={matchTag}')
    context = resp.text.replace(")","#")
    return context





def getTournament(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)

    resp = requests.get(f'http://127.0.0.1:9101/getTournament?&serverName={server}')
    context = resp.text.replace(")","#")
    return context

def getTeams(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    resp = requests.get(f'http://127.0.0.1:9101/getTeams?&serverName={server}&tournamentName={leagueName}')
    context = resp.text.replace(")","#")
    return context
    
def getPlayers(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    resp = requests.get(f'http://127.0.0.1:9101/getPlayers?&serverName={server}&tournamentName={leagueName}')
    context = resp.text.replace(")","#")
    return context

def getMatches(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    resp = requests.get(f'http://127.0.0.1:9101/getMatches?&serverName={server}&tournamentName={leagueName}')
    context = resp.text.replace(")","#")
    return context

def getServerPlayerInfo(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    playerName = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/getServerPlayerInfo?&serverName={server}&tournamentName={leagueName}&playerName={playerName}')
    context = resp.text.replace(")","#")
    return context

def getTeamMatches(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    teamName = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/getTeamMatches?&serverName={server}&teamName={teamName}&tournamentName={leagueName}')
    context = resp.text.replace(")","#")
    return context

def getTeamRoster(message):
    user = str(message.author).replace("#",")")
    channel = str(message.channel.name)
    server = str(message.guild)
    leagueName = str(message.channel.category.name)

    teamName = str(message.content).split(' ')[1].replace("#",")")

    resp = requests.get(f'http://127.0.0.1:9101/getTeamRoster?&serverName={server}&teamName={teamName}&tournamentName={leagueName}')
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

def adminHelp(user, leagueName):
    context = [
     f"""
<@{user.id}>
Welcome to the Admin Channel: This is where all of the tournament commands can be run from

**ONLY USERS WHO HAVE {leagueName}-Admin ROLE CAN SEE THIS CHANNEL AND CAN USE COMMANDS**

Things to do next:
Edit your tournament Config file - these command can only be run from this channel
    !config {{variable}} True/False


**BANNED CHARACTERS**
# - only use in discord name and riot id
"
'
)
(
&
?
**IT WILL BREAK SHIT THAT I HAVE TO FIX MANUALLY**

""",f"""
Perimeters for commands should be separated with spaces
    
Things that you can do now:


    # add players to the server database
        !addServerPlayer {{name of player}}
            - This will add a empty player file to the database which you can edit
            - no duplicate player names

            !editServerPlayerRank {{name of player}} {{rank}}
                - changes a player's server profile with new rank
                - stores a string, doesn't have to be a real rank

            !editServerPlayerAge {{name of player}} {{age}}
                - changes a player's server profile with new age
                - stores a string, doesn't have to be a number, but why wouldn't it be

            !editServerPlayerRole {{name of player}} {{role}}
                - changes a player's server profile with new rank
                - stores a string, doesn't have to be a real rank

            !editServerPlayerComplete {{name of player}} {{rank}} {{age}} {{role}}
                - changes a player's server profile with all new information
                - used if manually adding a player


            !getPlayers
                - returns all players in tournament

            !getServerPlayerInfo {{name of player}}
                - returns player info
                - need to make it look better
                     
    # add players from csv
        - for when you need to ad 60 players
        - not made next but will be once I see the google for max makes for registration
        - might make one for teams as well


    # add teams
""",f"""
        !addServerTeam {{name of team}} 
            - adds a new team folder to database where you can store players and matches
            - no duplicate team names
            - Banned Team Names
                - free

            !addTeamPlayer {{name of player}} {{name of team}}
                - adds player to team roster
                - player must registered in the server via !addServerPlayer

            !removeTeamPlayer {{name of player}} {{name of team}}
                - removes player to team roster
                - player must be on the team


            !getTeams
                - returns all teams in a tournament

            !getTeamMatches {{name of team}}
                - returns all matches associated with each team

            !getTeamRoster {{name of team}}
                - returns all players on a team and there information


    # add matches
""",f"""
        !addMatch {{date}} {{time}} {{name of team 1}} {{name of team 2}}
            - Adds match to the matches database and links it to the teams listed
            - date should be in a dd/mm/year format
            - time should be in a hour:day format in military time (No timezone)
            - teams must be registered with !addServerTeam
            Example: !addMatch 12/06/2000 14:30 {{name of team 1}} {{name of team 2}}

        !removeMatch {{match tag}}
            - removes match from database
            - match tag is given when match is created
            - match tag is given via !getMatches


        !getMatches
            - returns all match tags
            - used for debug and such, not very helpful, use !getTeamMatches for info
        


            """]
    return context



def checkChannel(message):
    channel = message.channel
    category = channel.category
    if str(channel.name) == "adminchannel":
        usedCategories = getTournament(message)
        usedCategories = strToList(usedCategories)
        num = 0
        for x in usedCategories:
            if x == "logs.txt":
                usedCategories.pop(num)
            num += 1
        if str(category.name) in usedCategories:
            return True
        else:
            return f""
    else:
        return f""


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
        user = message.author
        channel = message.channel
        server = message.guild
        category = channel.category

        serverRoles = server.roles
        adminRole = ""
        for x in serverRoles:
            if x.name == f"{category.name}-Admin":
                adminRole = x

        print(adminRole)

        if category.name != "adminchannel":
            await channel.send(f"Not in adminchannel")
            return None
        
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
                teamRole = await server.create_role(name=f"{x}-Team")

                category = await message.guild.create_category(name=f"{x}-Team")
                general = await category.create_text_channel("general")
                vibes = await category.create_voice_channel("vibes")
                match = await category.create_voice_channel("match")

                await category.set_permissions(teamRole, view_channel=True)
                await category.set_permissions(adminRole, view_channel=True)
                await category.set_permissions(server.default_role, view_channel=False)





        if len(repeatCategories) > 0:
            await message.channel.send(f"Success in making {num} team channels - {madeCategories}\nThese Team channels already existed - {repeatCategories}")
        else:
            await message.channel.send(f"Success in making {num} team channels - {teams}")


    if message.content.startswith('!test2'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send("In a valid channel")
        else:
            await message.channel.send(context)


    if message.content.startswith('!adminHelp'):
        user = message.author
        channel = message.channel
        server = message.guild
        leagueName = message.channel.category.name
        for x in adminHelp(user, leagueName):
            await channel.send(x)

    if message.content.startswith("!help"):
        user = message.author
        channel = message.channel
        server = message.guild
        leagueName = message.channel.category.name
        await channel.send("""
This will be created later
see !getStarted for tournament creation

see !adminHelp for help in a adminChannel


        """)


    if message.content.startswith("!getStarted"):
        channel = message.channel
        await channel.send("Generate a tournament with !createTournament, only server admins can run this command. \n You can configure the rest in the channel")

    if message.content.startswith('!createTournament'):
        user = message.author
        channel = message.channel
        server = message.guild

        leagueName = str(message.content).split(' ')[1]

        if user.guild_permissions.administrator:
            serverList = requests.get(f'http://127.0.0.1:9101/getServers')
            serverList = strToList(serverList.text)
            if server.name in serverList:
                resp = requests.get(f'http://127.0.0.1:9101/genServers')
                context = resp.text.replace(")","#")
                await channel.send(context)
                sleep(1)


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

                for x in adminHelp(user, leagueName):
                    message = await adminChannel.send(x)
                    await message.pin()

                await message.channel.send(f"The league has been created, head over to the admin channel to see what to do next")
            else:
                await message.channel.send(f"This league Name is already in use")
        else:
            await message.channel.send(f"You are not an admin on this server, only administrators can use this command")


    #print(message.content)
    if message.content.startswith('!addServerTeam'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(addServerTeam(message))
        else:
            pass
        
    if message.content.startswith('!addServerPlayer'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(addServerPlayer(message))
        else:
            pass
        
    #if message.content.startswith('!editServerPlayerTeam'):
    #    await message.channel.send(editServerPlayerTeam(message))

    if message.content.startswith('!editServerPlayerRank'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(editServerPlayerRank(message))
        else:
            pass
        
    if message.content.startswith('!editServerPlayerAge'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(editServerPlayerAge(message))
        else:
            pass
        
    if message.content.startswith('!editServerPlayerRole'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(editServerPlayerRole(message))
        else:
            pass
        
    if message.content.startswith('!editServerPlayerComplete'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(editServerPlayerComplete(message))
        else:
            pass
        
    if message.content.startswith('!addTeamPlayer'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(addTeamPlayer(message))
        else:
            pass
        
    if message.content.startswith('!removeTeamPlayer'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(removeTeamPlayer(message))
        else:
            pass
        
    if message.content.startswith('!addMatch'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(addMatch(message))
        else:
            pass
        
    if message.content.startswith('!removeMatch'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(removeMatch(message))
        else:
            pass
        


    if message.content.startswith('!getTeams'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(getTeams(message))
        else:
            pass
        
    if message.content.startswith('!getPlayers'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(getPlayers(message))
        else:
            pass
        
    if message.content.startswith('!getMatches'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(getMatches(message))
        else:
            pass
        
    if message.content.startswith('!getServerPlayerInfo'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(getServerPlayerInfo(message))
        else:
            pass
        
    if message.content.startswith('!getTeamMatches'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(getTeamMatches(message))
        else:
            pass
        
    if message.content.startswith('!getTeamRoster'):
        context = checkChannel(message)
        if type(context) == bool:
            await message.channel.send(getTeamRoster(message))
        else:
            pass
        







client.run(TOKEN)

