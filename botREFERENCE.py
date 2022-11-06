import discord

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, user, message):
    await ctx.send("hello world")

@bot.slash_command(description="Sends the bot's latency.", name = "hi")
async def hi(ctx, name: str, age: int = 18): #Sets 18 as default age
    await ctx.send(f'Hello {name}, you are {age} years old!')

@bot.user_command() #Creates the command in context of ... "user, message"
async def slap(ctx, user):
    await ctx.send(f'{ctx.author.mention} slaps {user.mention}!')

@bot.user_command() #Creates the command in context of ... "user, message"
async def dumb(ctx, message):
    await ctx.send(f'This message is dumb')


from secrets import TOKEN2
bot.run(TOKEN2)