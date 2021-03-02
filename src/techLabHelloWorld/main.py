import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
client = discord.Client()

bot_token = os.getenv("TECH_LAB_TOKEN")
channel_id = os.getenv("CHANNEL_ID")
print(bot_token)
print(channel_id)

bot = commands.Bot(command_prefix="!", description="Test Bot for Tech Lab", case_insensitive=True)
tmp = "some change"


@client.event
async def on_ready():
    print("Hello World")
    channel = client.get_channel(int(channel_id))  # put id of channel from discord
    await channel.send("Hello World")

@client.event
async def on_message(message):
    if message.author.id is client.user.id:
        return
    sent = None
    
    if message.content == "ping?":
        await asyncio.sleep(1)
        sent = await message.channel.send("pong!")
        
    if message.content == "log out":
        await asyncio.sleep(1)
        sent = await message.channel.send("logging off...")
        client.close()
        exit()


client.run(bot_token)