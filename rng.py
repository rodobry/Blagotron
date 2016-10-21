import random
import discord
from discord.ext import commands
from random import randint

class RNG():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices : str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))

    @commands.command(description="Rock Paper Scissors")
    async def rps(self, msg: str):
        """Rock paper scissors. Example : /rps Rock if you want to use the rock."""
        print('Petit pierre feuille ciseaux OKLM')
        # Les options possibles
        t = ["Rock", "Paper", "Scissors"]
        # random choix pour le bot
        computer = t[randint(0, 2)]
        player = msg
        print(msg)
        if player == computer:
            await self.bot.say("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                await self.bot.say("You lose! {0} covers {1}".format(computer, player))
            else:
                await self.bot.say("You win! {0} smashes {1}".format(player, computer))
        elif player == "Paper":
            if computer == "Scissors":
                await self.bot.say("You lose! {0} cut {1}".format(computer, player))
            else:
                await self.bot.say("You win! {0} covers {1}".format(player, computer))
        elif player == "Scissors":
            if computer == "Rock":
                await self.bot.say("You lose! {0} smashes {1}".format(computer, player))
            else:
                await self.bot.say("You win! {0} cut {1}".format(player, computer))
        else:
            await self.bot.say("That's not a valid play. Check your spelling!")

    @commands.command(pass_context=True,description="Commande fabriquée avec l'âme de MuscleF. Dit si quelque chose est bien ou pas.")
    async def mf(self, ctx):
        """Tell you if something is good or not"""
        print ('On tourne la roulette des goûts')
        mf = [
            ":wheel_of_dharma: J'aime bien {} :wheel_of_dharma:".format(ctx.message.content[4:]),
            ":wheel_of_dharma: {} c à chier :wheel_of_dharma:".format(ctx.message.content[4:])
        ]
        await self.bot.say(random.choice(mf))

def setup(bot):
    bot.add_cog(RNG(bot))