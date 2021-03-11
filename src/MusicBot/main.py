import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import api.audiodb

load_dotenv()
#client = discord.Client()

bot_token = os.getenv("TECH_LAB_TOKEN")
channel_id = os.getenv("CHANNEL_ID")
audiodb_token = os.getenv("AUDIODB_TOKEN")
print(bot_token)
print(channel_id)

client = commands.Bot(command_prefix="!", description="Test Bot for Tech Lab", case_insensitive=True)
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

    if message.content == "pong?":
        await asyncio.sleep(1)
        sent = await message.channel.send("ping!")
        
    if message.content == "log out":
        await asyncio.sleep(1)
        sent = await message.channel.send("logging off...")
        client.close()
        exit()

    await client.process_commands(message)


@client.command(name="play")
async def song(ctx, track, artist):
    user = f"{ctx.author.name}"
    await ctx.send(embed=api.audiodb.searchSong(track, artist, user, audiodb_token))


@client.command(name="songlist")
async def songlist(ctx):
    await ctx.send(embed=api.audiodb.printList())


@client.command(name="userlist")
async def userlist(ctx):
    await ctx.send(embed=api.audiodb.listUsers())
    await ctx.send("Looks like " + api.audiodb.getLowestRatio() + " should keep their music to themselves :grimacing:")


@client.command(name="desc")
async def desc(ctx):
    await ctx.send(api.audiodb.getDesc())


client.run(bot_token)
