from main_imports import *

class report(commands.Cog, name='report'):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def report(self, ctx, *, output):
            suggest = client.get_channel(841288177741332500)
            em = discord.Embed(color=discord.Color.green())
            em.title = f"{ctx.author} | User ID: {ctx.author.id}"
            em.description = output
            em.set_footer(text=f"From {ctx.author.guild} | Server ID: {ctx.author.guild.id}", icon_url=ctx.guild.icon_url)
            await suggest.send(embed=em)
            await ctx.message.delete()



def setup(bot):
  bot.add_cog(report(bot))
  print ("report is up")