with open('rosalind_orf.txt','r') as file:
    lines = file.readlines()
    dna_str = ''
    for line in lines:
        if line[0] != '>':
            dna_str += line.strip()
    ATGC = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    reverse_str = ''.join([ATGC[x] for x in dna_str[::-1]])

    DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A", "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G", "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I", "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M", "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W", "TAT": "Y", "TAC": "Y",
    "TAA": "STOP", "TAG": "STOP", "TGA": "STOP"
                }
    def dna_translate(DNA):
        ORF = []
        i = 0
        dna_len = len(DNA)
        for i in range(dna_len-4):
            start = DNA[i:i+3]
            if start == 'ATG':
                j = i + 3
                stop = DNA[j:j+3]
                protein = ['M']
                aa = DNA_Codons[stop]
                while aa != 'STOP' and j <= dna_len-7:
                    protein.append(aa)
                    j += 3
                    stop = DNA[j:j+3]
                    aa = DNA_Codons[stop]
                if aa == 'STOP':
                    pro_seq = ''.join(protein)
                    ORF.append(pro_seq)
        return ORF

    print(*dna_translate(dna_str), sep='\n')
    for seq in dna_translate(reverse_str):
        if seq not in dna_translate(dna_str):
            print(seq)
