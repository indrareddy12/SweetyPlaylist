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

spotifyObject.user_playlist.create(user=username, name=playlist_name, public=True, description=playlist_description)


user_input = input("enter the song:")
list_of_songs = []

while user_input != 'quit' :
    result = spotifyObject.search(q=user_input)
    
    list_of_songs.append(result['track']['items'][0]['uri'])
    user_input = input("enter the song:")
    
#find the new playlist

Playlist = spotifyObject.user_playlists(user=username) 
playlist = prePlaylist.['items'][0]['uri']

#add songs

spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs,)
    