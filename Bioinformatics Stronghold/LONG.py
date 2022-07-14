file = open('rosalind_long.txt', 'r')
lines = file.readlines()
dna_str = []
for line in lines:
    if line[0] == '>':
        dna_str.append('')
    else:
        dna_str[-1] += line.strip()

# Greedy algorithm for SCS
def EDGE(str1, str2):
    for i in range(len(str2), 0, -1):
        if str1[len(str1)-i:] == str2[:i]:
            return i
    return 0
def OVL(str1, str2):
    edge1 = EDGE(str1, str2)
    edge2 = EDGE(str2, str1)
    if str1 in str2 or str2 in str1:
        return -1
    elif edge1 > edge2:
        return edge1
    elif edge2 > edge1:
        return edge2
    else:
        return edge1
def ASSEM(str1, str2):
    assemble = ''
    if EDGE(str1, str2) > EDGE(str2, str1):
        assemble = str1 + str2[EDGE(str1, str2):]
    else:
        assemble = str2 + str1[EDGE(str2, str1):]
    return assemble

genome = dna_str
while len(genome) > 1:
    max = 0
    index1 = 0
    index2 = 0
    for i in range(len(genome)):
        for j in range(i, len(genome)):
            if OVL(genome[i], genome[j]) > max:
                max = OVL(genome[i], genome[j])
                index1 = i
                index2 = j
    genome[index1] = ASSEM(genome[index1], genome[index2])
    genome.remove(genome[index2])
with open('result_long.txt','w') as result:
    result.write(genome[0])


file.close()
