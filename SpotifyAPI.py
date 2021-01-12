import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
try:
    client_credentials_manager = SpotifyClientCredentials(client_id='{ Enter Your CLIENT ID }', client_secret='{ Enter Your CLIENT SECRET }')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    name = input("ENTER NAME OF ARTIST\n")
    result = sp.search(name)
    URI = result['tracks']['items'][0]['artists'][0]['uri']
    results = sp.artist_albums(URI, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    a = []
    for album in albums:
        if album['name'] not in a:
            a.append(album['name'])
    for i in a:
        print(i)
except:
    print("Server Error.Retry!!")