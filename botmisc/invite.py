from main_imports import *

class invite(commands.Cog, name='invite'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def invite (self, ctx):
      invite = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)

      invite.add_field(name=f'{ctx.message.author}', value=f'Thanks for supporting us by inviting for the bot Follow this link for [invite me](https://discord.com/oauth2/authorize?client_id=805123331618635816&scope=bot&permissions=2147483647)')

      await ctx.send(embed=invite)


def setup(bot):
  bot.add_cog(invite(bot))
  print ("invite is up")