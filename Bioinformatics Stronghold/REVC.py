with open('rosalind_revc.txt','r') as f:
    line = f.readline()
    revc = ''
    for char in line:
        if char == 'A':
            revc += 'T'
        elif char == 'T':
            revc += 'A'
        elif char == 'G':
            revc += 'C'
        elif char == 'C':
            revc += 'G'
    print(revc[::-1])
