with open('rosalind_fibd.txt','r') as file:
    line = file.readline().split()
    n = int(line[0])
    m = int(line[1])
    def rabbit(i, j):
        print(i,j)
        if i == 1 or i == 2:
            return 1
        elif i <= j+1:
            return rabbit(i-1, j) + rabbit(i-2, j)
        else:
            return rabbit(i-1, j) + rabbit(i-2, j) - rabbit(i-j-1, j)
    print(rabbit(n, m))
