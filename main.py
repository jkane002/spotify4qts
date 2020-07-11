import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

top50_uri = 'spotify:playlist:37i9dQZEVXbLRQDuF5jeBp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# today top hits store in dictionary


def main():
    results = spotify.playlist(top50_uri)
    # print(results)

    for track in results:
        print(track[0:10])
        # print('audio    : ' + track['preview_url'])
        # print('cover art: ' + track['album']['images'][0]['url'])
        print()

if __name__ == "__main__":
    main()