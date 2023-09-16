from billboard import Billboard
from spotify import Spotify

billboard_on_date = Billboard()
spotify = Spotify()

time_travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

top100_titles = billboard_on_date.get_content(time_travel_date)

top100_playlist = spotify.create_playlist(time_travel_date)
spotify.add_tracks_playlist(top100_titles, top100_playlist)
