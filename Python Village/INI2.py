with open('rosalind_ini2.txt','r') as file:
    my_numbers = file.readline().split()
    x = int(my_numbers[0])
    y = int(my_numbers[1])
    z = x*x + y*y
    print(z)