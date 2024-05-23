import spotipy
from spotipy.oauth2 import SpotipyOAuth
import json

scope = 'playlist-modify-public'
username = 'Lohith'

token =  SpotipyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#create a palylits

playlist_name = input("enter playlist name:")
playlist_description = input("enter playlist description:")

spotifyObject.user_playlist.creat(user=username, name=playlist_name, public=True, description=playlist_description)
