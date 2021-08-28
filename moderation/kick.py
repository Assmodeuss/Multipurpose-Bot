from main_imports import *

class Kick (commands.Cog, name='Kick'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members= True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
      embed = discord.Embed(color=0xdfab4d)
      embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/805123331618635816/056d84bb0da1079298d42fcb68e26063.webp?size=2048')
      embed.add_field(name="User ID:-", value=f"{member.id}", inline=False)
      embed.add_field(name="User:-", value=f"{member.mention} / {member.name}", inline=False)
      embed.add_field(name="Kicked By:-", value=f"{ctx.author.mention}", inline=False)
      embed.add_field(name="Reason:-", value=reason, inline=False)
      embed.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")
      await member.kick(reason=reason)
      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(Kick (bot))
  print ("Kick is up")