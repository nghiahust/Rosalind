with open('rosalind_pdst.txt', 'r') as file:
    lines = file.readlines()
seqs = []
for line in lines:
    if line[0] == '>':
        seqs.append('')
    else:
        seqs[-1] += line.strip()
n = len(seqs)
def pdistance(seq1, seq2):
    k = 0
    n = len(seq1)
    for i in range(n):
        if seq1[i] != seq2[i]:
            k += 1
    return round(k / n, 5)

for i in range(n):
    for j in range(n):
        print("{:.5f}".format(pdistance(seqs[i], seqs[j])),end = ' ')
    print('\n')
