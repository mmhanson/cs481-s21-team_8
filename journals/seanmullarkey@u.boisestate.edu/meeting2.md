# Meeting 2

- Attendance: Everyone present

This week we have officially decided on a project. We will develop a discord bot that can act as a
media player, retrieving songs from spotify. This bot will interact with a separate API known as the
audioDB which contains important discography of songs that we previously requested from the spotify API.

We broke up how we wanted to implement this in five steps. We first want to hit the spotify endpoint
for the song a user requests. If that song is found, then we want to proceed and retrieve the infomation
from the AudioDB. We know that the AudioDB is much more expansive than spotify's current library.
If we tried to retrieve information on valid AudioDB responses first, there is a chance we still may
not find the track on spotify. But we figured there is much less margin of error the other way around.
Then we will store the like/dislike ratio of the given track's music video and average that out to what
we refer to as the "taste ratio" for each user. Then, finally we play that song using discord's built in
audio player.

We started to think of additional features we could implement when we finish but have extra time. Some
ideas we came up with include push notifications on your phone from the discord bot teasing you
lightheartedly to come back to the channel and increase your music taste scores.

My task for this week:

- Research how to integrate the media player in the Discord application
- Research how we register for an authorization token for Discord, Spotify, and AudioDB API's
- Start thinking of good ways to separate this project into different stories that a team can tackle together.
