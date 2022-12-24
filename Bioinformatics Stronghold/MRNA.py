with open('rosalind_mrna.txt', 'r') as file:
    lines = file.readlines()
    protein_str = ''
    for line in lines:
        protein_str += line.strip()

    reverse_codon = {'A': {'GCA', 'GCC', 'GCU', 'GCG'}, 'C': {'UGC', 'UGU'}, 'E': {'GAG', 'GAA'}, 'D': {'GAU', 'GAC'}, 'G': {'GGU', 'GGG', 'GGA', 'GGC'}, 'F': {'UUU', 'UUC'}, 'I': {'AUA', 'AUC', 'AUU'}, 'H': {'CAC', 'CAU'}, 'K': {'AAG', 'AAA'}, '*': {'UAA', 'UGA', 'UAG'}, 'M': {'AUG'}, 'L': {'CUU', 'CUG', 'CUC', 'CUA', 'UUG', 'UUA'}, 'N': {'AAU', 'AAC'}, 'Q': {'CAA', 'CAG'}, 'P': {'CCU', 'CCG', 'CCA', 'CCC'}, 'S': {'UCU', 'AGC', 'UCG', 'UCC', 'UCA', 'AGU'}, 'R': {'AGG', 'CGC', 'AGA', 'CGA', 'CGG', 'CGU'}, 'T': {'ACC', 'ACA', 'ACG', 'ACU'}, 'W': {'UGG'}, 'V': {'GUC', 'GUA', 'GUG', 'GUU'}, 'Y': {'UAC', 'UAU'}}
    number = 1
    for i in range(len(protein_str)):
        if number > 1000000:
            number = number % 1000000
        number = number * len(reverse_codon[protein_str[i]])
    number = (number * len(reverse_codon['*']) % 1000000)
    print(number)
