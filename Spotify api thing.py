import dotenv
import os
import spotipy

dotenv.load_dotenv()
c_id = os.getenv("CLIENT_ID")
c_secret = os.getenv("CLIENT_SECRET")
scope = 'playlist-read-private'
redirect_uri = os.getenv("REDIRECT_URI")
sp = spotipy.Spotify(auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=c_id, client_secret=c_secret, redirect_uri=redirect_uri, scope=scope))
a = sp.current_user_playlists()
for i in a['items']:
    if i['name'] == "Anime Music":
        results = sp.playlist(i['id'], fields="tracks")
        tracks = results['tracks']
        l=[]
        for idx, item in enumerate(tracks['items']):
            track = item['track']
            l.append(track['name'])
print(l)