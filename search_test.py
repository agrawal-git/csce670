from search import Search

searchobj = Search("TheRealCaverlee","south")
result = searchobj.search()
for tweet in result:
	print tweet['text']
