import urllib2
request = urllib2.Request('https://api.github.com' + '/users/najeebp/repos')
result = urllib2.urlopen(request)
result.close()
for k in result:
	print k
print result