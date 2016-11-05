from discord.ext import commands
import wikipedia
from dataIO import dataIO

config = dataIO.load_json('data/config.json')
wikipedia.set_lang(config["wikilang"])

class Searches():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="You can then run !wiki on a given item returned")
    async def wikisearch(self, *, q: str):
        """Returns a list of wikipedia articles related search term"""
        search_results = wikipedia.search(q)
        # limit bot results to 10 to avoid long messages
        msg = "\n".join(search_results[:10])
        await self.bot.say(msg)

    @commands.command()
    async def wiki(self, *, q: str):
        """Returns a 1 sentence summary and link to wiki article"""
        try:
            page = wikipedia.page(q)
        except wikipedia.exceptions.DisambiguationError:
            await self.bot.say("Could not find Page :(")
        else:
            summary = wikipedia.summary(q, sentences=1)
            msg = "{}\n{}".format(page.url, summary)
            await self.bot.say(msg)

    @commands.command()
    async def wikilang(self, *, q: str):
        """Change the language used for the searches"""
        wikipedia.set_lang(q)
        await self.bot.say("Language changed to {}".format(wikipedia.languages()[q]))

def setup(bot):
    bot.add_cog(Searches(bot))