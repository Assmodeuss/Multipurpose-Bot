from main_imports import *
import topgg

class top(commands.Cog, name='top'):

    def __init__(self, bot):
        self.bot = bot
    
    dbl_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgwNTEyMzMzMTYxODYzNTgxNiIsImJvdCI6dHJ1ZSwiaWF0IjoxNjE5ODc1OTQzfQ.AhW_vG9CJ8EQnL6e6f59Bk7DUVeGQPRDUaNRlFdLfw0'  # set this to your bot's Top.gg token
    self.bot.topggpy = topgg.DBLClient(bot, dbl_token, autopost=True, post_shard_count=True)

    @commands.Cog.listener()
    async def on_autopost_success(self):
            print(f'Posted server count ({bot.topggpy.guild_count}), shard count ({bot.shard_count})')



def setup(bot):
  bot.add_cog(report(top))
  print ("top is up")