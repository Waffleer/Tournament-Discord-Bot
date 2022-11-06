import discord

from discord.ui import Button, View
from discord.ext import commands




bot = discord.Bot(
    debug_guilds = [1032120703094362192]
)
import json, requests
from time import sleep


def strToList(data):
    if "'" not in data and '"' not in data:
        return []
    data = data.strip("[]")
    data = data.replace("'","")
    data = data.replace('"',"")
    data = data.split(",")
    return(data)
def strToDict(string): # turns a string into a dict via json
    string.strip()
    context = json.loads(string)
    return context


def addServerTeamAPI(ctx, teamName):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    teamName = teamName.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/addServerTeam?user={user}&serverName={server}&tournamentName={category}&teamName={teamName}')
    context = resp.text
    return context
def addServerPlayerAPI(ctx, name): 
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    
    resp = requests.get(f'http://127.0.0.1:9101/addServerPlayer?user={user}&serverName={server}&tournamentName={category}&playerName={name}')
    context = json.loads(resp.text)
    return context
""" Ignore this block
def editServerPlayerTeam(message):
    user = str(message.author).replace("#","%23")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#","%23")
    team = str(message.content).split(' ')[2].replace("#","%23")
    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerTeam?user={user}&serverName={server}&playerName={name}&team={team}')
    context = json.loads(resp.text)
    return context
"""
def editServerPlayerRankAPI(ctx, name, rank):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerRank?user={user}&serverName={server}&tournamentName={category}&playerName={name}&rank={rank}')
    context = resp.text
    return context
def editServerPlayerAgeAPI(ctx, name, age):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerAge?user={user}&serverName={server}&tournamentName={category}&playerName={name}&age={age}')
    context = resp.text
    return context
def editServerPlayerRoleAPI(ctx, name, role):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    role = role.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerRole?user={user}&serverName={server}&tournamentName={category}&playerName={name}&role={role}')
    context = resp.text
    return context
def editServerPlayerDiscordNameAPI(ctx, name, discordUsername):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")

    discordUsername = discordUsername.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerDiscordName?user={user}&serverName={server}&tournamentName={category}&playerName={name}&discordName={discordUsername}')
    context = resp.text
    return context
def editServerPlayerCompleteAPI(ctx, name, rank, age, role, discordUsername):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")


    discordUsername = discordUsername.replace("#","%23")


    resp = requests.get(f'http://127.0.0.1:9101/editServerPlayerComplete?user={user}&serverName={server}&tournamentName={category}&playerName={name}&rank={rank}&age={age}&role={role}&discordName={discordUsername}')
    context = resp.text
    return context


def addTeamPlayerAPI(ctx, name, team):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    team = team.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/addTeamPlayer?user={user}&serverName={server}&tournamentName={category}&playerName={name}&teamName={team}')
    context = resp.text
    return context
def removeTeamPlayerAPI(ctx, name, team):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    team = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/removeTeamPlayer?user={user}&serverName={server}&tournamentName={category}&playerName={name}&teamName={team}')
    context = resp.text
    return context
def addMatchAPI(ctx, date, time, team1, team2):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    date = date.replace("#","%23")
    time = time.replace("#","%23")
    team1 = team1.replace("#","%23")
    team2 = team2.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/addMatch?user={user}&serverName={server}&tournamentName={category}&date={date}&time={time}&team1={team1}&team2={team2}')
    context = resp.text
    return context
def removeMatchAPI(ctx, matchTag):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    matchTag = matchTag.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/removeMatch?user={user}&serverName={server}&tournamentName={category}&matchTag={matchTag}')
    context = resp.text
    return context


def getTournamentAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    resp = requests.get(f'http://127.0.0.1:9101/getTournament?&serverName={server}')
    context = resp.text
    return context
def getTeamsAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    resp = requests.get(f'http://127.0.0.1:9101/getTeams?&serverName={server}&tournamentName={category}')
    context = resp.text
    return context
def getPlayersAPI(ctx):
    print("running")
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)
    resp = requests.get(f'http://127.0.0.1:9101/getPlayers?&serverName={server}&tournamentName={category}')
    print("returned")
    context = resp.text
    return context
def getMatchesAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    resp = requests.get(f'http://127.0.0.1:9101/getMatches?&serverName={server}&tournamentName={category}')
    context = resp.text
    return context
def getServerPlayerInfoAPI(ctx, player):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    resp = requests.get(f'http://127.0.0.1:9101/getServerPlayerInfo?&serverName={server}&tournamentName={category}&playerName={player}')
    context = resp.text
    return context
def getServerPlayerInfoByNameAPI(ctx, name):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)


    playerName = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/getServerPlayerInfo?&serverName={server}&tournamentName={category}&playerName={playerName}')
    context = resp.text
    return context
def getTeamMatchesAPI(ctx, teamName):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    teamName = teamName.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/getTeamMatches?&serverName={server}&teamName={teamName}&tournamentName={category}')
    context = resp.text
    return context
def getTeamRosterAPI(ctx, teamName):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    teamName = teamName.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9101/getTeamRoster?&serverName={server}&teamName={teamName}&tournamentName={category}')
    context = resp.text
    return context



def getServerReadyAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    resp = requests.get(f'http://127.0.0.1:9101/getServerReady?&serverName={server}')
    context = bool(resp.text)
    return context

def enableServerAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild.name)
    category = str(ctx.channel.category.name)
    print(user)
    print(server)
    resp = requests.get(f'http://127.0.0.1:9101/readyServer?&user={user}&serverName={server}')
    context = resp.text
    return context

def genTournamentAPI(ctx, name):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    category = name.split(' ')[1]

    resp = requests.get(f'http://127.0.0.1:9101/genTournament?user={user}&serverName={server}&tournamentName={category}')
    context = resp.text
    return context

#Utility Functions

#THIS NEEDS TO BE UPDATED or will be replaced with command descriptions
def adminHelpAPI(user, category):
    context = [
     f"""
<@{user.id}>
Welcome to the Admin Channel: This is where all of the tournament commands can be run from

**ONLY USERS WHO HAVE {category}-Admin ROLE CAN SEE THIS CHANNEL AND CAN USE COMMANDS**


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

            !editServerPlayerDiscordName {{name of player}} {{Discord Name}}
                - changes a player's server profile with new rank
                - stores a string, doesn't have to be a real rank

            !editServerPlayerComplete {{name of player}} {{rank}} {{age}} {{role}} {{Discord Name}}
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
            - do not have same team name as tournament name
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
        

    # General Commands
""",f"""

        !addServerRole
            - adds tournament role and team roles to registered players
            - should be run periodically or when a new person is added to a team

        !createTeamChannels
            - creates channels for each team in there own category
            - adds perms so only leagueAdmins and people with team tag can view category





            """]
    return context


def checkChannel(ctx):
    channel = ctx.channel
    category = channel.category
    if str(channel.name) == "adminchannel":
        usedCategories = getTournamentAPI(ctx)
        usedCategories = strToList(usedCategories)
        num = 0
        for x in usedCategories:
            if x == "logs.txt":
                usedCategories.pop(num)
            num += 1
        if str(category.name) in usedCategories:
            return True
        else:
            return False
    else:
        return False
def createChannel(message):
    pass
def applyRole(message, name, role):
    playerDict = getServerPlayerInfoByNameAPI(message, name).replace("'",'"')
    playerDict = strToDict(playerDict)
    discordName = f"{playerDict['discordName']}#{playerDict['discordTag']}"
    for z in message.guild.members:
        if str(z) == discordName:
            memberObj = z
    return memberObj.add_roles(role)



@bot.slash_command()
async def test(ctx):
    print("run")
    players = getPlayersAPI(ctx)
    print("ran")
    await ctx.send("Bruh")
    await ctx.send(str(players))

@bot.slash_command()
async def test2(ctx):
    players = getPlayersAPI(ctx)
    await ctx.send(str(players))

@bot.slash_command(description="you can add descriptons")
async def test3(ctx):
    
    if await serverready(ctx):
        await ctx.respond(str(ctx.channel.category))
    else:
        await ctx.respond("Server has not been made ready by the admin")

@bot.slash_command()
async def addroles(ctx):

    await ctx.send(type(ctx))

    context = checkChannel(ctx)
    if type(context) == bool:
        user = ctx.author
        channel = ctx.channel
        server = ctx.guild
        category = channel.category

        playerList = getPlayers(ctx)
        playerList = strToList(playerList)


        serverRoles = server.roles # Gets tournament Role
        tournamentRole = ""
        for x in serverRoles:
            if x.name == f"{category}":
                tournamentRole = x

        for x in playerList: # applies base tournament role to all members
            await applyRole(message, x, tournamentRole)
    
        teams = strToList(getTeams(message))

        for x in teams:
            #Checks to see if role exists already and if not creates one
            used = False
            for y in serverRoles:
                if f"{x}-Team" == str(y):
                    used = True
                    break
            teamRole = None
            if not used:
                teamRole = await server.create_role(name=f"{x}-Team")
            else:
                for y in serverRoles:
                    if y.name == f"{x}-Team":
                        teamRole = y

            players = getPlayers(message)
            players = strToList(players)
            for y in players: # adds role to discord tags
                await applyRole(message, y, teamRole)
            await message.channel.send("Success")
    else:
        pass


@bot.slash_command()
async def getteamroster(ctx, team_name):
    await ctx.send_response(getTeamRosterAPI(ctx, team_name))




@bot.slash_command()
async def serverready(ctx):
    ready = bool(getServerReadyAPI(ctx))
    await ctx.send_response(getServerReadyAPI(ctx), ephemeral=True)

class enableServerView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View

    def __init__ (self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(label="ENABLES BOT", style=discord.ButtonStyle.danger)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message(enableServerAPI(self.ctx)) # Send a message when the button is clicked


@bot.slash_command(description="Allows commands to be run by the the bot. Can only be run by admins")
async def enable_server(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category
    if user.guild_permissions.administrator:
        await ctx.send_response("DON'T RUN UNTIL YOU HAVE UPDATED THE SERVER INTEGRATIONS. see /get_started for details", ephemeral=True, view=enableServerView(ctx))

 



"""

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):

@bot.slash_command()
async def addroles(ctx):
"""



@bot.event
async def on_guild_join(guild):
    pass


@bot.slash_command()
async def test4(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category

    integrations = await ctx.guild.integrations()
    print(type(integrations))
    print(type(integrations[0]))

    await ctx.send_response(integrations, ephemeral=False)






from secrets import TOKEN2
bot.run(TOKEN2)