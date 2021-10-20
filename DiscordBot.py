# Discord Bot to ge Patch Notes for Games
import os 

import discord # discord python library 
from discord.ext import commands # commands framework
from dotenv import load_dotenv # used for environmental variables 

from parseHTML import queue_time # returns info

# .env 
load_dotenv() # adds the env variables from .env
TOKEN = os.getenv('DISCORD_TOKEN') # BOT API Key
# GUILD = os.getenv('DISCORD_GUILD') # Sets guild(server) to nooooooaaaaaaaah

bot = commands.Bot(command_prefix = '-') # sets up prefix and establishes the client as bot

@bot.event # Prints if connection is established
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context = True)
async def challenges(ctx, *args):
    channel = bot.get_channel(896900001207320656) # ID for new-world text channel
    print(args)
    #await channel.send('The queue time is: ')
    

bot.run(TOKEN) # Runs the bot logging in with token(Patch Notes Bot)

