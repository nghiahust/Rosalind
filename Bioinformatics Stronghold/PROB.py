import math
file = open('rosalind_prob.txt','r')
lines = file.readlines()
s = lines[0].strip()
A = [float(i) for i in lines[1].strip().split()]
AT = s.count('A') + s.count('T')
GC = s.count('G') + s.count('C')
result = []
for i in A:
    prob = (((1-i)/2)**AT)*((i/2)**GC)
    common_log = math.log10(prob)
    result.append('%0.3f'%common_log)
print(*result,sep=' ')
