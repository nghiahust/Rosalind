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
print(n)
i,j = 0,0
while i < n or j < n:
    print(i, j)
    if seq1[i] == seq2[j]:
        subseq += seq1[i]
        i += 1
        j += 1
    else:
        j+=1
    print(subseq)

