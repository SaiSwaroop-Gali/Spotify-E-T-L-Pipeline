import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    client_id=os.environ.get("client_id")
    client_secret=os.environ.get("client_secret")
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) #authentication
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist=sp.user_playlists('spotify')
    
    playlist_telugu = "https://open.spotify.com/playlist/37i9dQZF1DWTt3gMo0DLxA"
    playlist_url = playlist_telugu.split('/')[-1]
    data = sp.playlist_tracks(playlist_url)
    
    client = boto3.client("s3")
    
    file_name="spotify_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket='project.spotify.swaroop',
        Key='Raw_data/to_processed/' + file_name,
        Body=json.dumps(data)
        )