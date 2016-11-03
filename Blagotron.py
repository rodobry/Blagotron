import discord
import asyncio
import json
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#specify which extensions load when the bot starts up
startup_extensions = ["rng", "joke", "lol", "hearthstone", "searches"]

#Bot description
description = '''Blagotron is a bot used in private discord server'''

#Prefix of the commands to call the bot
bot = commands.Bot(command_prefix='/', description=description)

try:
    keyWords = json.load(open('keyWords.json'))
except Exception as e:
    keyWords = {}

def is_owner_check(message):
    return message.author.id == '132914536700182528'
def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

@bot.event
async def on_ready():
    print('Connected as')
    print(bot.user.name)
    print(bot.user.id)
    print("Discord version : {}".format(discord.__version__))
    print('------')

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc ='{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command(hidden=True)
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.command(hidden=True)
@is_owner()
async def shutdown():
    await bot.say(":robot: sHuTtInG dOwN :robot: ")
    await bot.close()

@bot.command(hidden=True)
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def join(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def say(*args):
    msg = ' '.join(args)
    await bot.say(msg)

@bot.command(no_pm=True)
@is_owner()
async def add_keyword(*args):
    """adds keyphrase/response to be checked
       parameters should be add_keyword <string of words> : <response of words>
       notice the space before and after the ':'
       """
    if ':' not in args:
        await bot.say("input should be 'add_keyword <string of words> : <response of words>'\nmake sure there is a space before and after the ':'")
        return
    index = args.index(':')
    keyphrase = args[:index]
    response = args[index+1:]
    keyWords.update({(' '.join(keyphrase)).lower():' '.join(response)})
    with open('keyWords.json', 'w') as fp:
        json.dump(keyWords, fp,indent=4)
    await bot.say("Added key '{}' with response '{}'".format((' '.join(keyphrase)).lower(),' '.join(response)))

@bot.command()
@is_owner()
async def list_keywords():
    msg = "keys:"
    i = 0
    for key in keyWords.keys():
        msg = msg + '\n' + str(i) + ": " + str(key)
        i += 1
        if len(msg) >= 1500:
            await bot.whisper(msg)
            msg = "\n"
    await bot.whisper(msg)


@bot.command(no_pm=True)
@is_owner()
async def remove_keyword(*args):
    """removes keyword phrase from keywords"""
    keyphrase = (' '.join(args)).lower()
    try:
        del keyWords[keyphrase]
    except KeyError as e:
        await bot.say("'{}' not in list of keywords".format(keyphrase))
    else:
        with open('keyWords.json', 'w') as fp:
            json.dump(keyWords, fp,indent=4)
        await bot.say("removed: " + keyphrase)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() in keyWords:
        await bot.send_message(message.channel, keyWords[message.content.lower()])

    await bot.process_commands(message)

bot.run('MjE1MjA4MzU2NjkwOTE5NDI0.CrblxQ.4gP1i71BwgSv0z9ld1yOSAVRe9E')