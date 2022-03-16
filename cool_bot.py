import os

import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix= "$", description= "your mom", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is online")

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
# Checks if user is playing BF1
async def on_member_update(before, after):
    game = "battlefield 1"
    channel = client.get_channel(id= 276664033971535873)

    if after.activity and after.activity.name.lower() == game:
        response = f"Stop Playing BF1 {after.mention}"
        await channel.send(response)  
    

@bot.command(name= "hello")
async def reply(ctx):
    answers = ["hi!", "hello!", "good day!"]
    answer = random.choice(answers)
    await ctx.send(answer)

##@bot.event
##async def on_message(message):
##    if message.author == client.user:
##        return
##            
##    if message.author.id == 287532310130196480:
##        await message.channel.send("ok junhan thanks 4 ur input")
##    elif message.author.id == 286487459431186432:
##        await message.channel.send("ok yuting thanks 4 ur input")
bot.run(TOKEN)
