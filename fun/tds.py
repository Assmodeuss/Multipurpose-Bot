from main_imports import *

class tds(commands.Cog, name='tds'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def truth(self, ctx):
        truth = ['When was the last time you lied ?', 'When was the last time you cried?', 'Whats your biggest fear?', 'Whats your biggest fantasy?', 'Do you have any fetishes?' ,'Whats something youre glad your mum doesnt know about you?', 'Have you ever cheated on someone?', 'Whats the worst thing youve ever done?', 'Whats a secret youve never told anyone?', 'Do you have a hidden talent?', 'Who was your first celebrity crush?', 'What are your thoughts on polyamory?', 'Whats the worst intimate experience youve ever had?', 'Whats the best intimate experience youve ever had?', 'Have you ever cheated in an exam?', 'Whats the most drunk youve ever been?', 'Have you ever broken the law?', 'Whats the most embarrassing thing youve ever done?', 'Whats your biggest insecurity?', 'Have you ever stayed friends with someone because it benefitted you beyond just the friendship?', 'Whats the biggest mistake youve ever made?', 'Whats the most disgusting thing youve ever done?', 'Whats one thing you hate people knowing about you?', 'Whats the worst thing anyones ever done to you?', 'Whats the best thing anyones ever done for you?', 'Have you ever had a run in with the law?', 'Whats your worst habit?', 'Whats the most embarrassing thing youve done in a taxi?', 'Whats the worst thing youve ever said to anyone?', 'Have you ever peed in the shower?', 'Whats the strangest dream youve had?', 'Have you ever been caught doing something you shouldnt have?', 'Whats the worst date youve been on?', 'Whats the best date youve been on?', 'What happened on the latest night out youve ever had?', 'Whats your biggest regret?', 'Whats the biggest misconception about you?', 'Have you ever said something you regret about someone in this room?', 'Whats one thing you wish people knew about you?', 'Wheres the weirdest place youve had sex?', 'Why did your last relationship break down?', 'Have you ever lied to get out of a bad date?', 'Whats the most trouble youve been in?', 'Whats the worst thing youve lied about?', 'Whats one thing you wish youd lied about?', 'Whats the best piece of advice youve been given?', 'Whats the most youve spent on a night out?', 'Name a time you think you were a bad partner', 'Whats your guilty pleasure?', 'Whats one thing you only do when youre alone?', 'If you had to get back with an ex, who would you choose?', 'If you had to cut one friend out of your life, who would it be?', 'Do you have a favourite friend?', 'Do you have a favourite sibling?', 'Whats the strangest rumour youve heard about yourself?', 'Whats your biggest turn on?', 'Whats the silliest reason youve left a club early?', 'What have you purchased thats been the biggest waste of money?', 'If you could swap lives with someone in this room, who would it be?']

        
        gay = discord.Embed(color=0xdfab4d, timestamp=ctx.message.created_at)

        gay.add_field(name=f'{ctx.message.author}', value=f"{random.choice(truth)}")
        await ctx.send(embed=gay)

    @commands.command()
    async def dare(self, ctx):
        truth = ['Show the most embarrassing photo on your phone', 'Show the last five people you texted and what the messages said', 'Do 100 squats', 'Let the group look in your Instagram DMs', 'Show us your screen time report', 'Yell out the first word that comes to your mind while recording it and send the video', 'Like the first 15 posts on your Facebook newsfeed send a  pic as a proof ', 'Send a sext to the last person in your phonebook', 'Show your orgasm face send a pic as a proof', 'Say two honest things about everyone else in the group', 'Twerk for a minute  while recording it and send the video ', 'Try and make the group laugh as quickly as possible', 'Try to put your whole fist in your mouth', 'Tell everyone an embarrassing story about yourself', 'Say everything in a whisper for the next 10 minutes', 'Post the oldest selfie on your phone on Instagram Stories', 'Tell the saddest story you know', 'Tell the group two truths and a lie, and they have to guess which one the lie is', 'Show off your secret talent send video/pic as proof', 'Reply to the first five Instagram Stories on your timeline', 'Share the first celebrity on your timelines Instagram to your Story', 'Attempt the first TikTok dance on your for you page', 'Give a personalised insult to everyone in the room',]

        
        gay = discord.Embed(color=0xdfab4d, timestamp=ctx.message.created_at)


        gay.add_field(name=f'{ctx.message.author}', value=f"{random.choice(truth)}")
        await ctx.send(embed=gay)

def setup(bot):
  bot.add_cog(tds(bot))
  print ("truth and Dare is up")