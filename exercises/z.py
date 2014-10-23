import urllib
response = urllib.requests.urlopen(' http://www.puzzlers.org/pub/wordlists/unixdict.txt')
html = response.read()
print html