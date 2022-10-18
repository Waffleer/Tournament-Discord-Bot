
import ngrok
from time import sleep
print("BOT Started")
sleep(20)








def get_url():
    client = ngrok.Client("2Em9qVUxZk3yx1YSNMvkJUJtvEj_7fzRn83kik2Q2ssVKWaza")
    public_url = None
    for t in client.tunnels.list():
        public_url = t.public_url

    if(public_url == None):
        return None

    public_url = public_url.split("//")[-1]
    return public_url


public_url = get_url()




# initiates bot
import discord
import discord.ext
from discord.ext import commands #, tasks




TOKEN = "MTAxOTcxOTA1NzE5ODU1OTI2NQ.Gt-hdT.IOJw0OYGOJcZSmUJiwfRbIdzF7IVBxwiUV2xQs"

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
       
        public_url = get_url()
        if(public_url == None):
            await message.channel.send(f'ngrok is not not responsive, so the server is likely not running')
        await message.channel.send(f'The current public IP is :   {public_url}')

client.run(TOKEN)
