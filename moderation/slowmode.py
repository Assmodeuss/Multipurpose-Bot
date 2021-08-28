from main_imports import *

class slow(commands.Cog, name='slow'):

    def __init__(self, bot):
        self.bot = bot
    
    def convert(time):
        pos = ["s", "m", "h", "d"]

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]


    @commands.command()
    async def slowmode(self, ctx, amount):
            await ctx.channel.edit(slowmode_delay=int(amount))
            await ctx.send('done')

def setup(bot):
  bot.add_cog(slow(bot))
  print ("slow mode is up")