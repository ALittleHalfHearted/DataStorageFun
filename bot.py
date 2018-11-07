import os, discord
from discord.ext.commands import Bot

#TOKEN = os.environ['token']
client = Bot(command_prefix='s~')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="--Insert-Game-name-here--"))

@client.command(name="exCommand") # 'name' is literaly the name of the command
                                  # this is what you type after the prefix
async def exampleCommand(): # commands can also take paramenters this example takes none
                            # but if it does have paramenter when the command is called it'll need
                            # them or else the command won't work
  
	await client.say("This is an example of a Command Funtion")

client.run('NTA3OTg3NDIxODc5NTk5MTQ0.DsTNrw.THFXaWPesJkagcT7cxhCEgKiGgU')#TOKEN)
