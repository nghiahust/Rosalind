file = open('rosalind_long.txt', 'r')
lines = file.readlines()
dna_str = []
for line in lines:
    if line[0] == '>':
        dna_str.append('')
    else:
        dna_str[-1] += line.strip()

def comp(dna1, dna2):
    len1 = len(dna1)
    len2 = len(dna2)
    for i in range(len1):
        fraq1 = dna1[i::]
        fraq2 = dna2[:len2-i:]
        if fraq1 == fraq2:
            return len(fraq1)
    return 0

super_str = ''
str_status = [False] * len(dna_str)
for i in range(len(dna_str)):
    comp_len = 0
    for j in range(i, len(dna_str)):
        distance = comp(dna_str[i], dna_str[j])
        if distance > comp_len and str_status[j] == False:
            comp_len = distance
            overlap = j
    str_status[overlap] = True


file.close()
