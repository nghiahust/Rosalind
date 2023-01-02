import urllib
code = "Q7Z7W5"
data = urllib.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt").read()
print(data)

print('Nghia dep trai')
for i in range(0,10):
    print(i)
