file = open('rosalind_pmch.txt','r')
lines = file.readlines()
rna_str = ''
for line in lines:
    if lines != '>':
        rna_str += line.strip()

AT_content = rna_str.count('A')
GC_content = rna_str.count('G')

def Poss(number):
    if number == 1:
        return 1
    else:
        return number * Poss (number-1)

n1 = Poss(AT_content)
n2 = Poss(GC_content)
n = n1 * n2
print(n)
