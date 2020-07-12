import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

# Top 50 songs in US URI
top50_uri = 'spotify:playlist:37i9dQZEVXbLRQDuF5jeBp'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

###############
#
# Parses JSON Object passed in from spotify
# Returns object in following format for each song
#
# "Track #": {
#   "song": "",
#   "preview": "",
#   "images": [],
#   "uri": "",
#   "album": "",
#   "artists": {}
# }
#
###############
def parse(json_obj) :
    data_out = {}
    res = json_obj['items']

    for i in range(0,len(res)):
        data_out[str(i)] = {}
        # Song name
        data_out[str(i)]['song'] = res[i]['track']['name']
        # Album name
        data_out[str(i)]['album'] = res[i]['track']['album']['name']
        # Preview url
        data_out[str(i)]['preview']= res[i]['track']['preview_url']
        # Album Images
        data_out[str(i)]['images']= res[i]['track']['album']['images']
        # Song URI
        data_out[str(i)]['uri'] = res[i]['track']['uri']
        # Song
        # Artists on song
        data_out[str(i)]['artists'] = {}
        for j in range( 0, len( res[i]['track']['artists'] ) ) :
            data_out[str(i)]['artists'][str(j)] = res[i]['track']['artists'][j]['name']

    return data_out

def main():
    results = spotify.playlist_tracks(top50_uri)
    # Stores parsed data
    songs_data = parse(results)
    

if __name__ == "__main__":
    main()