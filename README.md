# CS481 - Senior Design Project

TODO:[CI Lab](https://shanep.github.io/capstone/labs/ci/)

## Project Epic

Our project is a Discord bot based around utilizing APIs to rank the musical tastes of users in a Discord chat. The bot will have two different purposes: the first is as a Spotify player inside of Discord that can be used to play music for a whole chat, and the second is to take music from the chat and use it to analyze user and chat taste.

The first part, the Spotify player, is fairly simple. It will store music linked in the chat or played via the bot in an internal buffer of about 50 songs or so, with the user that played the song, song title, artist, album, and music video like/dislike ratio all being saved. This will interface with Spotify’s API to get the songs to play, and then will interface using the name, album, and artist of the song to get the like/dislike ratio of the music video for the song (if it exists) from an API on a website called “TheAudioDB.” We anticipate that most songs on Spotify will be on TheAudioDB, but that the reverse isn’t necessarily true - hence, why the bot will search Spotify first to find data to plug into TheAudioDB. If there’s no data for the music video on TheAudioDB, an indicator of this is put into the file.

The second part of the project, the analyzer, takes the data of the like/dislike ratios and collates it into a tongue-in-cheek analysis of the music taste of users and the chat at large. When called, this bot will take the like/dislike ratio of the songs in the buffer and total the like/dislike ratios per user, and then display this data out into the chat with various humorous yet light-hearted messages attached to it. For example, the user with the lowest ratio will be told they need better taste, while the person at the top is called a conformist.

The overall process will be like this: a user searches a song on Spotify with our bot, the bot pings Spotify’s API to get the song. If there is a valid response retrieved from the Spotify endpoint, the bot then reaches out to TheAudioDB API to get the like/dislike data as well as other discography information a user may want (which we have not yet decided what we would like to make available for the user). We then will store this data and the other information pertaining the song that we retrieved from Spotify API (title, album, artist, etc) internally so it can be recalled and displayed with various commands to the users, and then the bot will call the built in music player in Discord with the response we get from Spotify to play the song.

Some other features we discussed about implementing is having our Discord bot give us push notifications through the Discord app when we haven’t visited the channel it is registered on in a while. If we have a relatively high “musical taste” according to the like/dislike ratio, maybe the bot would make fun of us for enjoying popular music so much. If we have a low musical taste ranking, then the bot would try to encourage us to revisit the channel to play some more songs to increase our ranking.

### Feeback from shane

Nice idea! Just like we talked about today I think a discord bot would be really cool and defiantly big enough for this class. I personally would write it in typescript and leverage discord.js however if python makes more sense the got with that! Sorry for not getting feedback to you sooner, I have been slammed and got a little behind in grading.

I am excited to see the finished project! 


### Tech lab

Discord.py:

Discord.py is the standard framework for developing discord bots for writing it in the python programming language. Some of its important features to utilize includes modern pythonic API requests using the async/await syntax, being able to implement the entirety of the Discord API, easy to use object oriented design, and speed and memory optimization. To use this, we simply install the package using pip install discord.py and the functionalities that this framework provides is ready to use. 

Akairo:

Akairo is a Discord bot framework based around Discord.js, which is in turn a node.js module used to interact with Discord. Akairo is installed via npm and features a number of different utilities; in general, it appears to be a very comprehensive bot framework. Notable among its features are the ability to interface easily with databases (including sqlite), which would be useful in our case for the storage of song information. Also notable is the full suite of features related to implementing commands (which would be useful for the number of different commands and command line options we’ll have to support) including one that allows commands to be placed on a cooldown - this would be useful, for example, in the case of the taste analyzer, which we wouldn’t want people to be able to spam the chat with.

Discord-Hero:

Discord-Hero is a Discord bot framework intended to help create bots quicker and easier. It includes all the basic functions found in discord.py that you need to start making your bot, and also includes more advanced features using other discord bot frameworks, such as FastAPI and Django. This framework includes all the core commands for creating a bot, as well as the ability to create extensions, cogs, and listeners, all features found in discord.py, but it changes all the command and class names. It also includes some more advanced features like controllers and models, which comes from the Django framework. Overall, it’d be better to stick to discord.py over this framework due to the lack of documentation discord-hero has, and the changing of command and class names could lead to confusion when trying to debug.

## Planning Lab

TODO:[Planning Lab](https://shanep.github.io/capstone/labs/planning/)

- [Jane's Plan](planning/janedoe@u.boisestate.edu.md)
- John's Plan
- Bob's Plan

## Running the bot 

# change this later to run the build script instead
In one terminal, run the ./startbot.sh script

## To run tests 
In a separate terminal run the ./test.sh script 
(
This will not work with the current version of distest. Author of repo has been notified of bug.
To run tests currently as of 2/18/2019, go into validate_discord_token.py and change line 19 to include the letter O
```
if not re.match(r"[MNO][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}", token_value):
```
)
