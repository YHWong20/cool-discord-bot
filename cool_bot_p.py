import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # .env file with your bot token should be in the same directory

# Gives bot intent permissions
intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix= "$", description= "A Cool Bot", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online")

    member_dict = {}
    for guild in bot.guilds:
        for member in guild.members:
            member_dict.update({member.id: member.display_name})
            
    print("## FOR REFERENCE ##\n\n")        
    print("## REFERENCE MEMBER DICTIONARY ##\n")
    print(member_dict)
    
    print("\n## REFERENCE GUILD ID ##\n")
    print(guild.id)
    
    print("\n\n## DEBUG ZONE ##\n")
    # Insert code that needs debugging here. Use print() to visualise    


@bot.event
# Checks if member activity has changed
async def on_member_update(before, after):
    game = ["battlefield 1", "visual studio code"]
    channel = bot.get_channel(id= 276664033971535873)

    if after.activity and after.activity.name.lower() == game[0]:
        bf_response = f"{after.mention} Playing BF1?\n https://c.tenor.com/W5fgIZhzwiAAAAAM/eyebrow-dwayne-johnson.gif"
        await channel.send(bf_response)  
    

@bot.event
# Foul Language Checker
async def on_message(message):
    bad_words = [] # Insert swear words here
    if message.author == bot.user:
        return    
    if message.content in bad_words:
        await message.channel.send(f"{message.author.mention} Watch your language!")
    

# Randomly choose reply to $hello command
@bot.command(name= "hello", help= "Gets a reply to 'hello'")
async def hello(ctx):
    answers = ["hi!", "hello!", "good day!", "how are you?", ":)"]
    answer = random.choice(answers)
    await ctx.send(answer)



bot.run(TOKEN)
