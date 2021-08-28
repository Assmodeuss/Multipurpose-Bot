from main_imports import *

class Wife(commands.Cog, name='Wife'):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wife(self, ctx):
        wives = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20 - But youre gayyyyyyyyyy!')
        wive =discord.Embed(color=0xdfab4d, timestamp=ctx.message.created_at)
        wive.add_field(name=f'{ctx.message.author}', value=f'Answer: {random.choice(wives)}')
        await ctx.send(embed=wive)

    @wife.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Wife(bot))
  print ("Wife is up")