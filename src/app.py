import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt
# load the .env file variables
load_dotenv()

artisturl = '1Xyo4u8uXC1ZmMpatF05PJ'
client_credential_manager = SpotifyClientCredentials(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"))
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)
results = sp.artist_top_tracks(artisturl)


for track in results['tracks'][:10]:
    print('track    : ' + str(track['name']))
    print('popularity    : ' + str(track['popularity']))
    print('duration: ' + str(track['duration_ms']/1000/60))
    print()

songs = []
for track in results['tracks'][:10]:
    song = { 'Track' : str(track['name']),
            'Popularity' :  track['popularity'], 
            'Duration' : track['duration_ms']/1000/60           

    }
    songs.append(song)

step6 = pd.DataFrame(songs[:3])
print(step6)

x = []
y = []
for track in results['tracks'][:10]:

    x.append(track['popularity'])
    y.append(track['duration_ms']/1000/60 )

plt.scatter(x, y)
plt.show()