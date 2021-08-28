from main_imports import *

class nep(commands.Cog, name='nep'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nep(self, ctx):
        embed = discord.Embed(
            title='',
            color=0xdfab4d
          
        )
        embed.set_image(url=random.choice(open('nep.txt').readlines()))


        await ctx.send(embed=embed)
        time.sleep(0.001)
    @nep.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(nep(bot))
  print ("nep is up")