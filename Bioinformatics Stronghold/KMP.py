with open('rosalind_kmp.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
P = []
n = len(seq)
for i in range(n):
    if i == 0:
        P.append(0)
    else:
        while k > 0 and seq[k] != seq[  ]
        s = 0
        for k in range(1, (i+1)//2):
            if seq[0: k] == seq[i-k+1: i+1]:
                s = k
        P.append(s)
print(*P, end = ' ')
