file = open('rosalind_tran.txt','r')
lines = file.readlines()
file.close()
sequences = []
for line in lines:
    if line[0] == '>':
        s = ''
        sequences.append(s)
    else:
        sequences[-1] += line.strip()
s1 = sequences[0]
s2 = sequences[1]
transitions = {'A':'G', 'C':'T', 'G':'A', 'T':'C'}
transversions = {'A':['C','T'], 'C':['A','G'], 'G':['C','T'], 'T':['A','G']}
n = 0 # transitions
m = 0 # transversions
for i in range(len(s1)):
    if transitions[s1[i]] == s2[i]:
        n += 1
    elif s2[i] in transversions[s1[i]]:
        m += 1
    else:
        continue
print('%0.11f'%(n/m))
