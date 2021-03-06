import os, discord
from discord.ext import commands

PREFIX = 's~'
TOKEN = os.environ['token']
bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	await bot.change_presence(activity=discord.Game(name=PREFIX + 'help'))


@bot.command()
async def ping(ctx):
    '''
    Get the latency of the bot.
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(bot.user.name + "\'s latency is: " + str(latency))

@bot.command()
async def store(ctx, label:str, *, data:str):
	'''
	Store data. [WIP]
	s~store [data label] [data to store]
	'''
	print('label: ' + label + '\ndata: ' + data)
	fileName = str(ctx.message.guild) + ".txt"
	spaceCount = fileName.count(" ")
	fileName = fileName.replace(" ", "_", spaceCount)
	await ctx.send(fileName)
	os.chroot("DataStorageFun/Storage")
	os.system("type nul > " + fileName)
	print(os.listdir("DataStorageFun/Storage"))
	
bot.run(TOKEN)
