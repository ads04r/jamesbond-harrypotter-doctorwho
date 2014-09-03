#!/usr/bin/python

import sys, json

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
	print str(i) + " movies/tv shows"
	print "================="

	for j in range(0, c):
		id = k[j]
		if people[id]['moviecount'] == i:
			movielist = ', '.join(people[id]['movies'])
			print people[id]['name'] + '\t(' + movielist + ')'

	print ""

print "The Doctors"
print "==========="
ids = ['0367156', '0873743', '0675727', '0048982', '0205749', '0048346', '0566809', '0001524', '0001172', '0855039', '1741002', '0000457', '0134922']
for id in ids:
	if people[id]['moviecount'] > 1:
		movielist = ', '.join(people[id]['movies'])
		print people[id]['name'] + '\t(' + movielist + ')'
print ""

print "The Bonds"
print "========="
ids = ['0000125', '0493872', '0000549', '0001096', '0000112', '0185819']
for id in ids:
	if people[id]['moviecount'] > 1:
		movielist = ', '.join(people[id]['movies'])
		print people[id]['name'] + '\t(' + movielist + ')'
print ""
