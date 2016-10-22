import discord
import asyncio
import random
from discord.ext import commands
#specify which extensions load when the bot starts up
startup_extensions = ["rng", "joke", "lol"]

#Bot description
description = '''Bot destiné à un serveur discord privé, quelques commandes pour le fun actuellement.'''

#Prefix of the commands to call the bot
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Connected as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc ='{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def join(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.command(description="That's not racist I promise")
async def iq():
    """Iq repartition on earth based on skin color"""
    await bot.say('http://img.pr0gramm.com/2016/09/04/738b85ee1098dd59.jpg')



bot.run('API-TOKEN')
