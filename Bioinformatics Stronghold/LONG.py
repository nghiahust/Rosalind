with open('rosalind_long.txt', 'r') as file:
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
                return(len(fraq1))
    matrix =[[comp(i,j) for i in dna_str] for j in dna_str]
    print(*matrix, sep='\n')
