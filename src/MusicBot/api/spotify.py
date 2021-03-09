import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

BASE_URL = 'https://api.spotify.com/v1/'
AUTH_URL = 'https://accounts.spotify.com/api/token'
track_id = '6y0igZArWVi6Iz0rj35c1Y'

def get_headers():
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': spotify_client_id,
        'client_secret': spotify_client_secret,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    return headers


def get_spotify_track_example(track_id):
    headers = get_headers()
    response = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    response = response.json()
    return response

def search_spotify_for_artist(artist_name):
    headers = get_headers()
    query_artist_string = artist_name.replace(" ", "%20")
    response = requests.get(BASE_URL + 'search?query=' + query_artist_string + '&type=artist', headers=headers)
    response = response.json()
    return response

def search_spotify_for_track(track_name):
    headers = get_headers()
    query_track_string = track_name.replace(" ", "%20")
    response = requests.get(BASE_URL + 'search?query=' + query_track_string + '&type=track', headers=headers)
    response = response.json()
    return response


track_response = search_spotify_for_track('Why I love the moon')
first_result = track_response['tracks']['items'][0]
first_result_artist = first_result['artists'][0]['name']

def extract_spotify_url(track_reponse):
    spotify_url = track_reponse['external_urls']['spotify']
    return spotify_url
    


print(first_result_artist) # to get the first artist (likely the result we were looking for)
print(extract_spotify_url(first_result)) # to get the spotify link to play the song
