import random
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy, StatSummaryType
from discord.ext import commands
import json
try:
    config = json.load(open('data/config.json'))
except Exception as e:
    config = {}

riotapi.set_region(config["riot-region"])
riotapi.set_api_key(config["riot-api"])

class LOL():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randchamp(self):
        """Get a random LoL champion"""
        champions = riotapi.get_champions()
        random_champion = random.choice(champions)
        await self.bot.say(random_champion)

    @commands.command(pass_context=True)
    async def kda(self, ctx):
        """Get the KdA of a summoner over his 20 last games"""
        summoner = riotapi.get_summoner_by_name(ctx.message.content[5:])

        match_list = summoner.match_list()

        num_matches = 10
        kills = 0
        deaths = 0
        assists = 0

        await self.bot.say("Calculating K/D/A from the past {0} matches...".format(num_matches))

        for i, match_reference in enumerate(match_list[0:num_matches]):
            match = match_reference.match()
            for participant in match.participants:
                if participant.summoner_id == summoner.id:
                    kills += participant.stats.kills
                    deaths += participant.stats.deaths
                    assists += participant.stats.assists
            kda = (kills+assists)/deaths
        await self.bot.say("Average K/D/A : {0}/{1}/{2} == {3} over past {4} matches".format(kills,deaths,assists, round(kda, 3),num_matches))


def setup(bot):
    bot.add_cog(LOL(bot))
