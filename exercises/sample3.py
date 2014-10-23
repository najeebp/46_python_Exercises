import urllib
import requests
import os
def downlode(username):
	listt = []
	i = 1
	f = requests.get('https://api.github.com/users/' + username + '/repos')
	x = f.readline()
	print x
	y = requests.get(x)
	for k in y:
		listt.append(k['html_url'])
	for j in listt:
		print urllib.urlretrieve(j,os.path.join(os.path.abspath('.'),'rep%d'%i))	
		i +=1	  

downlode('najeebp')	