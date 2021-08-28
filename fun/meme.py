from main_imports import *

class Meme(commands.Cog, name='Meme'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
          embed = discord.Embed(title="", description="")

          async with aiohttp.ClientSession() as cs:
              async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                  res = await r.json()
                  embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                  await ctx.send(embed=embed)
          
    @meme.error
    async def command_name_error(self, ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
              embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
              await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Meme(bot))
  print ("Meme is up")