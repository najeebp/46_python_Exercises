import urllib
import json
import os
def downlode(username):
	listt = []
	i = 1
	f = urllib.urlopen('https://api.github.com/users/' + username + '/repos')
	x = f.readline()
	y = json.loads(x)
	for k in y:
		listt.append(k['html_url'])
	for j in listt:
		print urllib.urlretrieve(j,os.path.join(os.path.abspath('.'),'rep%d'%i))	
		i +=1	  

downlode('najeebp')	