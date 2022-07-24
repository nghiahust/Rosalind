file = open('rosalind_cat.txt')
lines = file.readlines()
sequence = ''
for line in lines:
    if line[0] != '>':
        sequence += line.strip()
n = len(sequence)
catNum = []
for i in range(1, n//2+1):
    if i == 1:
        catNum.append(1)
    elif i == 2:
        catNum.append(2)
    else:
        result = 0
        for j in range(1, len(catNum)):
            print(i,j)
            result += catNum[j-1] * catNum[-1-j]
print(catNum)
