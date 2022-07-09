with open('rosalind_fib.txt','r') as file:
    my_list = file.readline().split()
    n = int(my_list[0])
    k = int(my_list[1])
    def rabbits(a, b):
        if a == 2 or a == 1:
            return 1
        else:
            total_rab = rabbits(a - 1, b) + rabbits(a - 2, b) * b
            return total_rab
    print(rabbits(n, k))
