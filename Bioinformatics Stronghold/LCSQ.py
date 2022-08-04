with open('rosalind_lcsq.txt','r') as file:
    lines = file.readlines()
seqs = []
for line in lines:
    if line[0] == '>':
        seqs.append('')
    else:
        seqs[-1] += line.strip()
seq1 = seqs[0]
seq2 = seqs[1]
subseq = ''
n = len(seq1)
m = len(seq2)
i, j = 0, 0 # Current possition on seq1 and seq2
while i < n or j < m:
    k = min(i, j)
    while k < max(i, j):        
print(subseq)
