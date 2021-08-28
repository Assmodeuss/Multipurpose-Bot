from main_imports import *

class Ban(commands.Cog, name='Ban'):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def ban(sels, ctx, member : discord.Member, *, reason=None):
      embed = discord.Embed(color=0xdfab4d)
      embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/805123331618635816/056d84bb0da1079298d42fcb68e26063.webp?size=2048')
      embed.add_field(name="User ID:-", value=f"{member.id}", inline=False)
      embed.add_field(name="User:-", value=f"{member.mention} / {member.name}", inline=False)
      embed.add_field(name="Reason:-", value=reason, inline=False)
      embed.add_field(name="Banned By:-", value=f"{ctx.author.mention}", inline=False)
      embed.add_field(name="Duration:-", value="Eternity", inline=False)
      embed.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")
      await member.ban(reason=reason)
      await ctx.send(embed=embed)
      await ctx.message.delete()
#unban
      @commands.command()
      @commands.has_permissions(ban_members = True)
      async def unban(seld, ctx, *, member,):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        embed = discord.Embed(color=0xdfab4d)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/826823226968899584/854332949491089418/hehe.png')
        embed.add_field(name="User ID:-", value=f"{member.id}", inline=False)
        embed.add_field(name="User:-", value=f"{member.mention} / {member.name}", inline=False)
        embed.add_field(name="Un-Banned By:-", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")

        for ban_entry in banned_users:
          user = ban_entry.user

          if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return

def setup(bot):
  bot.add_cog(Ban(bot))
  print ("Ban/Unban is up")