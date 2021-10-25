# Discord Bot to ge Patch Notes for Games
import os 

import discord # discord python library 
from discord.ext import commands # commands framework
from dotenv import load_dotenv # used for environmental variables 
from crypto_src.crypto_data import CryptoData

import importlib.util # use to import custom python modules 

# .env 
load_dotenv() # adds the env variables from .env
TOKEN = os.getenv('DISCORD_TOKEN') # BOT API Key
GUILD = os.getenv('DISCORD_GUILD') # Sets guild(server) to nooooooaaaaaaaah

bot = commands.Bot(command_prefix = '-') # sets up prefix and establishes the client as bot

@bot.event # Prints if connection is established
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context = True)
async def crypto(ctx, *args):
    channel = bot.get_channel(865695929440272456) # ID for new-world text channel
    #print(args)
    coin = CryptoData(args[0], args[1])
    coin_price = (f"{coin.price[args[0]][args[1]]} {args[1]}")
    await channel.send(coin_price)
    

bot.run(TOKEN) # Runs the bot logging in with token(Patch Notes Bot)

