from main_imports import *

class Help(commands.Cog, name='Help'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, cmd = None):
      if cmd is None:
    #page1    
          page1 = discord.Embed(title="Command Modules Pages",  description="**Perseus**  is a multi-purpose bot that contain many different commands. This is the 1ˢᵗ page of the command  modules I hope you all like the bot ━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d,  timestamp=ctx.message.created_at)
          page1.set_thumbnail(url='https://cdn.discordapp.com/avatars/805123331618635816/056d84bb0da1079298d42fcb68e26063.webp?size=2048')
          page1.add_field(name="<a:doggy:849323553097777252> | **Fun** ", value="- Fun features of the bot", inline=False)
          page1.add_field(name="<:ban2:849322385114398761> | **Moderation**", value="-moderations features of the bot", inline=False)
          page1.add_field(name="<a:music:849323556068261958> | **Music**", value="-music features of the bot", inline=False)
          page1.add_field(name="<a:vibe:849323558479200288> | **Miscellanies**", value="-Extra features of the bot", inline=False)
          page1.add_field(name="<:bot:849323846485540894> | **About**", value="- Bot information", inline=False)
          page1.add_field(name="<a:5625_remspin:853582514614304768> | **NSFW **", value="- NSFW commands ", inline=False)
          page1.add_field(name="<:717373238245589083:837296143540813824>   | **Services**", value="- Chech the last page of this module", inline=False)
          page1.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")

    #page2      
          
          page2 = discord.Embed(title="<a:doggy:849323553097777252> | **Fun Commands**",  description="━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page2.add_field(name="`Flip`", value="-Does a random coin toss")
          page2.add_field(name="`Poll`", value="- Creates a random Poll with 2 options")
          page2.add_field(name="`Say`", value="- Says the message user wish ")   
          page2.add_field(name="`gayrate`", value="- I seriuosly don't know why i added such commands but leeave it nvm the command tells the gay rate of the user")
          page2.add_field(name="`simprate`", value="- As the name suggests the command tells the simp rate of the user")
          page2.add_field(name="`Wife`", value="- Hehe lmao this command tells the number of wifes you will have")
          page2.add_field(name="`Meme`", value="- When the command is run a epic meme is presented")
          page2.add_field(name="`truth`", value="- Gives you a random question")
          page2.add_field(name="`dare`", value="- Gives you a random task")
          page2.add_field(name="`joke`", value="-tells a random joke ")
          page2.add_field(name="`Pat`", value="sends a random patting image or gif it depends on your luck")
          page2.add_field(name="`Nep`", value="For nep lover sends a random NEP NEP")
          page2.add_field(name="`Hug`", value="Sends a random huggy gif/photo")
          page2.add_field(name="`Slap`", value="Sends a random slap gif")
          page2.add_field(name="`Kill`", value="It doesnt kills but sends a killing gif ")
          page2.add_field(name="`sendav`", value="Sends a random avatar")
          page2.add_field(name="`Hentai`", value="Sends a random hentai uncensored pics")
          page2.add_field(name='⁣          ',value='⁣          ')
          page2.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")

    #page3
          page3 = discord.Embed(title="<:ban2:849322385114398761> | **Moderation** Commands",  description="━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page3.add_field(name="**BAN**", value="- bans a member from the server", inline=False)
          page3.add_field(name="**KICK**", value="- kicks a member from the server", inline=False)
          page3.add_field(name="**Purge**", value="- Deletes the amount of messages told ***NOTE*** this is command has a defualt amount set to `5`  ", inline=False)
          page3.add_field(name="**Announce**", value="- Makes an Announcement with everyone as a ghost ping", inline=False)
          page3.add_field(name="**Role**", value="- Add or removes the role from a member", inline=False)
          page3.add_field(name="**Slowmode**", value="- Add slowmode to the current channel `??slowmode <time only in seconds like : 100>`", inline=False)
          page3.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")
        

    #page4

          page4 = discord.Embed(title="<a:music:849323556068261958> | **Music** Commands",  description="━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page4.add_field(name="<a:ezgif:838407263336661012><a:ezgif:838407263336661012>***IMP***<a:ezgif:838407263336661012><a:ezgif:838407263336661012>", value="These commands are currently not available", inline=False)
          page4.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")

    #page5

          page5 = discord.Embed(title="<a:vibe:849323558479200288> | **Miscellanies**",  description="━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page5.add_field(name="**Snipe**", value="- `??snipe` shows the recent deleted message", inline=False)
          page5.add_field(name="`whois`", value="Currently not working <a:ezgif:838407263336661012>", inline=False)
          page5.add_field(name="`Avatar`", value="Currently not working <a:ezgif:838407263336661012>")
          page5.add_field(name="`serverinfo`", value="Currently not working <a:ezgif:838407263336661012>", inline=False)
          page5.add_field(name="**roleinfo**", value="Currently not working <a:ezgif:838407263336661012>", inline=False)
          page5.add_field(name="**emojicount**", value="Currently not working <a:ezgif:838407263336661012>", inline=False)
          page5.add_field(name="**membercount**", value="- As the name tells", inline=False)
          page5.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")

          page5 = discord.Embed(title="<:bot:849323846485540894> | **Developer** Info",  description="━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page5.set_thumbnail(url='https://cdn.discordapp.com/avatars/634343118384398347/913585df59c2a0af713e0b73e091dea4.webp?size=2048')
          page5.add_field(name="`developer info`", value=f'`??devinfo` Currently not working <a:ezgif:838407263336661012>', inline=False)
          page5.add_field(name="`Support Server`", value="- Pls do `??suport` for the servers link!", inline=False)
          page5.add_field(name="`Bot info`", value="Currently not working <a:ezgif:838407263336661012>", inline=False)
          page5.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")

          

          page7 = discord.Embed(title="<a:5625_remspin:853582514614304768>  | **NSFW Commands for your horny guys <a:kek:800638152162148353><a:kek:800638152162148353>** ",  description="━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page7.set_thumbnail(url='https://cdn.discordapp.com/avatars/634343118384398347/913585df59c2a0af713e0b73e091dea4.webp?size=2048')
          page7.add_field(name="Anal", value=f'-`??anal`', inline=False)
          page7.add_field(name="Boobs", value=f'- `??boobs`',   inline=False)
          page7.add_field(name="Porn", value=f'-`??porn`', inline=False)
          page7.add_field(name="Hentai", value=f"- `??hentai`", inline=False)
          page7.add_field(name="Hot", value=f"- `??hot`", inline=False)
          page7.add_field(name='⁣          ', value=f" ● [Support Server](https://discord.gg/sKGE96fzcd) | ● [Invite Me](http://tiny.cc/samuraiinvite) |  ● [Vote Me](https://top.gg/bot/805123331618635816/vote)")


          page8 = discord.Embed(title="<:717373238245589083:837296143540813824>   | **Services by the dev** ",  description="DM the bot owner for plans, Prices may vary regarding the service you choose ━━━━━━━━━━━━━━━━━━━━━━━━", color=0xdfab4d, timestamp=ctx.message.created_at)
          page8.set_thumbnail(url='https://cdn.discordapp.com/avatars/634343118384398347/913585df59c2a0af713e0b73e091dea4.webp?size=2048')
          page8.add_field(name="Server Design", value=f'A complete Make-over of your server with new channels, roles, etc', inline=False)
          page8.add_field(name="Custom Bot", value=f'A custom bot made for you/your server', inline=False)
          page8.add_field(name="Video Editing", value=f'Gaming montage, Advertisments, Tutorials, etc', inline=False)
          page8.add_field(name="Photo Editing", value=f"Video's thumbnail, etc", inline=False)
          page8.set_image(url="https://cdn.discordapp.com/attachments/827235292879519754/857930639990063124/standard_6.gif")

          self.bot.help_pages = [page1, page2, page3, page4, page5, page7, page8]

          buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]
          current = 0
          msg = await ctx.send(embed=self.bot.help_pages[current])  
          
          for button in buttons:
              await msg.add_reaction(button)
              
          while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=120.0)

            except asyncio.TimeoutError:
                return

            else:
                previous_page = current
                if reaction.emoji == u"\u23EA":
                    current = 0
                    
                elif reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1
                        
                elif reaction.emoji == u"\u27A1":
                    if current < len(self.bot.help_pages)-1:
                        current += 1

                elif reaction.emoji == u"\u23E9":
                    current = len(self.bot.help_pages)-1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed=self.bot.help_pages[current])
      else:
        return

def setup(bot):
  bot.add_cog(Help(bot))
  print ("Help is up")