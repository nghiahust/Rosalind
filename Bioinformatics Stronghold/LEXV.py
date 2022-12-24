import itertools
with open('rosalind_lexv.txt','r') as file:
    lines = file.readlines()
char_list = lines[0].strip().split()
n = int(lines[1])
lexv = []
for i in range(1, n+1):
    c = list(itertools.product(char_list, repeat=i))
    for x in c:
        lexv.append(''.join(x))
print(*sorted(lexv, key=lambda x:[char_list.index(a) for a in x]),sep='\n')
