file = open('rosalind_cat.txt')
lines = file.readlines()
sequence = ''
for line in lines:
    if line[0] != '>':
        sequence += line.strip()
n = len(sequence) // 2

def CAT(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        c = 0
        for k in range(1, n+1):
            c += CAT(k-1) * CAT(n-k)
        return c

print(CAT(n))
