with open('rosalind_dna.txt','r') as f:
    line = f.readline()
    print("%s %s %s %s" % (line.count('A'), line.count('C'), line.count('G'), line.count('T')))
