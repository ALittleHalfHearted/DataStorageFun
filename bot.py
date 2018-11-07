import os, discord
from discord.ext import commands

#TOKEN = os.environ['token']
client = commands.Bot(command_prefix='s~')

@client.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="--Insert-Game-name-here--"))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user: # this is to prevent crashing via infinite loops
        return
      
      #conditional branches for commands go below here
      
      if message.content.startswith('!hello'): # a simple hello Command
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

bot.run('NTA3OTg3NDIxODc5NTk5MTQ0.DsTNrw.THFXaWPesJkagcT7cxhCEgKiGgU')#TOKEN)
