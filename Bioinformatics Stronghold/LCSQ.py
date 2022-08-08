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

def LCSL(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    C = [[0] * m] * n
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                if seq1[i] == seq2[j]:
                    C[i][j] = 1
            elif seq1[i] == seq2[j]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
        print(*C, sep='\n', end='\n\n')
    return C
#print(*LCSL(seq1, seq2), sep= '\n')

def LCS(C, seq1, seq2, n, m):
    if n == 0 or m == 0:
        return ''
    if seq1[n] == seq2[m]:
        return LCS(C, seq1, seq2, n-1, m-1) + seq1[n]
    elif C[n][m-1] > C[n-1][m]:
        return LCS(C, seq1, seq2, n, m-1)
    else:
        return LCS(C, seq1, seq2, n-1, m)
print(LCS(LCSL(seq1, seq2), seq1, seq2, n-1, m-1))
