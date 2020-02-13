#WorkInPlaylist

import requests
import json
from secrets import spotify_user_id

class CreatePlaylist:
		def __unit__(self):
			self.user_id=
				
		#Step1: Login To Youtube
		def get_youtube_client(self):
			
		#Step2: Grab Liked Videos
		def get_liked_videos(self):
			
		#Step3: Create a New Playlist
		def create_playlist(self):
			request_body=json.dumps({
				"name":"Youtube Liked Videos"
				"description":"Music From Liked Youtube Videos"
				"public":"True"

				})

			query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
			response = requests.post(
					query,
					data=request_body,
					headers=(
						"Content-Type": "application/json",
						"Authorization": "Bearer()".format(spotify_token)
					
				)

				response_json= response.json()

			
		#Step4: Search for the Song
		def get_spotify_uri(self, song_name, artist):

			query= "https://api.spotify.com/v1/search?query=track%3A()+artist%3A()&type=track&offset=0&limit=20".format()
				song_name,
				artist

			response= requests.get()
				query,
				headers=(
					"Content-Type":"application/json"
					"Authorization":"Bearer {}".format(spotify_token))

			
		#Step5: Add Song to Spotify Playlist
		def add_song_to_playlist(self):
			
			
