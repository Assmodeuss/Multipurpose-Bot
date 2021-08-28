from main_imports import *

class vote(commands.Cog, name='vote'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def vote (self, ctx):
            vote = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)

            vote.add_field(name=f'{ctx.message.author}', value=f'Thanks for supporting us by voting for the bot Follow this link for [voting](https://top.gg/bot/805123331618635816/vote)')

            await ctx.send(embed=vote)


def setup(bot):
  bot.add_cog(vote(bot))
  print ("vote is up")