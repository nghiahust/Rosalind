from itertools import permutations as Perm
#file = open('rosalind_sign.txt','r')
#line = file.readline()
#n = int(line.strip())

#sign_list = list(Perm([i for i in range(-2,2+1) if i != 0],2))
sign_list = list(Perm(range(3), 2))
print(*sign_list, end= '\n')
print(len(sign_list))
res = [i for i in sign_list if ]
