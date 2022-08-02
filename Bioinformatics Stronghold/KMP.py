with open('rosalind_kmp.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
n = len(seq)
P = [0] * n
k = 0
for i in range(1, n):
    for j in range(1, n-i+1):
        if seq[:i] == seq[j:j+i]:
            P[j+i-1] = len(seq[:i])
            k = len(seq[:i])
    if k < len(seq[:i]):
        break
print(*P, end=' ')
