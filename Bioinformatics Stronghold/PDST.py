with open('rosalind_pdst.txt', 'r') as file:
    lines = file.readlines()
seqs = []
for line in lines:
    if line[0] == '>':

