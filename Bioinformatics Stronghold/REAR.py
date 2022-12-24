with open('rosalind_rear.txt', 'r') as file:
    lines = file.readlines()
num_pair = []
for line in lines:
    if line != '\n':
        num_pair.append(line.split())

#def ham_dis(seq1, seq2):
#    l = len(seq1)
#    n = 0
#    for i in range(0, l):
#        if seq1[i] != seq2[i]:
#            n += 1
#    return n

def rev_seq(seq, p1, p2):
    rev = seq[p1:p2][::-1]
    seq_rev = seq
    for i in range(0, len(rev)):
        seq_rev[p1+i] = rev[i]
    return seq_rev

def rev_dis(seq1, seq2):
    l = len(seq1)
    n = 0
    for i in range(0, l):
        if seq1[i] != seq2[i]:
            k = seq2.index(seq1[i])
            seq2 = rev_seq(seq2, i, k+1)
            n += 1
    return n

for i in range(0, len(num_pair), 2):
    print(rev_dis(num_pair[i], num_pair[i+1]), end=' ')
