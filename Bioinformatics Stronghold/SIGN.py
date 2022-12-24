from itertools import permutations as Perm
file = open('rosalind_sign.txt','r')
line = file.readline()
n = int(line.strip())

sign_list = list(Perm([i for i in range(-n,n+1) if i != 0],n))
abs_list = [[abs(i) for i in a_list] for a_list in sign_list]
abs_set = [set(x) for x in abs_list]
result = []
for i in range(len(sign_list)):
    if len(sign_list[i]) == len(abs_set[i]):
        result.append(sign_list[i])
print(len(result))
for i in result:
    for j in i:
        print(j, end=' ')
    print('\n')
