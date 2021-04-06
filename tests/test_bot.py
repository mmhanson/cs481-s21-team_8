import asyncio
import sys
from distest import TestCollector
from distest import run_dtest_bot
from discord import Embed 
from distest import TestInterface


test_collector = TestCollector()

# test default song by artist
@test_collector()
async def test_play_song_by_artist_response(interface):
    test_song = "Livin' on a Prayer"
    test_artist = "Bon Jovi"  
    message = await interface.send_message(
        f'MusicBot Play "{test_song}" by "{test_artist}" --test' 
    )
    await asyncio.sleep(3)
    response_message = message.channel.last_message
    await interface.assert_message_contains(response_message, f"Now playing: {test_song}")
    await interface.assert_message_contains(response_message, f"By Artist: {test_artist}")

#test that the info within the embed is what it should be
@test_collector()
async def test_song_list_info(interface):
    desc = "**Song:** Livin' on a Prayer **Artist:** Bon Jovi **Album:** Slippery When Wet **Like Ratio:** 0.98 **Played By:** CS 481 Tester Bot"
    embed = Embed(
        title="Recently Played!",
        description=desc,
        color=0x1DB954,
    )
    await interface.assert_reply_embed_equals(
        'MusicBot song list', embed
    )
    await asyncio.sleep(3)
    
# test default song by album
@test_collector()
async def test_play_song_by_album_response(interface):
    test_song = "Livin' on a Prayer"
    test_artist = "Bon Jovi"  
    test_album = "Slippery When Wet"
    message = await interface.send_message(
        f'MusicBot Play "{test_song}" from "{test_album}" --test'
    )
    await asyncio.sleep(3)
    response_message = message.channel.last_message
    await interface.assert_message_contains(response_message, f"Now playing: {test_song}")
    await interface.assert_message_contains(response_message, f"By Artist: {test_artist}")


@test_collector()
async def test_get_now_playing(interface): # this doesn't show if we are in test mode currently
    message = await interface.send_message(
        f'MusicBot now playing' 
    )
    await asyncio.sleep(3)


@test_collector()
async def test_get_user_list(interface):
    embed = Embed(title="Music Taste Leaderboard!")
    # await interface.get_delayed_reply(5, interface.assert_reply_embed_equals, embed, attributes_to_check=["title"])
    await interface.assert_reply_embed_equals(
        'MusicBot user list' , embed, attributes_to_check=["title"]
    )
    await asyncio.sleep(3)


@test_collector()
async def test_get_song_list(interface):
    embed = Embed(title="Recently Played!")
    # await interface.get_delayed_reply(5, interface.assert_reply_embed_equals, embed, attributes_to_check=["title"])
    await interface.assert_reply_embed_equals(
        'MusicBot song list' , embed, attributes_to_check=["title"]
    )
    await asyncio.sleep(3)

# log out after tests
@test_collector()
async def test_log_out(interface):
    message = await interface.send_message("--log_out")
    # await asyncio.sleep(1)
    # await interface.assert_reply_contains(message, "logging off...")
    # await asyncio.sleep(3)

if __name__ == "__main__":
    run_dtest_bot(sys.argv, test_collector)
