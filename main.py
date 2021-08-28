from main_imports import *

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('??'), intents=intents)
bot.remove_command('help')
@bot.event
async def on_ready():
    print('The bot is logged in.')
    print('Ready!')
    print('Logged in as ---->', bot.user)
    print('ID:', bot.user.id)

    await bot.change_presence(activity=discord.Game(name=f"Flying Above you..||@perseus help"),status=discord.Status.do_not_disturb)

@bot.event
async def on_guild_join(guild):
  channel = bot.get_channel(827923431084654644)
  emb = discord.Embed(title=f"Ser ver Joined",color=0xdfab4d)
  emb.add_field(name='Server Name', value=f'{guild.name}', inline=False)
  emb.add_field(name='Server ID', value=f'{guild.id}', inline=False)
  emb.add_field(name='Owner ID', value=f'{guild.owner_id}', inline=False)
  emb.add_field(name='Owner name', value=f'<@{guild.owner_id}>', inline=False)
  emb.add_field(name='Link To The server', value=f' https://disboard.org/server/{guild.id} ' , inline=False)
  emb.add_field(name='Server Members', value=f'{guild.member_count}' , inline=False)
  emb.add_field(name='Total Servers', value=f'{len(bot.guilds)}', inline=False)
  await channel.send(embed=emb)

@bot.event
async def on_guild_remove(guild):
  channel = bot.get_channel(836895991252516874)
  emb = discord.Embed(title=f"Server Left",color=0xdfab4d)
  emb.add_field(name='Server Name', value=f'{guild.name}', inline=False)
  emb.add_field(name='Server ID', value=f'{guild.id}', inline=False)
  emb.add_field(name='Owner ID', value=f'{guild.owner_id}', inline=False)
  emb.add_field(name='Owner name', value=f'<@{guild.owner_id}>', inline=False)
  emb.add_field(name='Total Servers', value=f'{len(client.guilds)}', inline=False)
  await channel.send(embed=emb)


extensions=[
            'help.help',
            'fun.gay',
            'fun.meme',
            'fun.simp',
            'fun.tds',
            'fun.wife',
            'fun.flip',
            'fun.say',
            'fun.sendav',
            'anime.hug',
            'anime.kill',
            'anime.nep',
            'anime.pat',
            'anime.slap',
            'botmisc.invite',
            'botmisc.report',
            'botmisc.support',
            'botmisc.vote',
            'botmisc.top',
            'moderation.announce',
            'moderation.ban',
            'moderation.kick',
            'moderation.purge',
            'moderation.role',
            'moderation.slowmode',
            'moderation.warn',
            'nsfw.nsfw',
            'misc.misc1'




]
    
if __name__ == "__main__":
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
        print (f"Error loading {extension}", file=sys.stderr)
        traceback.print_exc()

              
bot.run(os.getenv('TOKEN'))