import itertools
file = open('rosalind_kmer.txt','r')
seqs = ''.join([line.strip() for line in file.readlines() if line[0] != '>'])
file.close()
k = 4
n = len(seqs)
combi = itertools.product(['A','C','G','T'], repeat=k)
count= {}
for i in combi:
    seq = ''.join(i)
    count[seq] = 0
for i in range(n-k+1):
    seq = seqs[i:i+k]
    count[seq] += 1
print(*list(count.values()), end=' ')
