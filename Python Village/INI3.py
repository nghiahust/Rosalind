with open('rosalind_ini3.txt', 'r') as file:
    lines = file.readlines()
    my_str = lines[0]
    numbers = [int(x) for x in lines[1].split()]
    a, b, c, d = numbers
    str_1 = my_str[a:b+1]
    str_2 = my_str[c:d+1]
    print("{0} {1}".format(str_1, str_2))
