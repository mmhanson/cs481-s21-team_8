import requests
import discord

maxSongs = 50
numSongs = 0
songList = [None] * maxSongs
userList = []
currentDesc = ""


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


def getDesc():
    return currentDesc


def searchSong(track, artist, user, token):
    global currentDesc
    url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"

    querystring = {"s": artist, "t": track}

    headers = {
        'x-rapidapi-key': token,
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
        color=0xdb3b25,
    )
    #embed.set_thumbnail(url=getAlbumCover(idAlbum))

    return embed


def getAlbumCover(albumId):
    url = "https://theaudiodb.p.rapidapi.com/album.php"

    querystring = {"m": albumId}

    headers = {
        'x-rapidapi-key': "7eff181196msh647e7836d36277bp1bd94ejsn70666bc4d59d",
        'x-rapidapi-host': "theaudiodb.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonResponse = response.json()

    return jsonResponse['album'][0]['strAlbumThumb']
