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
while i < n and i < m:
    li = i
    lj = j
    while li < n-1 or seq1[li] != seq2[j]:
        li += 1
        print(i, j, li, lj, seq1[li], seq2[j])
    while lj < m-1 or seq1[i] != seq2[lj]:
        lj += 1
    if li - i < lj - j:
        subseq += seq1[li]
        i = li+1
        j += 1
    elif li - i > lj - j:
        subseq += seq2[lj]
        i += 1
        j = lj+1
    else:
        i = li+1
        j = lj+1
print(subseq)
