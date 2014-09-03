from imdb import IMDb
from json import dumps
import sys

ia = IMDb()

movies = {}
movies['doctor_who'] = ['0056751', '0116118', '0436992'] # Doctor Who
movies['james_bond'] = ['0055928', '0057076', '0058150', '0059800', '0062512', '0064757', '0066995', '0070328', '0071807', '0076752', '0079574', '0082398', '0086034', '0090264', '0093428', '0097742', '0113189', '0120347', '0143145', '0246460', '0381061', '0830515', '1074638'] # James Bond
movies['harry_potter'] = ['0241527', '0295297', '0304141', '0330373', '0373889', '0417741', '0926084', '1201607'] # Harry Potter
# movies['downton_abbey'] = ['1606375'] # Downton Abbey

# I'm well aware that Doctor Who isn't a movie, but I don't care about semantics!

people = {}

for moviegroupid in movies.keys():
	moviegroup = movies[moviegroupid]
	for movieid in moviegroup:
		movie = ia.get_movie(movieid)
		if not(movie['kind'] == 'tv series'):
			sys.stderr.write(movie['title'] + '\n')
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
					episodeinfo = ia.get_movie(episodeimdbid)
					sys.stderr.write(episode['title'] + '\n')
					if 'cast' in episodeinfo.keys():
						for actor in episodeinfo['cast']:
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
						sys.stderr.write(" ... cast not found\n")
print dumps(people)
