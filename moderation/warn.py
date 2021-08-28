from main_imports import *

class Warn(commands.Cog, name='Warn'):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user:discord.User, *, reason: str):
      if not reason:
       await ctx.send("Please provide a reason.", delete_after=5)
      else:
        await ctx.send("User has been warned.", delete_after=5)
        await user.send(f'You have been warned for: {reason}')
        await ctx.message.delete()
        reason = ''.join(reason)
    

def setup(bot):
  bot.add_cog(Warn(bot))
  print ("Warn Rate is up")