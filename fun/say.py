from main_imports import *

class Say(commands.Cog, name='Say'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def say(self, ctx, *, output):
          if "@everyone" in ctx.message.content.lower():
            return await ctx.send(f"{ctx.author.mention}, you are not allowed to mention `everyone` with that command.")
          elif "@here" in ctx.message.content.lower():
            return await ctx.send(f"{ctx.author.mention}, you are not allowed to mention `here` with that command.")
          elif "@" in ctx.message.content.lower():
            return await ctx.send(f"{ctx.author.mention}, you're not allowed to mention a role/ping a member with this command.")
          else:
            await ctx.send(output)
            await ctx.message.delete()

def setup(bot):
  bot.add_cog(Say(bot))
  print ("Say is up")