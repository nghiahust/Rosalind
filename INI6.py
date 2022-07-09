with open('rosalind_ini6.txt','r') as file:
    line = file.readline().strip().split()
    my_dict = {}
    for i in line:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for key, value in my_dict.items():
        print(key, value)
