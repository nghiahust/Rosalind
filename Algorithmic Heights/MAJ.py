file = open('rosalind_maj.txt','r')
lines = file.readlines()
k = lines[0].strip().split()[0]
n = lines[0].strip().split()[1]
A = [[int(i) for i in line.strip().split()] for line in lines[1::]]

def MAJ(array):
    num_dict = {}
    for i in array:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    for i in num_dict:
        if num_dict[i] > len(array) / 2:
            return i
    return -1
for i in A:
    print(MAJ(i), end=' ')
