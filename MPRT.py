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
            seq_dict[id] += seq.seq

    motif = 'N{P}[ST]{P}'
    for seq in seq_dict:
        sequence = seq_dict[seq]
        i = 0 # Location on sequence
        j = 0 # Location on motif
        checker = False # Check if motif exist in sequence
        while i <= len(sequence):
            if seq[i] = motif[j]:
                pass
                j += 1
            elif motif[j] == '{':
                    while motif[j] != '}'

            elif
            i += 1
