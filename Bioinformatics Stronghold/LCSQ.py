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
C = [[0] * m] * n
def 

#def LCS(seq1, seq2, n, m):
#    if n == 0 or m == 0:
#        break
#    else:
#        if 
#print(LCS(seq1, seq2, n, m))
