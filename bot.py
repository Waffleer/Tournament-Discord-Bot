import discord

from discord.ui import Button, View
from discord.ext import commands
import json, requests
from time import sleep
import datetime

#main - https://discord.com/api/oauth2/authorize?client_id=1038641710835703808&permissions=8&scope=bot%20applications.commands
#dev - https://discord.com/api/oauth2/authorize?client_id=1032121033186091031&permissions=8&scope=bot%20applications.commands

bot = discord.Bot(
    activity=
        discord.Activity(
            type=discord.ActivityType.custom, 
            name="See /Get for Help", 
            details="Just Trying to help, sheesh.", 
            start = datetime.datetime.now()
             ),

    debug_guilds = [1032120703094362192,1010740300823662623,1039937599063728279]
)



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

    resp = requests.get(f'http://127.0.0.1:9015/addServerTeam?user={user}&serverName={server}&tournamentName={category}&teamName={teamName}')
    context = resp.text
    return context
def addServerPlayerAPI(ctx, name, discord_username): 
    user = str(ctx.author).replace("#","%23")
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    discord_username = discord_username.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/addServerPlayer?user={user}&serverName={server}&tournamentName={category}&playerName={name}&discordName={discord_username}')
    print(resp.text)
    context = json.loads(str(resp.text).replace("'",'"'))
    return context
""" Ignore this block
def editServerPlayerTeam(message):
    user = str(message.author).replace("#","%23")
    channel = str(message.channel.name)
    server = str(message.guild)
    name = str(message.content).split(' ')[1].replace("#","%23")
    team = str(message.content).split(' ')[2].replace("#","%23")
    resp = requests.get(f'http://127.0.0.1:9015/editServerPlayerTeam?user={user}&serverName={server}&playerName={name}&team={team}')
    context = json.loads(resp.text)
    return context
"""
def editServerPlayerRankAPI(ctx, name, rank):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/editServerPlayerRank?user={user}&serverName={server}&tournamentName={category}&playerName={name}&rank={rank}')
    context = resp.text
    return context
def editServerPlayerAgeAPI(ctx, name, age):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/editServerPlayerAge?user={user}&serverName={server}&tournamentName={category}&playerName={name}&age={age}')
    context = resp.text
    return context
def editServerPlayerRoleAPI(ctx, name, role):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    role = role.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/editServerPlayerRole?user={user}&serverName={server}&tournamentName={category}&playerName={name}&role={role}')
    context = resp.text
    return context
def editServerPlayerDiscordNameAPI(ctx, name, discordUsername):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")

    discordUsername = discordUsername.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/editServerPlayerDiscordName?user={user}&serverName={server}&tournamentName={category}&playerName={name}&discordName={discordUsername}')
    context = resp.text
    return context
def editServerPlayerCompleteAPI(ctx, name, rank, age, role, discordUsername):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")


    discordUsername = discordUsername.replace("#","%23")


    resp = requests.get(f'http://127.0.0.1:9015/editServerPlayerComplete?user={user}&serverName={server}&tournamentName={category}&playerName={name}&rank={rank}&age={age}&role={role}&discordName={discordUsername}')
    context = resp.text
    return context


def addTeamPlayerAPI(ctx, name, team):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    team = team.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/addTeamPlayer?user={user}&serverName={server}&tournamentName={category}&playerName={name}&teamName={team}')
    context = resp.text
    return context
def removeTeamPlayerAPI(ctx, name, team):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    name = name.replace("#","%23")
    team = team.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/removeTeamPlayer?user={user}&serverName={server}&tournamentName={category}&playerName={name}&teamName={team}')
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

    resp = requests.get(f'http://127.0.0.1:9015/addMatch?user={user}&serverName={server}&tournamentName={category}&date={date}&time={time}&team1={team1}&team2={team2}')
    context = resp.text
    return context
def removeMatchAPI(ctx, matchTag):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    matchTag = matchTag.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/removeMatch?user={user}&serverName={server}&tournamentName={category}&matchTag={matchTag}')
    context = resp.text
    return context


def getTournamentAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    resp = requests.get(f'http://127.0.0.1:9015/getTournament?&serverName={server}')
    context = resp.text
    return context
def getTeamsAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    resp = requests.get(f'http://127.0.0.1:9015/getTeams?&serverName={server}&tournamentName={category}')
    context = resp.text
    return context
def getPlayersAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)
    resp = requests.get(f'http://127.0.0.1:9015/getPlayers?&serverName={server}&tournamentName={category}')
    context = resp.text
    return context
def getMatchesAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category)

    resp = requests.get(f'http://127.0.0.1:9015/getMatches?&serverName={server}&tournamentName={category}')
    context = resp.text
    return context
def getServerPlayerInfoAPI(ctx, player):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    player = str(player).replace("#","%23")
    resp = requests.get(f'http://127.0.0.1:9015/getServerPlayerInfo?&serverName={server}&tournamentName={category}&playerName={player}')
    context = resp.text
    return context
def getServerPlayerInfoByNameAPI(ctx, name):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)


    playerName = name.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/getServerPlayerInfo?&serverName={server}&tournamentName={category}&playerName={playerName}')
    context = resp.text
    return context
def getTeamMatchesAPI(ctx, teamName):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    teamName = teamName.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/getTeamMatches?&serverName={server}&teamName={teamName}&tournamentName={category}')
    context = resp.text
    return context
def getTeamRosterAPI(ctx, teamName):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    teamName = teamName.replace("#","%23")

    resp = requests.get(f'http://127.0.0.1:9015/getTeamRoster?&serverName={server}&teamName={teamName}&tournamentName={category}')
    context = resp.text
    return context


def genServerAPI(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    serverList = requests.get(f'http://127.0.0.1:9015/getServers')
    serverList = strToList(serverList.text)
    if server.name not in serverList:
        userName = str(user.name).replace("#","%23")
        serverName = str(server.name).replace("#","%23")
        resp = requests.get(f'http://127.0.0.1:9015/genServer?user={userName}&serverName={serverName}')
        return resp.text

def getServerReadyAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    resp = str(requests.get(f'http://127.0.0.1:9015/getServerExist?&serverName={server}').text)
    resp = resp.strip('"')
    #print(resp)
    if resp == 'f':
        #print("First Check Failed")
        return False
    #print("first Check Success")

    #print("Second Check is running")
    resp = str(requests.get(f'http://127.0.0.1:9015/getServerReady?&serverName={server}').text)
    resp = resp.strip('"')
    #print(resp)
    if resp == "t":
        return True
    else:
        return False


def enableServerAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild.name)
    category = str(ctx.channel.category.name)
    print(user)
    print(server)
    resp = requests.get(f'http://127.0.0.1:9015/readyServer?&user={user}&serverName={server}')
    context = resp.text
    return context

def genTournamentAPI(ctx, name):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)

    resp = requests.get(f'http://127.0.0.1:9015/genTournament?user={user}&serverName={server}&tournamentName={name}')
    context = resp.text
    return context

def getConfigAPI(ctx):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    resp = requests.get(f'http://127.0.0.1:9015/getConfig?&serverName={server}')
    context = strToDict(resp.text)
    return context

def getConfigTournamentAPI(ctx, tournamentName):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    resp = requests.get(f'http://127.0.0.1:9015/getConfigTournament?&tournamentName={tournamentName}&serverName={server}')
    context = strToDict(resp.text)
    return context

def registerIdAPI(ctx, roleName, id):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    id = str(id)
    resp = requests.get(f'http://127.0.0.1:9015/registerRole?&serverName={server}&roleName={roleName}&id={id}')

def registerIdTournamentAPI(ctx, tournamentName, roleName, id):
    user = str(ctx.author).replace("#","%23")
    channel = str(ctx.channel)
    server = str(ctx.guild)
    category = str(ctx.channel.category.name)
    id = str(id)
    resp = requests.get(f'http://127.0.0.1:9015/registerRoleTournament?&tournamentName={tournamentName}&serverName={server}&roleName={roleName}&id={id}')


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
def enableError():
    return "This Server Has not been Enabled by an Admin, see /get_started"

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

def getMember(members, name):
    for x in members:
        if f"{x.name}#{x.discriminator}" == name:
            return x
def getRole(serverRoles, roleName):
    for x in serverRoles:
        if x.name == roleName:
            return x
    return None
def getChannel(category, channelName):
    for x in category.text_channels:
        if x.name == channelName:
            return x
    return None
def getCategory(server, categoryName):
    for x in server.categories:
        if x.name == categoryName:
            return x
    return None
def ifMemberHasRole(roles, role: discord.role):
    for x in roles:
        if x == role:
            return True
    return False
async def addRole(member: discord.member, role: discord.role):
    await member.add_roles(role)
async def removeRole(member: discord.member, role: discord.role):
    await member.remove_roles(role)



@bot.event
async def on_guild_join(guild):
    #This doesn't Work
    #print("Join Server")
    #adminRole = await guild.create_role(name=f"Tournament Admin", mentionable=True)
    pass

@bot.slash_command(description="Test")
async def test(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category





    #serverRoles = server.roles
    #member = getMember(server.members, "TheBetterNick#5462")
    #role = getRole(serverRoles, "ranch-mncs")
    #print(member.roles)

    #await addRole(member, role)
    #await removeRole(member, role)
    #print(member.roles)


    #print(getConfigTournamentAPI(ctx, category))
    #registerIdTournamentAPI(ctx, category, "test", 7890)
    #print(getConfigTournamentAPI(ctx, category))
    #getServerReadyAPI(ctx)
    #print(type(getServerReadyAPI(ctx)))
    #print(getServerReadyAPI(ctx))

    await ctx.send_response("pong", ephemeral=True)


@bot.slash_command()
async def test3(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category

    category = getCategory(server, "Tournament Administration")
    print(getChannel(category,"bot-commands-admin"))

    
        


#Setup Commands
@bot.slash_command(description="Check to see if your server has been enabled or not, True or False")
async def server_ready(ctx):
    await ctx.send_response(getServerReadyAPI(ctx), ephemeral=True)
class enableServerView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    def __init__ (self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(label="ENABLES BOT", style=discord.ButtonStyle.danger)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message(enableServerAPI(self.ctx), ephemeral=True) # Send a message when the button is clicked
@bot.slash_command(description="Allows commands to be run by the the bot. Can only be run by admins")
async def enable_server(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category

    genServerAPI(ctx)

    if user.guild_permissions.administrator:
        if not getServerReadyAPI(ctx):
            await ctx.send_response("DON'T RUN UNTIL YOU HAVE UPDATED THE SERVER INTEGRATIONS. see /get_started for details", ephemeral=True, view=enableServerView(ctx))
        else:
            await ctx.send_response("Server is already enabled", ephemeral=True)


@bot.slash_command(description="What you need to do to enable the bot and get it running")
async def get_started(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category
    serverRoles = server.roles



    if user.guild_permissions.administrator:
        #Creates server file structure if it doesn't exist
        genServerAPI(ctx)

            
        usedCategories = server.categories
        usedCategoriesNames = []
        for x in usedCategories:
            usedCategoriesNames.append(x.name)

        if "Tournament Administration" not in usedCategoriesNames:
            adminRole = await server.create_role(name=f"Tournament Admin", mentionable=True)
            category = await server.create_category(name="Tournament Administration")
            adminChannel = await category.create_text_channel("bot-commands-admin")

            vc = await category.create_voice_channel("vc")

            #registerIdAPI(ctx, adminRole.name, adminRole.id)
            #registerIdAPI(ctx, adminChannel.name, adminChannel.id)

            await category.set_permissions(adminRole, view_channel=True)
            await category.set_permissions(server.self_role, view_channel=True)
            await category.set_permissions(server.default_role, view_channel=False)

            await adminChannel.set_permissions(adminRole, view_channel=True)
            await adminChannel.set_permissions(server.self_role, view_channel=True)
            await adminChannel.set_permissions(server.default_role, view_channel=False)

            await vc.set_permissions(adminRole, view_channel=True)
            await vc.set_permissions(server.self_role, view_channel=True)
            await vc.set_permissions(server.default_role, view_channel=False)


            botCommands = adminChannel
        else:
            adminRole = getRole(serverRoles,"Tournament Admin")
            category = getCategory(server, "Tournament Administration")
            botCommands = getChannel(category, "bot-commands-admin")

        text = f"""
Welcome to Tournament Bot

**The Role {adminRole.mention} and Category {category.mention} should have been created **


Things to do
    1. Set integration Permissions
        - Go to Server Settings and then integrations
        - Click on this bot

        - Under Roles & Members set @everyone to False
        - Add role {adminRole.mention} and set to True
            - This role can run the bots important commands, dont let this role fall into the wrong hands
            - You might want to more this role further up the role list

        - Under Channels set All Channels to False
        - Add the channel <#{botCommands.id}> and set to True

        - Under Commands click /help
        - make @everyone True
        - make all channels True

        - It will say not synced and thats ok, clicking sync will undo your changes

        - Now only members with the role {adminRole.mention} and in the channel <#{botCommands.id}> can run all of the administration commands
        - Make sure to add the people who need access, including yourself


    2. Enable Server
        - Next thing to do is enable your server
        - This will allow the running of /commands other then the set-up commands
        - You need to set integration permissions otherwise anyone can start generating tournaments which would result in a shit show
        - Run /enable_server in any channel


    3. Generate your First Tournament
        - Congratulations on getting the bot working
        - Next Run /new tournament in <#{botCommands.name}>, it will get you started from there
    

    4. Have Fun and TO better
    """

        await ctx.send_response(text, ephemeral=True)
    else:
        await ctx.send_response("Admin only command", ephemeral=True)
 

new_group = discord.SlashCommandGroup("new", "For new Tournaments and such")
sync_group = discord.SlashCommandGroup("sync", "For new Tournaments and such")


@bot.slash_command(description="Help for those in need, not very useful though")
async def help(ctx, show: bool = False):
    show = not show

    text = f"""
It looks like you need help.

- Starting Out
    See /get_started if you starting out on a new server, you need to be an admin though

- Player
    as a player you have access to all of the /get commands, use them to find information on what ever you need
    if you have access to other commands then something went terribly wrong, please contact an admin imitatively

- Admin
    see /get_started for initial set up and that should prompt you on what to do next
    Other than that play around with the bot and see what you can do
        If something is not self explanatory then contact TheBetterNick#5462 and he will try his best to fix something

- Bug or error  
    First make sure you spelt everything correctly, that will cause most errors

    Somethings that will brick your bot will be using banned characters like  '  or  "  in the name of anything, blame json not me
        This will likely be fixed later down the line, I need to sleep too

    Make sure you are running the commands in the right bot command channel
    tournament specific commands can only be run in there own bot channel
    administration commands can only be run in the admin channel of there respective tournament

    Do not rename the category as it will break you tournament


    
    
    
    """

    await ctx.send_response(text, ephemeral=show)

@new_group.command(description="Allows commands to be run by the the bot. Can only be run by admins")
async def tournament(
    ctx, 
    tournament_name: discord.Option(discord.SlashCommandOptionType.string, description="""Name of Tournament, DO NOT USE  '  or  "  IN THE NAME, recommended that you keep this short"""),
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        user = ctx.author
        channel = ctx.channel
        server = ctx.guild
        category = channel.category
        serverRoles = server.roles

        if "'" in tournament_name or '"' in tournament_name:
            ctx.send_response("""Don't Use the characters  "  or  '  in any names, it will break shit""", ephemeral=show)
            return None

        #Gets a list of categories
        usedCategories = server.categories
        usedCategoriesNames = []
        for x in usedCategories:
            usedCategoriesNames.append(x.name)
        
        if tournament_name not in usedCategoriesNames:

            #Makes file structure in database
            genTournamentAPI(ctx, tournament_name)

            #Creates League Role
            leagueRole = await server.create_role(name=f"{tournament_name}") # for general participents

            #Registers League Role
            #registerIdTournamentAPI(ctx, category, leagueRole.name, leagueRole.id)

            #Makes category
            category = await server.create_category(name=tournament_name)

            # add default pers so only people with league role
            adminChannel = await category.create_text_channel(f"bot-admin-{tournament_name}")

            #Creates Generic Channels
            general = await category.create_text_channel("general")
            bot_commands = await category.create_text_channel(f"bot-commands-{tournament_name}")

            vibes = await category.create_voice_channel("vibes")

            #config = getConfigAPI(ctx)
            adminRole = getRole(serverRoles, "Tournament Admin")

            #Applies Permissions
            
            await category.set_permissions(adminRole, view_channel=True)
            await category.set_permissions(leagueRole, view_channel=True)
            await category.set_permissions(server.self_role, view_channel=True)
            await category.set_permissions(server.default_role, view_channel=False)
            

            await user.add_roles(adminRole, atomic=True)
            await adminChannel.set_permissions(adminRole, view_channel=True)
            await adminChannel.set_permissions(leagueRole, view_channel=False)
            await adminChannel.set_permissions(server.self_role, view_channel=True)
            await adminChannel.set_permissions(server.default_role, view_channel=False)

            teamRole = await server.create_role(name=f"{'free'}-{category}") # for general participents
            #registerIdTournamentAPI(ctx, category, teamRole.name, teamRole.id)
            addServerTeamAPI(ctx, "free")

            

            text = f"""
<@{user.id}>
Welcome to the tournament, there are just a few thing you need to to before you can get rolling

Things to do
    1. Set integration Permissions
        - Go to Server Settings and then integrations
        - Click on this bot

        - Under Channels add new
        - Add the channel <#{adminChannel.id}> and set to True

        - Scroll Down to Commands and find /get
        - Click and add the channel <#{bot_commands.id}>
        - Set to True - DO NOT CLICK SYNC, YOU WILL HAVE TO REDUE THIS STEP

    Your all finished, it wasn't that bad.

Things to Do Next   
    Look at /add new to start setting up your tournament
        I would start with the players

    /edit will let you edit player's profiles

    /add team player will assign a player to a team

    /get is all of the commands for looking though the database
        - all people with the {leagueRole.mention} role can use these

Things to not do
    Do not rename the category as it will break you tournament
    Do not use the characters  '  "  at any point,  #  can only be used in discord or player names


If something breaks, pint "TheBetterNick#5462" and he will try his best to fix it,
            
This bot is still in its V1 release so if you see any bugs or think of any features that can be added, then please do tell via github
github - https://github.com/Waffleer/Tournament-Discord-Bot
            
            """

            
            await adminChannel.send(text)
            await ctx.send_response("The league has been created, head over to the admin channel to see what to do next", ephemeral=show)
            
            #except:
            #    await ctx.respond("The league has been created, head over to the admin channel to see what to do next", ephemeral=show)
        
        else:
            await ctx.send_response("This league Name is already in use", ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)




#Generic Smaller Commands Below
move_group = discord.SlashCommandGroup("move", "All move related Commands")

get_group = discord.SlashCommandGroup("get", "All Get Commands")
team_group = get_group.create_subgroup("team", "Commands related to get team")
player_group = get_group.create_subgroup("player", "Commands related to get player")

remove_group = discord.SlashCommandGroup("remove", "Commands related to removing")
add_group = discord.SlashCommandGroup("add", "Commands related to get adding")

add_team_group = add_group.create_subgroup("team", "Commands related to add team")
add_new_group = add_group.create_subgroup("new", "Commands related to add team")
remove_team_group = remove_group.create_subgroup("team", "Commands related to remove team")

edit_group = discord.SlashCommandGroup("edit", "Commands related to editing")
edit_player_group = edit_group.create_subgroup("player", "Commands related to editing player")



class playerOption(discord.Option):
    def __init__(self):
        super().__init__(discord.SlashCommandOptionType.string, description="Name of Registered Player")
class teamOption(discord.Option):
    def __init__(self):
        super().__init__(discord.SlashCommandOptionType.string, description="Name of Registered Team")
class discordUserOption(discord.Option):
    def __init__(self):
        super().__init__(discord.SlashCommandOptionType.string, description="Discord username with tag   Example - 'TheBetterNick#5462'")

"""
@.command(description="")
async def (ctx, show: bool = False):
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(, ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
"""

#Edit player
@edit_player_group.command(description="Edits the rank of the player")
async def rank(
    ctx, 
    player_name: playerOption(),
    rank: discord.Option(discord.SlashCommandOptionType.string, description="Competitive Rank of Player"),
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(editServerPlayerRankAPI(ctx, player_name, rank), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@edit_player_group.command(description="Edits the age of the player")
async def age(
    ctx, 
    player_name: playerOption(),
    age: discord.Option(discord.SlashCommandOptionType.string, description="Age of Player"),
    show: bool = False
    ):
    
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(editServerPlayerAgeAPI(ctx, player_name, age), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@edit_player_group.command(description="Edits the role of the player")
async def role(
    ctx, 
    player_name: playerOption(),
    role: discord.Option(discord.SlashCommandOptionType.string, description="Role in team of Player"),
    show: bool = False
    ):
    
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(editServerPlayerRoleAPI(ctx, player_name, role), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@edit_player_group.command(description="Edits the discord username of the player")
async def discord_username(
    ctx, 
    player_name: playerOption(),
    discord_username: discordUserOption(),
    show: bool = False
    ):
    
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(editServerPlayerDiscordNameAPI(ctx, player_name, discord_username), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@edit_player_group.command(description="Edits all of the information of a player")
async def all(
    ctx, 
    player_name: playerOption(),
    rank: discord.Option(discord.SlashCommandOptionType.string, description="Competitive Rank of Player"),
    age: discord.Option(discord.SlashCommandOptionType.string, description="Age of Player"),
    role: discord.Option(discord.SlashCommandOptionType.string, description="Role in team of Player"),
    discord_username: discordUserOption(),
    show: bool = False
    ):
    
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(editServerPlayerCompleteAPI(ctx, player_name, rank, age, role, discord_username), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)

#Remove Commands
@remove_group.command(description="Removes a match from database")
async def match(
    ctx, 
    match_id: discord.Option(discord.SlashCommandOptionType.string, description="ID of a match, can be obtained via /get team matches, /get matches, or when you create a match"), 
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(removeMatchAPI(ctx, match_id), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)

#Add Commands
@add_new_group.command(description="Adds a match to database, ")
async def match(
    ctx, 
    date: discord.Option(discord.SlashCommandOptionType.string, description="dd/mm/year format"), 
    time: discord.Option(discord.SlashCommandOptionType.string, description="hour:minute format - military time"), 
    team_one: discord.Option(discord.SlashCommandOptionType.string, description="Team Name that has been registered"), 
    team_two: discord.Option(discord.SlashCommandOptionType.string, description="Team Name that has been registered"), 
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(addMatchAPI(ctx, date, time, team_one, team_two), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@add_new_group.command(description="Adds a new player to database")
async def player(
    ctx,
    player_name: playerOption(),
    discord_username: discordUserOption(),
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        server = ctx.guild
        member = getMember(server.members, discord_username)
        role = getRole(server.roles, str(ctx.channel.category))
        await addRole(member, role)
        
        await ctx.send_response(addServerPlayerAPI(ctx, player_name, discord_username), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@add_new_group.command(description="")
async def team(
    ctx,
    team_name: teamOption(),
    show: bool = False
    ):

    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category
    serverRoles = server.roles

    show = not show

    if getServerReadyAPI(ctx):
        teamRole = await server.create_role(name=f"{team_name}-{category}") # for general participents
        #registerIdTournamentAPI(ctx, category, teamRole.name, teamRole.id)

        #Creates Channels

        
        teamGeneral = await category.create_text_channel(f"{team_name}-private")
        vc = await category.create_voice_channel(f"{team_name}-private")

        adminRole = getRole(serverRoles, "Tournament Admin")

        await teamGeneral.set_permissions(adminRole, view_channel=True)
        await teamGeneral.set_permissions(teamRole, view_channel=True)
        await teamGeneral.set_permissions(server.self_role, view_channel=True)
        await teamGeneral.set_permissions(server.default_role, view_channel=False)

        await vc.set_permissions(adminRole, view_channel=True)
        await vc.set_permissions(teamRole, view_channel=True)
        await vc.set_permissions(server.self_role, view_channel=True)
        await vc.set_permissions(server.default_role, view_channel=False)


        await ctx.send_response(addServerTeamAPI(ctx, team_name), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)

#Remove Team Commands


#Move Commands
@move_group.command(description="Moves player to team")
async def player(
    ctx, 
    player_name: playerOption(),
    team_name: teamOption(),
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        server = ctx.guild
        category = ctx.channel.category
        serverRoles = server.roles
        player = strToDict(getServerPlayerInfoAPI(ctx, player_name))
        member = getMember(server.members, player["discordName"])

        #print(member)
        #print(type(player))
        #print(player['team'])

        #print(getRole(serverRoles, f"{player['team']}-{category}"))

        await removeRole(member, getRole(serverRoles, f"{player['team']}-{category}"))
        await addRole(member, getRole(serverRoles, f"{team_name}-{category}"))

        removeTeamPlayerAPI(ctx, player_name, str(player['team']))

        await ctx.send_response(addTeamPlayerAPI(ctx, player_name, team_name), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)


#Generic Get Commands
@get_group.command(description="Returns all matches in database, see /get team matches for more information")
async def matches(ctx, show: bool = False):
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(getMatchesAPI(ctx), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@get_group.command(description="Returns all Players in database")
async def players(ctx, show: bool = False):
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(getPlayersAPI(ctx), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@get_group.command(description="Returns all Teams in database")
async def teams(ctx, show: bool = False):
    show = not show
    print(getServerReadyAPI(ctx))
    if getServerReadyAPI(ctx):
        await ctx.send_response(getTeamsAPI(ctx), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)


#Player Commands
@player_group.command(description="Returns Player Information")
async def info(
    ctx,
    player_name: playerOption(), 
    show: bool = False
    ):
    
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(getServerPlayerInfoAPI(ctx, player_name), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
#Team commands
@team_group.command(description="Returns all of the matches for a Team")
async def matches(
    ctx, 
    team_name: teamOption(), 
    show: bool = False
    ):

    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(getTeamMatchesAPI(ctx, team_name), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)
@team_group.command(description="Returns all of the Players on a Specified Team")
async def roster(
    ctx, 
    team_name: teamOption(), 
    show: bool = False
    ):
    
    show = not show
    if getServerReadyAPI(ctx):
        await ctx.send_response(getTeamRosterAPI(ctx, team_name), ephemeral=show)
    else:
        await ctx.send_response(enableError(), ephemeral=show)


#Doesn't Work
#@bot.event
async def on_guild_join(guild):
    pass

#For testing interactions
#@bot.slash_command()
async def test4(ctx):
    user = ctx.author
    channel = ctx.channel
    server = ctx.guild
    category = channel.category

    integrations = await ctx.guild.integrations()
    print(type(integrations))
    print(type(integrations[0]))

    await ctx.send_response(integrations, ephemeral=False)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


bot.add_application_command(get_group)
bot.add_application_command(add_group)
bot.add_application_command(remove_group)
bot.add_application_command(edit_group)
bot.add_application_command(new_group)
bot.add_application_command(move_group)



from secrets import TOKEN
bot.run(TOKEN)