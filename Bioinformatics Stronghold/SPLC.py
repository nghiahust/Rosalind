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
with open('rosalind_splc.txt', 'r') as file:
    lines = file.readlines()
    dna_list = []
    for line in lines:
        if line[0] == '>':
            dna_list.append('')
        else:
            dna_list[-1] += line.strip()

    dna_str = dna_list[0]
    for sub_str in dna_list[1::]:
        dna_str = dna_str.replace(sub_str, '')
    protein = ''
    for i in range(0,len(dna_str),3):
        if DNA_Codons[dna_str[i:i+3]] != 'STOP':
            protein += DNA_Codons[dna_str[i:i+3]]
    print(protein)
