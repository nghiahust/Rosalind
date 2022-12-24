with open('rosalind_subs.txt','r') as file:
    lines = file.readlines()
    t = lines[0]
    s = lines[1]
    print(s)
    for i in range(len(t) - len(s) -1):
        if t[i:i+len(s)] == s:
            print(i+1,end=' ')