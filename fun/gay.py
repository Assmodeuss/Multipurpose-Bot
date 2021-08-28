from main_imports import *

class Gay(commands.Cog, name='Gay'):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gayrate(self, ctx):
        gays = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
        gay = discord.Embed(color=0xdfab4d, timestamp=ctx.message.created_at)

        gay.add_field(name=f'{ctx.message.author}', value=f"Gayrate ={random.choice(gays)}%")
        await ctx.send(embed=gay)

    @gayrate.error
    async def command_name_error(self, ctx, error):
          if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=random.choice(open('slow.txt').readlines()),description=f"Try again in {error.retry_after:.2f}s.", color=0xdfab4d)
            await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Gay(bot))
  print ("Gay Rate is up")