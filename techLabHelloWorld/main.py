import discord
from discord.ext.commands import Bot
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Test Bot for Tech Lab", case_insensitive=True)
channel_id = "806993458623152248"
bot_token = "ODA2OTk0NTcyMjI3NzcyNDQ2.YBxiQw.upryfy9AY0ZrUufcdkgGXIbCxM8"
tmp = "some change"


@bot.event
async def on_ready():
    print("Hello World")
    channel = bot.get_channel(int(channel_id)) # put id of channel from discord  
    await channel.send("Hello World")


bot.run(bot_token, bot=True, reconnect=True) 