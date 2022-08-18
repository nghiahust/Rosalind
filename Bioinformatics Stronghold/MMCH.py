with open('rosalind_mmch.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
n = len(seq)
count_A = seq.count('A')
count_U = seq.count('U')
count_G = seq.count('G')
count_C = seq.count('C')
combiAU = count_A * count_U
combiGC = count_G * count_C
result = combiAU * combiGC
print(result)
