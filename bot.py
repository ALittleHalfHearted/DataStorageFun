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
	await client.change_presence(game=discord.Game(name="s~"))

@client.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

	
client.run('NTA3OTg3NDIxODc5NTk5MTQ0.DsTNrw.THFXaWPesJkagcT7cxhCEgKiGgU')#TOKEN)
