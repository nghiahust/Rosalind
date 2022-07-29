file = open('rosalind_2sum.txt','r')
lines = file.readlines()
k = lines[0].strip().split()[0]
n = lines[0].strip().split()[1]
A =[[int(i) for i in line.strip().split()] for line in lines[1::]]
def find2sum(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i] == -array[j]:
                return [i+1,j+1]
    return [-1]
for a in A:
    print(*find2sum(a))
