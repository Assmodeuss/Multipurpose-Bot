from main_imports import *

class Purge(commands.Cog, name='Purge'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pu'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send("**Cleared `" + str(amount) + "` Messages**", delete_after=1)

    @purge.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)  

def setup(bot):
  bot.add_cog(Purge(bot))
  print ("Purge is up")