import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TECHLABTOKEN")
channel_id = os.getenv("CHANNELID")
print(bot_token)
print(channel_id)

bot = commands.Bot(command_prefix="!", description="Test Bot for Tech Lab", case_insensitive=True)
tmp = "some change"

@bot.event
async def on_ready():
    print("Hello World")
    channel = bot.get_channel(int(channel_id)) # put id of channel from discord  
    await channel.send("Hello World")


bot.run(bot_token, bot=True, reconnect=True) 