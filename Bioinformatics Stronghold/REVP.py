with open('rosalind_revp.txt','r') as file:
    lines = file.readlines()
    DNA_str = ''
    for line in lines:
        if line[0] != '>':
            DNA_str += line.strip()
    ATGC = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    def rev_pal(str1, str2):
        rev_str2 = ''.join([ATGC[x] for x in str2[::-1]])
        if str1 == rev_str2:
            return True
        else:
            return False
    length = [int(x) for x in range(4,13,2)]
    for i in length:
        n = int(i / 2)
        for pos in range(len(DNA_str)-1):
            str1 = DNA_str[pos:pos+n]
            str2 = DNA_str[pos+n:pos+i]
            if rev_pal(str1, str2):
                print(pos+1, i, sep=' ')
