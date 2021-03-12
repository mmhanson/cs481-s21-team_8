import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import re
from dotenv import load_dotenv
import asyncio
from api.spotify import get_track_from_spotify, audio_db_formatter
from api import audiodb

load_dotenv()
#client = discord.Client()

bot_token = os.getenv("TECH_LAB_TOKEN")
channel_id = os.getenv("CHANNEL_ID")
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
async def get_track(ctx, *args):
    if args[0] == "song":
        try:
            (
                track_name,
                track_artist,
                track_url,
                album_cover
            ) = get_track_from_spotify(args[1])
        except Exception:
            return Response(
                "Failed to get track information",
                status=HTTP_400_BAD_REQUEST,
            )
        ret_string = "Now playing: " + str(track_name) + "\nBy Artist: " + str(track_artist) + "\n" + str(track_url)
        await ctx.send(ret_string)

        audio_db_track, audio_db_artist = audio_db_formatter(track_name, track_artist)
        user = f"{ctx.author.name}"
        try:
            embed = audiodb.searchSong(audio_db_track, audio_db_artist, user, album_cover)
        except Exception:
            split_track = re.split("[-(]|FEAT.", audio_db_track)
            split_track[0] = split_track[0].strip("_")
            try:
                embed = audiodb.searchSong(split_track[0], audio_db_artist, user, album_cover)
            except Exception:
                embed = discord.Embed(
                    title="Uh-oh :astonished:",
                    description="That song couldn't be found in our database, sorry!",
                    color=0xff1500,
                )
                audiodb.currentSong = embed

        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid options, we don't know how to search for what you wanted!")



@client.command(name="songlist")
async def songlist(ctx):
    await ctx.send(embed=audiodb.printList())


@client.command(name="userlist")
async def userlist(ctx):
    await ctx.send(embed=audiodb.listUsers())
    await ctx.send(audiodb.getQuip())


# @client.command(name="desc")
# async def desc(ctx):
#     await ctx.send(audiodb.getDesc())


@client.command(name="nowplaying")
async def currsong(ctx):
    await ctx.send(embed=audiodb.getCurrSong())

client.run(bot_token)
