from main_imports import *

class NSFW(commands.Cog, name='NSFW'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def anal(self, ctx):
                embed = discord.Embed(color=0xdfab4d)
                embed.set_image(url=f"{random.choice(open('anal.txt').readlines())}")
            
                await ctx.send(embed=embed)

    @anal.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)
          if isinstance(error, commands.errors.NSFWChannelRequired):
                error = discord.Embed(color=0xdfab4d,title="<:Error:855039538303860747>** Error**<:Error:855039538303860747>",description="You need to make this a __NSFW__ in order to use this command", inline=False)
                error.set_image(url="https://i.imgur.com/oe4iK5i.gif")
                error.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
                await ctx.send(embed=error)

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hentai(self, ctx):
                embed = discord.Embed(color=0xdfab4d)
                embed.set_image(url=f"{random.choice(open('hentai.txt').readlines())}")
            
                await ctx.send(embed=embed)
              
            

    @hentai.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)
          if isinstance(error, commands.errors.NSFWChannelRequired):
                error = discord.Embed(color=0xdfab4d,title="<:Error:855039538303860747>** Error**<:Error:855039538303860747>",description="You need to make this a __NSFW__ in order to use this command", inline=False)
                error.set_image(url="https://i.imgur.com/oe4iK5i.gif")
                error.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
                await ctx.send(embed=error)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def porn(self, ctx):
                embed = discord.Embed(color=0xdfab4d)
                embed.set_image(url=f"{random.choice(open('porn.txt').readlines())}")
                await ctx.send(embed=embed)

    @porn.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)
          if isinstance(error, commands.errors.NSFWChannelRequired):
                error = discord.Embed(color=0xdfab4d,title="<:Error:855039538303860747>** Error**<:Error:855039538303860747>",description="You need to make this a __NSFW__ in order to use this command", inline=False)
                error.set_image(url="https://i.imgur.com/oe4iK5i.gif")
                error.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
                await ctx.send(embed=error)

    @commands.command()
    @commands.is_nsfw()
    async def boobs(self, ctx):
                embed = discord.Embed(color=0xdfab4d)
                embed.set_image(url=f"{random.choice(open('boobs.txt').readlines())}")
            
                await ctx.send(embed=embed)

    @boobs.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)
          if isinstance(error, commands.errors.NSFWChannelRequired):
                error = discord.Embed(color=0xdfab4d,title="<:Error:855039538303860747>** Error**<:Error:855039538303860747>",description="You need to make this a __NSFW__ in order to use this command", inline=False)
                error.set_image(url="https://i.imgur.com/oe4iK5i.gif")
                error.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
                await ctx.send(embed=error)

    @commands.command()
    @commands.is_nsfw()
    async def hot(self, ctx):
                embed = discord.Embed(color=0xdfab4d)
                embed.set_image(url=f"{random.choice(open('hot.txt').readlines())}")
            
                await ctx.send(embed=embed)

    @hot.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)
          if isinstance(error, commands.errors.NSFWChannelRequired):
                error = discord.Embed(color=0xdfab4d,title="<:Error:855039538303860747>** Error**<:Error:855039538303860747>",description="You need to make this a __NSFW__ in order to use this command", inline=False)
                error.set_image(url="https://i.imgur.com/oe4iK5i.gif")
                error.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)", inline=False)
                await ctx.send(embed=error)

def setup(bot):
  bot.add_cog(NSFW(bot))
  print ("NSFW is up")