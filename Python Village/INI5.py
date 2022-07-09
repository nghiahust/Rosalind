with open('rosalind_ini5.txt','r') as file:
    lines = file.readlines()
    for line in lines[1::2]:
        print(line.strip())
