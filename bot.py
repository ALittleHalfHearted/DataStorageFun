import os, discord
from discord.ext import commands

#TOKEN = os.environ['token']
bot = commands.Bot(command_prefix='s~')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="--Insert-Game-name-here--"))

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('NTA3OTg3NDIxODc5NTk5MTQ0.DsTNrw.THFXaWPesJkagcT7cxhCEgKiGgU')#TOKEN)
