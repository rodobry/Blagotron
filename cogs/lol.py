import random
import cassiopeia as cass
from cassiopeia import Champion, Champions, Summoner, ChampionMastery
from discord.ext import commands
import json
try:
    config = json.load(open('data/config.json'))
except Exception as e:
    config = {}

class LOL():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def summinfo(self, ctx, name : str, region : str):
        """Get informations on a summoner"""
        summoner = Summoner(name=name, region=region)
        await self.bot.say("Name : {0}\n ID: {1}\n Account ID: {2}\n Level: {3}\n Profil icon : {4}".format(summoner.name,summoner.id,summoner.account.id,summoner.level,summoner.profile_icon.url))

    @commands.command(pass_context=True)
    async def champmastery(self, ctx, name : str, region : str):
        """Get champions masteries of a summoner"""
        summoner = Summoner(name=name, region=region)
        sid=summoner.id
        summoner = Summoner(name=name,region=region,id=sid)
        cms = cass.get_champion_masteries(summoner=summoner, region=region)
        cms = summoner.champion_masteries
        await self.bot.say("Highest mastery score : {}".format(cms[0].points))
        pro = cms.filter(lambda cm: cm.level >= 5)
        await self.bot.say("{} has mastery level 5 or higher on:".format(summoner.name))
        await self.bot.say([cm.champion.name for cm in pro])

def setup(bot):
    bot.add_cog(LOL(bot))
