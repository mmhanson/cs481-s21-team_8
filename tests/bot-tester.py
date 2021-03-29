import asyncio
import sys
from distest import TestCollector
from distest import run_dtest_bot
from discord import Embed 
from distest import TestInterface


test_collector = TestCollector()
created_channel = None

# test default song by artist
@test_collector()
async def test_play_song_response(interface):
    test_song = "Livin' on a Prayer"
    test_artist = "Bon Jovi"    
    # await interface.assert_message_contains(message, f"Now playing: {test_song}")
    # await interface.assert_message_contains(message, f"By Artist: {test_artist}")
    # await asyncio.sleep(5)
    # await interface.assert_reply_contains(message,  f"Now playing: {test_song}")
    message = await interface.send_message(
        f'MusicBot Play "{test_song}" by "{test_artist}" test' 
    )
    await interface.get_delayed_reply(3, interface.assert_message_contains, f"Now playing: {test_song}")
    

if __name__ == "__main__":
    run_dtest_bot(sys.argv, test_collector)
