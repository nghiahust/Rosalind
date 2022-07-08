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
            print(seq.seq)
            seq_dict[id] += seq.seq

    gly_motif = 'N{O}[ST]{P}'
    len_motif = 5
    for seq in seq_dict:
        sequence = seq_dict[seq]
        for i in range(len(sequence)-len_motif+1):
            checker = False
            seq_pos = 0
            motif_pos = 0
            for j in gly_motif:
                if not j.isalpha():

