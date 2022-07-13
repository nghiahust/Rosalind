from Bio import Entrez
Entrez.email = 'hatrongnghia@outlook.com'
handle = Entrez.esearch(db='nucleotide', term='Anthoxanthum')
print(Entrez.read(handle))
