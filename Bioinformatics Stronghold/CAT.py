file = open('rosalind_cat.txt')
lines = file.readlines()
sequence = ''
for line in lines:
    if line[0] != '>':
        sequence += line.strip()
n = len(sequence)
for i in range(1, n+1):

