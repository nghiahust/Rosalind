from itertools import permutations as permu
with open('rosalind_mmch.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
n = len(seq)
count_nu = {}
for i in ('A','U','G','C'):
    count_nu[i] = seq.count(i)

