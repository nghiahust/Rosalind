with open('rosalind_ini4.txt','r') as file:
    numbers = [int(x) for x in file.readline().split()]
    a, b = numbers
    n = 0
    for i in range(a, b+1):
        if i % 2 == 1:
            n += i
    print(n)
