from imdb import IMDb
from json import dumps
import sys

ia = IMDb()

movies = {}
# movies['doctorwho'] = ['0056751', '0116118', '0436992'] # Doctor Who
movies['downton'] = ['1606375'] # Downton Abbey
movies['bond'] = ['0055928', '0057076', '0058150', '0059800', '0062512', '0064757', '0066995', '0070328', '0071807', '0076752', '0079574', '0082398', '0086034', '0090264', '0093428', '0097742', '0113189', '0120347', '0143145', '0246460', '0381061', '0830515', '1074638'] # James Bond

# I'm well aware that Doctor Who isn't a movie, but I don't care about semantics!

people = {}

for moviegroupid in movies.keys():
	moviegroup = movies[moviegroupid]
	for movieid in moviegroup:
		movie = ia.get_movie(movieid)
		if not(movie['kind'] == 'tv series'):
			for actor in movie['cast']:
				id = actor.personID
				name = actor['name']
				if id in people:
					item = people[id]
				else:
					item = {}
					item['id'] = id
					item['name'] = name
					item['movies'] = []
				if moviegroupid not in item['movies']:
					item['movies'].append(moviegroupid)
				people[id] = item
		else:
			ia.update(movie, 'episodes')
			for seriesid in movie['episodes'].keys():
				series = movie['episodes'][seriesid]
				for episodeid in series.keys():
					episode = series[episodeid]
					episodeimdbid = episode.movieID
					episode = ia.get_movie(episodeimdbid)
					sys.stderr.write(episode['title'])
					if 'cast' in episode:
						for actor in episode['cast']:
							id = actor.personID
							name = actor['name']
							if id in people:
								item = people[id]
							else:
								item = {}
								item['id'] = id
								item['name'] = name
								item['movies'] = []
							if moviegroupid not in item['movies']:
								item['movies'].append(moviegroupid)
							people[id] = item
					else:
						sys.stderr.write(" ... cast not found")
print dumps(people)
