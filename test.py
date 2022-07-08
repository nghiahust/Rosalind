import urllib
code = "Q7Z7W5"
data = urllib.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt").read()
print(data)
