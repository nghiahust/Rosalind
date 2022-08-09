import itertools
with open('rosalind_lexv.txt','r') as file:
    lines = file.readlines()
char_list = lines[0].strip().split()
n = lines[1]
print(*itertools.product(char_list, ' ', ' '))
