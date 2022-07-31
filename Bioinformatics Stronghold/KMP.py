with open('rosalind_kmp.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
P = []
n = len(seq)
for i in range(n):
    print(i)
    if i == 0:
        P.append(0)
    else:
        s = 0
        for k in range(1, (i+1)//2):
            print(i, k, seq[0:k], 'vs.', seq[i-k:i])
            if seq[0: k] == seq[i-k: i]:
                s = k
            else:
                break
        P.append(s)
print(*P, end = ' ')
