from itertools import permutations

with open('rosalind_perm.txt', 'r') as file:
    n = int(file.readline())
    perm = permutations([i for i in range(1, n+1)])
    list_perm = list(perm)
    print(len(list_perm))
    for i in list_perm:
        print(*i, sep=' ')
