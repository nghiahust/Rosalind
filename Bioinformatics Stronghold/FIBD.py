with open('rosalind_fibd.txt','r') as file:
    line = file.readline().split()
    n = int(line[0])
    m = int(line[1])
    rabbits = [1,1]
    for month in range(3, n+1):
        if month < m+1:
            rabbits.append(rabbits[-1] + rabbits[-2])
        elif month == m+1:
            rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[0])
        else:
            rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[-m-1])
        print(len(rabbits), month, rabbits[-1])
    print(rabbits[-1])