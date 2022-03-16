import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
# Checks if member is playing a specified game
async def on_member_update(before, after):
    game = ["battlefield 1", "visual studio code"]
    channel = bot.get_channel(id= 276664033971535873)

    if after.activity and after.activity.name.lower() == game[0]:
        bf_response = f"{after.mention} Playing BF1?\n https://c.tenor.com/W5fgIZhzwiAAAAAM/eyebrow-dwayne-johnson.gif"
        await channel.send(bf_response)  

    # elif after.activity and after.activity.name.lower() == game[1]:
    #     vs_response = f"Visual studio code deez nuts {after.mention}"
    #     await channel.send(vs_response)
    

@bot.event
# Foul Language Checker
async def on_message(message):
    bad_words = ["fuck", "fk", "fck", "fug", "fugg", "fark", "faggot", "fag", "fker", "fucker",\
         "cunt", "twat", "nigger", "penis", "asshole", "bitch", "dickhead", "pussy", "vagina", "motherfucker",\
             "motherfker", "motherfcker", "cb", "cheebai", "cheebye", "coon", "lanjiao", "lanpa", "jibai", "kns",\
                 "lj", "fkface", "fuckface"]
    if message.author == bot.user:
        return    
    if message.content in bad_words:
        await message.channel.send(f"{message.author.mention} Watch your language!")
    

@bot.command(name= "hello", help= "Gets a reply to 'hello'")
async def hello(ctx):
    answers = ["hi!", "hello!", "good day!", "how are you?", ":)"]
    answer = random.choice(answers)
    await ctx.send(answer)


@bot.command(name= "yuting", help= "Gets Yu Ting quote")
async def yuting(ctx):
    answers = ["bruh", "fk me in my ass", "bro my team fking sucks", "poggers", "i like men"]
    answer = random.choice(answers)
    await ctx.send(answer)


@bot.command(name= "euhian", help= "Gets Eu Hian quote")
async def euhian(ctx):
    answers = ["brooo?", "yooo?", "who up meatsmith", "the egg is tamago", "bro?"]
    answer = random.choice(answers)
    await ctx.send(answer)



bot.run(TOKEN)
