from main_imports import *

class Role(commands.Cog, name='Role'):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @has_permissions(manage_roles=True)
    async def role(self, ctx, member : discord.Member, role : discord.Role):
        embed1 = discord.Embed(color=0xdfab4d)
        embed1.add_field(name=f"Role Update", value=f"{member.mention} was given {role.mention}", inline=False)
        embed1.add_field(name="⁣          ", value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
        embed2 = discord.Embed(color=0xdfab4d)
        embed2.add_field(name=f"Role Update", value=f"{role.mention} was removed from {member.mention}", inline=False)
        embed2.add_field(name="⁣          ", value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
        if role in member.roles :
          await member.remove_roles(role)
          await ctx.send(embed=embed2)
        else:
          await member.add_roles(role)
          await ctx.send(embed=embed1)

def setup(bot):
  bot.add_cog(Role(bot))
  print ("Role Rate is up")