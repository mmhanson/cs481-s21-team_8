import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import re
from dotenv import load_dotenv
import asyncio
from api.spotify import get_track_from_spotify, audio_db_formatter
from api import audiodb
import shlex

load_dotenv()
client = discord.Client()

bot_token = os.getenv("TECH_LAB_TOKEN")
channel_id = os.getenv("CHANNEL_ID")

client = commands.Bot(command_prefix="!", description="Music Bot", case_insensitive=True)
tmp = "some change"


@client.event
async def on_ready():
    print("Music Bot is ready!")
    channel = client.get_channel(int(channel_id))  # put id of channel from discord
    await channel.send("Music Bot is ready!")


@client.event
async def on_message(message):
    if message.author.id is client.user.id:
        return
    sent = None
  
    if message.content.lower() == "--log_out":
        await asyncio.sleep(1)
        sent = await message.channel.send("logging off...")
        await client.logout()
        # exit()

    if message.content.startswith("MusicBot Play"):
        # if message.content.startswith("MusicBot Play"):
        content = message.content
        args_list = shlex.split(content)
        args_list = args_list[2:]
        # args_list = args_list[2:]
        await get_track(args_list, message.author.name, message)

    if message.content.lower() == "musicbot now playing":
        await currsong(message)

    if message.content.lower() == "musicbot user list":
        await userlist(message)

    if message.content.lower() == "musicbot user list --clear":
        await userlistclear(message)

    if message.content.lower() == "musicbot user list --ranktest":
        await userlist_rankingtest(message)

    if message.content.lower() == "musicbot song list":
        await songlist(message)

    if message.content.lower() == "musicbot song list --clear":
        await songlistclear(message)

    await client.process_commands(message)


async def get_track(args_list, author, message):
    user = f"{author}"
    test_mode = False
    if len(args_list) > 3:
        if "--test" in args_list[3].lower():
            test_mode = True
            await message.channel.send("Test Mode Active!")
        else:
            await message.channel.send("Too many arguments! Try again!")
            return

    if test_mode:
        # currently this defaults to livin on a prayer for test mode.
        # It's alright for now but maybe we can come up with a more dynamic test in the future
        track_name = "Livin' on a Prayer"
        track_artist = "Bon Jovi"
        track_album = "Slippery When Wet"
        track_ratio = 0.98
        track_url = "https://open.spotify.com/track/37ZJ0p5Jm13JPevGcx4SkF"
        album_cover = "https://community.mp3tag.de/uploads/default/original/2X/a/acf3edeb055e7b77114f9e393d1edeeda37e50c9.png"
        audiodb.addSong(track_name, track_artist, track_album, track_ratio, user)

    if len(args_list) > 1:
        if args_list[1] == "by":
            await message.channel.send("Searching Song By Artist...")
            if not test_mode:
                try:
                    (
                        track_name,
                        track_artist,
                        track_url,
                        album_cover
                    ) = get_track_from_spotify(args_list[0], args_list[2], "artist")
                except Exception:
                    await message.channel.send("400 Error!")
                    return
        elif args_list[1] == "from":
            await message.channel.send("Searching Song By Album...")
            if not test_mode:
                try:
                    (
                        track_name,
                        track_artist,
                        track_url,
                        album_cover
                    ) = get_track_from_spotify(args_list[0], args_list[2], "album")
                except Exception:
                    await message.channel.send("400 Error!")
                    return
        else:
            await message.channel.send("invalid arguments! Please try again!")
            return
    else:
        if not test_mode:
            await message.channel.send("Searching Song By Best Match...")
            try:
                (
                    track_name,
                    track_artist,
                    track_url,
                    album_cover

                ) = get_track_from_spotify(args_list[0], None, None)
            except Exception:
                await message.channel.send("400 Error!")
                return

    # ret_string = "Now playing: " + str(track_name) + "\nBy Artist: " + str(track_artist) + "\n" + str(track_url)
    # await message.channel.send(ret_string)

    audio_db_track, audio_db_artist = audio_db_formatter(track_name, track_artist)
    if test_mode:
        embed = discord.Embed(
            title="Now Playing!",
            description=track_name + " by " + track_artist,
            color=0xe6ba39,
        )
        embed.set_thumbnail(url=album_cover)
    else:
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

    # await message.channel.send(embed=embed)
    # I want to test the embedded stuff in the future.
    # This is important but I'm not quite sure how to do it yet

    ret_string = "Now playing: " + str(track_name) + "\nBy Artist: " + str(track_artist) + "\n" + str(track_url)
    await message.channel.send(ret_string)


async def songlist(message):
    await message.channel.send(embed=audiodb.printList())


async def songlistclear(message):
    await audiodb.clearSongs()


async def userlist(message):
    await message.channel.send(embed=audiodb.listUsers())
    await message.channel.send(audiodb.getQuip())


async def userlistclear(message):
    await audiodb.clearUsers()


async def userlist_rankingtest(message):
    audiodb.clearUsers()
    audiodb.addUser("Bill", .90)
    audiodb.addUser("Bill", .50)
    audiodb.addUser("Bill", .10)
    audiodb.addUser("Sarah", .95)
    await message.channel.send(embed=audiodb.listUsers())
    await message.channel.send(audiodb.getQuip())


# async def desc(message):
#     await message.send(audiodb.getDesc())


async def currsong(message):
    await message.channel.send(embed=audiodb.getCurrSong())


client.run(bot_token)
