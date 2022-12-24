from itertools import product

with open('rosalind_lexf.txt','r') as file:
    lines = file.readlines()
    str_list = lines[0].split()
    num = int(lines[1])
    combs = [''.join(comb) for comb in product(str_list, repeat=num)]
    print(*combs, sep='\n')
