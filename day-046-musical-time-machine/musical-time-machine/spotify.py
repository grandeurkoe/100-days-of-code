import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"


class Spotify:
    def __init__(self):
        self.top100_uri = []
        self.spotipy_api = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="playlist-modify-private"
        ))

    def create_playlist(self, time_travel_date):
        """Creates an empty playlist."""
        client = self.spotipy_api.current_user()

        top100_playlist = self.spotipy_api.user_playlist_create(
            user=client['id'],
            name=f"Top 100 Billboard ({time_travel_date})",
            public=False,
            description=f"The top 100 billboard songs on {time_travel_date}",
        )
        return top100_playlist

    def add_tracks_playlist(self, top100_titles, top100_playlist):
        """Add tracks to a given playlist."""
        for song_index in range(len(top100_titles)):
            each_song = self.spotipy_api.search(
                q=f"{top100_titles[song_index]}",
                type="track",
                limit=1)
            self.top100_uri.append(each_song['tracks']['items'][0]['uri'])

        self.spotipy_api.playlist_add_items(
            playlist_id=top100_playlist['id'],
            items=self.top100_uri,
        )
