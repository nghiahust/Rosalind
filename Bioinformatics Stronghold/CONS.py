with open('rosalind_cons.txt','r') as file:
    lines = file.readlines()
    seq_list = []
    seq = ''
    for line in lines:
        if line[0] == '>':
            seq = ''
            for line2 in lines[lines.index(line)+1::]:
                if line2[0] == '>':
                    break
                else:
                    seq += line2.strip()
            seq_list.append(seq)
    profile = []
    consensus = ''
    for i in range(len(seq_list[0])):
        nu_count = {
                'A':0,
                'C':0,
                'G':0,
                'T':0
                }
        for seq in seq_list:
            nu_count[seq[i]] += 1
        consensus += max(nu_count, key= lambda x: nu_count[x])
        profile.append(nu_count)
    print(consensus)
    for nu in ['A', 'C', 'G', 'T']:
        print(nu, end=': ')
        for count in profile:
            print(count[nu], end=' ')
        print('\n')
