# CS481 - Senior Design Project

TODO:[CI Lab](https://shanep.github.io/capstone/labs/ci/)

## Project Epic

Our project is a Discord bot based around utilizing APIs to rank the musical tastes of users in a Discord chat. The bot will have two different purposes: the first is as a Spotify player inside of Discord that can be used to play music for a whole chat, and the second is to take music from the chat and use it to analyze user and chat taste.

The first part, the Spotify player, is fairly simple. It will store music linked in the chat or played via the bot in an internal buffer of about 50 songs or so, with the user that played the song, song title, artist, album, and music video like/dislike ratio all being saved. This will interface with Spotify’s API to get the songs to play, and then will interface using the name, album, and artist of the song to get the like/dislike ratio of the music video for the song (if it exists) from an API on a website called “TheAudioDB.” We anticipate that most songs on Spotify will be on TheAudioDB, but that the reverse isn’t necessarily true - hence, why the bot will search Spotify first to find data to plug into TheAudioDB. If there’s no data for the music video on TheAudioDB, an indicator of this is put into the file.

The second part of the project, the analyzer, takes the data of the like/dislike ratios and collates it into a tongue-in-cheek analysis of the music taste of users and the chat at large. When called, this bot will take the like/dislike ratio of the songs in the buffer and total the like/dislike ratios per user, and then display this data out into the chat with various humorous yet light-hearted messages attached to it. For example, the user with the lowest ratio will be told they need better taste, while the person at the top is called a conformist.

The overall process will be like this: a user searches a song on Spotify with our bot, the bot pings Spotify’s API to get the song. If there is a valid response retrieved from the Spotify endpoint, the bot then reaches out to TheAudioDB API to get the like/dislike data as well as other discography information a user may want (which we have not yet decided what we would like to make available for the user). We then will store this data and the other information pertaining the song that we retrieved from Spotify API (title, album, artist, etc) internally so it can be recalled and displayed with various commands to the users, and then the bot will call the built in music player in Discord with the response we get from Spotify to play the song.

Some other features we discussed about implementing is having our Discord bot give us push notifications through the Discord app when we haven’t visited the channel it is registered on in a while. If we have a relatively high “musical taste” according to the like/dislike ratio, maybe the bot would make fun of us for enjoying popular music so much. If we have a low musical taste ranking, then the bot would try to encourage us to revisit the channel to play some more songs to increase our ranking.

### Tech lab

TODO:[Tech Lab](https://shanep.github.io/capstone/labs/tech/)

## Planning Lab

TODO:[Planning Lab](https://shanep.github.io/capstone/labs/planning/)

- [Jane's Plan](planning/janedoe@u.boisestate.edu.md)
- John's Plan
- Bob's Plan
