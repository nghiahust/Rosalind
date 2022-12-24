with open('rosalind_kmp.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
print(seq)
n = len(seq)
P = [0] * n
k = 0
for i in range(1, n):
    while k > 0 and seq[k] != seq[i]:
        k = P[k-1]
    if seq[k] == seq[i]:
        k = k + 1
    P[i] = k
print(*P, end=' ')
