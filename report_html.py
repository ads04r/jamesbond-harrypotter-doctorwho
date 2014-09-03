#!/usr/bin/python

import sys, json, string

jsontxt = sys.stdin.read().decode('utf8', 'ignore')

people = json.loads(jsontxt)
k = people.keys()
c = len(k)
max = 0
for i in range(0, c):
	id = k[i]
	people[id]['moviecount'] = len(people[id]['movies'])
	if people[id]['moviecount'] > max:
		max = people[id]['moviecount']

for i in range(2, max + 1):
	print "<table>"

	for j in range(0, c):
		id = k[j]
		if people[id]['moviecount'] == i:
			movielist = string.capwords(', '.join(people[id]['movies']).replace("_", " "))
			print '<tr><td><a href="http://www.imdb.com/name/nm' + id + '/">' + people[id]['name'] + '</a></td><td>(' + movielist + ')</td></tr>'

	print "</table>"

