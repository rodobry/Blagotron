import discord
import asyncio
import os
import json
from discord.ext import commands
from dataIO import dataIO
import Checker
import logging
import re

#Load the config file
config = dataIO.load_json('data/config.json')

#Generate a log file
discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.CRITICAL)
log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.FileHandler(filename='Discord.log', encoding='utf-8', mode='w')
log.addHandler(handler)

#specify which extensions load when the bot starts up
startup_extensions = ["cogs.rng", "cogs.joke", "cogs.lol", "cogs.hearthstone", "cogs.searches", "cogs.trivia", "cogs.remindme", "cogs.economy", "cogs.buyrole", "cogs.russianroulette"]

#Bot description
description = '''Blagotron is a bot used in private discord server'''

#Prefix of the commands to call the bot
bot = commands.Bot(command_prefix='/', description=description)

#Check if the Keywords file exists, if not create it
def check_files():
    if not os.path.isfile("data/keyWords.json"):
        test = {}
        print("Creating empty keyWords.json...")
        dataIO.save_json("data/keyWords.json",test)

#Load the keywords file
check_files()
keyWords = dataIO.load_json('data/keyWords.json')

@bot.event
async def on_ready():
    print('Connected as')
    print(bot.user.name)
    print(bot.user.id)
    print("Discord version : {}".format(discord.__version__))
    print('------')
    await bot.change_presence(game=discord.Game(name=config["botgame"]))
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
@Checker.is_owner()
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
@Checker.is_mod_or_admin()
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
    with open('data/keyWords.json', 'w') as fp:
        json.dump(keyWords, fp,indent=4)
    await bot.say("Added key '{}' with response '{}'".format((' '.join(keyphrase)).lower(),' '.join(response)))

@bot.command()
@Checker.is_mod_or_admin()
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
@Checker.is_mod_or_admin()
async def remove_keyword(*args):
    """removes keyword phrase from keywords"""
    keyphrase = (' '.join(args)).lower()
    try:
        del keyWords[keyphrase]
    except KeyError as e:
        await bot.say("'{}' not in list of keywords".format(keyphrase))
    else:
        with open('data/keyWords.json', 'w') as fp:
            json.dump(keyWords, fp,indent=4)
        await bot.say("removed: " + keyphrase)

@bot.command(name='setgame', description='Sets current game. Usage: setgame game', pass_context=True, no_pm=True)
@Checker.is_mod_or_admin()
async def setgame(ctx, status: str):
    """Set the game played by the bot"""
    await bot.change_presence(game=discord.Game(name=status))
    await bot.say("Game set to : **" + status + "**")
    config["botgame"] = status
    dataIO.save_json("data/config.json", config)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msgtest = message.content.lower()
    for a in keyWords:
        regex = re.escape(a)
        if re.search(regex, msgtest):
            match = re.search(regex, msgtest)
            matchsplit = match.group()
            await bot.send_message(message.channel, keyWords[matchsplit])

    await bot.process_commands(message)

bot.run(config["discord-token"])