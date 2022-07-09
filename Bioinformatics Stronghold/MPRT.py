from Bio import SeqIO
import requests
from io import StringIO

with open('rosalind_mprt.txt','r') as file:
    lines = file.readlines()
    seq_dict = {}
    for line in lines:
        id = line[0:6]
        seq_dict[id] = ''
        link = "http://www.uniprot.org/uniprot/" + id + ".fasta"
        data = requests.get(link).text
        fasta_iterator = SeqIO.parse(StringIO(data), "fasta")
        for seq in fasta_iterator:
            seq_dict[id] += str(seq.seq)

    motif = 'N{P}[ST]{P}'
    len_motif = 0
    for i in motif:
        if i.isalpha():
            len_motif += 1
    for seq in seq_dict: # Loop in all given sequences
        sequence = seq_dict[seq]
        loc_list = []
        for i in range(len(sequence)+1-len_motif):
            j = i
            k = 0
            checker = False
            while k < len(motif):
                if sequence[j] == motif[k]:
                    checker = True
                    j += 1
                    k += 1
                elif motif[k] == '{':
                    temp = []
                    k += 1
                    while motif[k] != '}':
                        temp.append(motif[k])
                        k += 1
                    if sequence[j] not in temp:
                        checker = True
                        j += 1
                        k += 1
                    else:
                        checker = False
                        break
                elif motif[k] == '[':
                    temp = []
                    k += 1
                    while motif[k] != ']':
                        temp.append(motif[k])
                        k += 1
                    if sequence[j] in temp:
                        checker = True
                        j += 1
                        k += 1
                    else:
                        checker = False
                        break
                else:
                    checker = False
                    break
            if checker == True:
                loc_list.append(i+1)
        if len(loc_list) > 0:
            for line in lines:
                if seq == line[0:6]:
                    print(line.strip())
            print(*loc_list)
