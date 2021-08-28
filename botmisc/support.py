from main_imports import *

class support(commands.Cog, name='support'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def support(self, ctx):
          if ctx.channel.id == 826818842650083338:
            await ctx.send(' <@&826845945235898418> looks like someone needs your help !!!')
          else :

            support = discord.Embed(color=0xdfab4d)

            support.add_field(name='Support Server', value='join our [support server](https://discord.com/oauth2/authorize?client_id=805123331618635816&scope=bot&permissions=2147483647)')
            await ctx.send(embed=support)


def setup(bot):
  bot.add_cog(support(bot))
  print ("support is up")