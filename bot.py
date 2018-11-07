import os, discord
from discord.ext import commands

TOKEN = os.environ['token']
bot = commands.Bot(command_prefix='s~')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run(TOKEN)
