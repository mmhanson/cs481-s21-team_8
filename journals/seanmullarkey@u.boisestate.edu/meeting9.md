# Meeting 8

- Attendance: Everyone present

Ben created new features for our music bot. We used to get album cover data from the audio db API but that required another call to a different endpoint. Because the audioDB cost is so high, we wanted to find a different way to pull the album cover photo. Ben found that the spotify API gives us that album cover when we get our track object so we decided to integrate that into our music bot.

I developed a new feature where we can specify a track by either an artist or an album. Previously, we pulled tracks which were the best match by keyword. We changed this so that by adding extra parameters to the current endpoint we are calling, we can now specify artist and album keywords as well. 

My task for this week:
- Fix output and how it is styled on discord
- Write tests on new endpoints and bot interactions


