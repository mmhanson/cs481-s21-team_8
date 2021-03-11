import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from api.spotify import get_track_from_spotify, audio_db_formatter

load_dotenv()
client = discord.Client()

bot_token = os.getenv("TECH_LAB_TOKEN")
channel_id = os.getenv("CHANNEL_ID")
# print(bot_token)
# print(channel_id)

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
                track_url
            ) = get_track_from_spotify(args[1])
        except Exception:
            return Response(
                "Failed to get track information",
                status=HTTP_400_BAD_REQUEST,
            )
        ret_string = "Now playing: " + str(track_name) + "\nBy Artist: " + str(track_artist) + "\n" + str(track_url)
        await ctx.send(ret_string)

        audio_db_track, audio_db_artist = audio_db_formatter(track_name, track_artist)
        # call audio db with new args
    else:
        await ctx.send("Invalid options, we don't know how to search for what you wanted!")


# @client.command(name="play song by artist")
# async def get_track(ctx, track):
#     try:
#         (
#             track_name,
#             track_artist,
#             track_url
#         ) = get_track_from_spotify(track)
#     except Exception:
#         return Response(
#             "Failed to get track information",
#             status=HTTP_400_BAD_REQUEST,
#         )
#     ret_string = "Now playing: " + str(track_name) + "\nBy Artist: " + str(track_artist) + "\n" + str(track_url)
#     await ctx.send(ret_string)

#     audio_db_track, audio_db_artist = audio_db_formatter(track_name, track_artist)
#     print(audio_db_artist)
#     print(audio_db_track)
#     # call audio db with new args



client.run(bot_token)