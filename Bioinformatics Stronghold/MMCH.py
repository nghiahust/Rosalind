from math import factorial
with open('rosalind_mmch.txt','r') as file:
    lines = file.readlines()
seq = ''.join([line.strip() for line in lines if line[0] != '>'])
n = len(seq)
A, U, G, C = 22, 19, 21, 21
#for base in seq:
#    match base:
#        case 'A':
#            A += 1
#        case 'U':
#            U += 1
#        case 'G':
#            G += 1
#        case 'C':
#            C += 1
print(A, U, G, C)
AU = factorial(max(A, U)) / factorial(max(A, U) - min(A, U))
GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
print(int(AU * GC))
