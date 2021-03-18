# Meeting 8

- Attendance: All were present

This week I showed them the changes I made over the weekend, I added a double try/catch so that the program no
longer breaks if a song isn't found the audiodb, though if it fails the first time, it tries once more after
breaking off everything behind characters like "-" and "(" because those are common extra things on Spotify's
titles that the audiodb doesn't like. If it fails both times though, it will print out a message saying it wasn't
found. Along with that I also showed them how I saved off the album cover to create a "now playing" embed that can
be displayed on command, and I wrote the function to choose a different little quip to go after the leaderboard
depending on different possible situations with all the users. We then merged that code into the default branch,
and Sean went over some more ideas for the Spotify API such as how to request the artist or album name along with
the track.

My task for this week:

- Brainstorm additional functions that could be helpful, or things to add to the current embeds.
- Try imputting more edge cases to see if I need to add more characters to the try/catch.
- Start writing test functions for our GitHub Actions that target my code.
