file = open('rosalind_sseq.txt','r')
lines = file.readlines()
sequences = []
for line in lines:
    if line[0] == '>':
        s = ''
        sequences.append(s)
    else:
        s = line.strip()
        sequences[-1] += s

s = sequences[0]
m = len(s)
t = sequences[1]
n = len(t)
pos = 0
for i in range(m):
    if pos == n:
        break
    if s[i] == t[pos]:
        print(i+1, end=' ')
        pos += 1
