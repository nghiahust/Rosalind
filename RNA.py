with open('rosalind_rna.txt','r') as f:
    line = f.readline().replace('T', 'U')
    print(line)
