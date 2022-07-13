from Bio.Seq import Seq
with open('rosalind_ini.txt', 'r') as file:
    line = file.readline()
    my_seq = Seq(line.strip())
    for i in ['A', 'C', 'G', 'T']:
        print(my_seq.count(i), end=' ')
