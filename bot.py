import os, discord
from discord.ext import commands

#TOKEN = os.environ['token']
client = commands.Bot(command_prefix='s~')

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	#await client.change_presence(game=discord.Game(name="s~"))

@client.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = client.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(client.user.name, "\'s latency is: ", latency)

@client.command()
async def store(ctx, label:str, *, data:str):
	'''
	Store data.
	s~store [data label] [data to store]
	'''
	target = str(ctx.message.guild) + ".txt"
	spaceCount = target.count(" ")
	target = target.replace(" ", "_", spaceCount)
	doc = open(target, "a+")
	await ctx.send(target)
	contents = doc.read()
	await ctx.send(contents)
	#docL = doc.readlines()
	#for i in docL:
	#	await ctx.send(i)
		#if (i == ctx.message.author):
		#	x = i
		#	for x in docL:
		#		if (
	
client.run('NTA3OTg3NDIxODc5NTk5MTQ0.DsTNrw.THFXaWPesJkagcT7cxhCEgKiGgU')#TOKEN)
