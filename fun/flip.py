from main_imports import *

class Flip(commands.Cog, name='Flip'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def flip(self, ctx):
          choices = ["Heads", "Tails"]
          ranflip = random.choice(choices)
          await ctx.send(ranflip)

    @flip.error
    async def command_name_error(self, ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
              embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
              await ctx.send(embed=embed)
    

def setup(bot):
  bot.add_cog(Flip(bot))
  print ("Flip is up")