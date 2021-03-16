import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()
audiodb_token = os.getenv("AUDIODB_TOKEN")
maxSongs = 50
numSongs = 0
songList = [None] * maxSongs
userList = []
currentSong = discord.Embed()


class trackInfo():
    def __init__(self, title, artist, album, ratio):
        self.title = title
        self.artist = artist
        self.album = album
        self.ratio = ratio


class userInfo():
    def __init__(self, name, ratio, songsReq):
        self.name = name
        self.ratio = ratio
        self.songsReq = songsReq


def getQuip():
    if rankFunc(userList[0]) < .5:
        return "I'm not mad, just disappointed :neutral_face:"
    elif rankFunc(userList[len(userList)-1]) > .8:
        return "Do you guys listen to anything not in the top 100? :rolling_eyes:"
    elif rankFunc(userList[0]) > .95:
        return "All hail " + getHighestRatio() + "! :crown:"
    else:
        return "Looks like " + getLowestRatio() + " should keep their music to themselves :grimacing:"


def addSong(title, artist, album, ratio):
    global songList, numSongs, maxSongs
    track = trackInfo(title, artist, album, ratio)
    songList[numSongs] = track
    numSongs += 1
    numSongs = numSongs % maxSongs


def printList():
    songs = ""
    for i in range(numSongs, len(songList)):
        if songList[i] is not None:
            songs = songs + ("**Song:** " + songList[i].title + " **Artist:** " + songList[i].artist + " **Album:** " + songList[i].album + " **Like Ratio:** " + str(songList[i].ratio) + "\n\n")
    for i in range(0, numSongs):
        if songList[i] is not None:
            songs = songs + ("**Song:** " + songList[i].title + " **Artist:** " + songList[i].artist + " **Album:** " + songList[i].album + " **Like Ratio:** " + str(songList[i].ratio) + "\n\n")
    embed = discord.Embed(
        title="Recently Played!",
        description=songs,
        color=0x1DB954,
    )
    return embed


def addUser(username, ratio):
    global userList
    for i in range(0, len(userList)):
        if userList[i].name == username:
            userList[i].ratio += ratio
            userList[i].songsReq += 1
            return
    user = userInfo(username, ratio, 1)
    userList.append(user)


def rankFunc(e):
    return float(e.ratio) / float(e.songsReq)


def listUsers():
    users = ""
    userList.sort(reverse=True, key=rankFunc)
    for i in range(0, len(userList)):
        users = users + ("**Name:** " + userList[i].name + " **Ratio:** " + str(round(float(userList[i].ratio)/float(userList[i].songsReq), 2)) + "\n\n")
    embed = discord.Embed(
        title="Music Taste Leaderboard!",
        description=users,
        color=0x7289da,
    )
    return embed


def getLowestRatio():
    return userList[len(userList)-1].name


def getHighestRatio():
    return userList[0].name


def getCurrSong():
    return currentSong


def searchSong(track, artist, user, coverurl):
    global currentSong
    url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"

    querystring = {"s": artist, "t": track}

    headers = {
        'x-rapidapi-key': audiodb_token,
        'x-rapidapi-host': "theaudiodb.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonResponse = response.json()

    print(response.text)

    artistName = jsonResponse['track'][0]['strArtist']
    #print(artistName)
    albumName = jsonResponse['track'][0]['strAlbum']
    #print(albumName)
    trackName = jsonResponse['track'][0]['strTrack']
    #print(trackName)
    idAlbum = jsonResponse['track'][0]['idAlbum']
    #if jsonResponse['track'][0]['strTrackThumb'] is not None:
    #    cover = jsonResponse['track'][0]['strTrackThumb']
    #    print(cover)
    if jsonResponse['track'][0]['strDescriptionEN'] is not None:
        trackDesc = jsonResponse['track'][0]['strDescriptionEN']
        currentDesc = trackDesc
        #print(trackDesc)
    if jsonResponse['track'][0]['intMusicVidLikes'] is not None and jsonResponse['track'][0]['intMusicVidDislikes'] is not None:
        likes = float(jsonResponse['track'][0]['intMusicVidLikes'])
        dislikes = float(jsonResponse['track'][0]['intMusicVidDislikes'])
        totalLikeDislike = likes + dislikes
        if totalLikeDislike > 0:
            likeRatio = round(likes / totalLikeDislike, 2)
            #print(likes)
            #print(dislikes)
            #print(totalLikeDislike)
            #print(likeRatio)
        else:
            likeRatio = "N/A"
    else:
        likeRatio = "N/A"

    addSong(trackName, artistName, albumName, likeRatio)

    if likeRatio != "N/A":
        addUser(user, likeRatio)

    embed = discord.Embed(
        title="Now Playing!",
        description=trackName + " by " + artistName,
        color=0xe6ba39,
    )
    embed.set_thumbnail(url=coverurl)
    currentSong = embed
    return embed
