from main_imports import *

class announce(commands.Cog, name='announce'):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *args):
        output = ''
        for word in args:
            output += str(word)
            output += ' '
        embed = discord.Embed(title="  <:exclaim:847444972181389332><:exclaim:847444972181389332>  **ANNOUNCEMENT** <:exclaim:847444972181389332><:exclaim:847444972181389332>  ",
                              description=output,
                              color=0xdfab4d)
        embed.set_image(
            url=
            'https://media.discordapp.net/attachments/783319872230129674/784371198188453909/Tw.gif'
        )
        await ctx.send(embed=embed)
        await ctx.send('@everyone ', delete_after=1)
        await ctx.message.delete()

def setup(bot):
  bot.add_cog(announce(bot))
  print ("announce is up")