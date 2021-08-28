from main_imports import *

class Misc(commands.Cog, name='Misc'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'**Pong!** Latency: {round(self.bot.latency * 1000)}ms')
        
    
    @commands.command()
    async def timer(self, ctx, timeInput):
        try:
            try:
                time = int(timeInput)
            except:
                convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
                time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
            if time > 86400:
                await ctx.send("I can\'t do timers over a day long")
                return
            if time <= 0:
                await ctx.send("Timers don\'t go into negatives :/")
                return
            if time >= 3600:
                message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
            elif time >= 60:
                message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
            elif time < 60:
                message = await ctx.send(f"Timer: {time} seconds")
            while True:
                try:
                    await asyncio.sleep(5)
                    time -= 5
                    if time >= 3600:
                        await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                    elif time >= 60:
                        await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
                    elif time < 60:
                        await message.edit(content=f"Timer: {time} seconds")
                    if time <= 0:
                        await message.edit(content="Ended!")
                        await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
                        break
                except:
                    break
        except:
            await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")

    @commands.command()
    async def poll(self, ctx, question, option1=None, option2=None):
          emb = discord.Embed(title=f" Poll by {ctx.message.author} ", description=f" {question} ?\n**<a:verified:822163811217309728> = {option1}**\n**<a:unverified:822163810580037694> = {option2}**")
          if option1==None and option2==None:
            await ctx.channel.purge(limit=1)
          message = await ctx.send(embed=emb)
          await message.add_reaction('<a:unverified:822163810580037694>')
          await message.add_reaction('<a:verified:822163811217309728>')

      #embed
    @commands.command()
    async def embed(self, ctx, *, message):
          emb = discord.Embed(description=f"{message}",color=0xdfab4d)
          await ctx.send(embed=emb)
          await ctx.message.delete()
    
    @commands.command()
    async def servers(self, ctx):
      await ctx.send(f"{len(self.bot.guilds)}")
    @commands.command()
    @commands.is_owner()
    async def members (self, ctx):
      await ctx.send(f"{len(self.bot.users)}")  
      
def setup(bot):
  bot.add_cog(Misc(bot))
  print ("misc is up")