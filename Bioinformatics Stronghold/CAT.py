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
