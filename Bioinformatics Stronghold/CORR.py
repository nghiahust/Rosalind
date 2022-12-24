file = open('rosalind_corr.txt','r')
lines = file.readlines()
file.close()
seqs = [line.strip() for line in lines if line[0] != '>']
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def revComp(seq):
    return ''.join([complement[i] for i in seq[::-1]])

def hammDis(seq1, seq2):
    n = len(seq1)
    result = 0
    for i in range(n):
        if seq1[i] != seq2[i]:
            result += 1
    return result
n = len(seqs)
correct = []
for i in range(n):
    for j in range(i+1, n):
        if seqs[i] == seqs[j] or seqs[i] == revComp(seqs[j]):
            correct.append(seqs[i])
            correct.append(revComp(seqs[i]))
correct = set(correct)
for i in range(n):
    if seqs[i] not in correct:
        for seq in correct:
            if hammDis(seqs[i], seq) == 1:
                print(f"{seqs[i]}->{seq}")
