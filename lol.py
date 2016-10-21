import random
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy, StatSummaryType
from discord.ext import commands

riotapi.set_region("EUW")
riotapi.set_api_key("RGAPI-423fb003-e22b-4064-b4a5-eb091e47a07c")

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

        num_matches = 20
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