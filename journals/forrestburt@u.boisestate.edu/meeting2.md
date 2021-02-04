# Meeting 2

- Attendance: All present

This week we formally decided on a project from the research we did last week: a Discord bot that utilizes two different APIs to perform a couple different music related functions in a chat. We decided that the first part of the bot is a Spotify music player - users will be able to call the bot to play music for an entire chat. The second part is as a taste analyzer - the bot will keep track of what songs are called by which user and then use that data to present tongue-in-cheek comments about the user's music taste.

We've decided that the bot will operate via what is basically a five step process: 1. User searches for a song using the bot. 2. Bot pings the Spotify API to get the song and some info about it. 3. Bot takes this information and uses it to ping another API, TheAudioDB, to get information about the like/dislikes on the song's music video (if it exists). 4. The bot stores all of the data about the song (title, artist, album, user that called it, etc) internally so it can be recalled. 5. The bot plays the song with Spotify and displays some information about the song. 

The taste analyzer will, in essence, take the internally stored data per user and then display information out based on this.

Much of the meeting was spent planning this and writing our epic, which we mostly finished in the time we had. We all agreed to check back over the epic before the end of the weekend and let the others know over Discord whether or not we were good with it.

My task for this week:

- Review the project epic over the weekend and let the group know if it looks good
