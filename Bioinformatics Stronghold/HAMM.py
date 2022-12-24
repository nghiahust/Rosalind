with open('rosalind_hamm.txt','r') as file:
    lines = file.readlines()
    string1 = lines[0]
    string2 = lines[1]
    hamm_dist = 0
    for i in range(len(string1) - 1):
        if string1[i] != string2[i]:
            hamm_dist += 1
    print(hamm_dist)