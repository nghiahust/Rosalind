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

def LCSL(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    C = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0) and seq1[i] == seq2[j]:
                C[i][j] = 1
            elif seq1[i] == seq2[j]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i-1][j], C[i][j-1])
    return C

def LCS(C, seq1, seq2, n, m):
    motif = ''
    while n * m >= 0:
        if C[n][m] == C[n-1][m]:
            n -= 1
        elif C[n][m] == C[n][m-1]:
            m -= 1
        else:
            motif = seq1[n] + motif
            n -= 1
            m -= 1
    return motif
C = LCSL(seq1, seq2)
print(LCS(C, seq1, seq2, n-1, m-1))
