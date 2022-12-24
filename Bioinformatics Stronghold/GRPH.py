with open('rosalind_grph.txt','r') as file:

    # Read data from file to sequences dictionary
    lines = file.readlines()
    sequences = {}
    for line in lines:
        if line[0] == '>':
            sequence = ''
            for seq in lines[lines.index(line)+1::]:
                if seq[0] == '>':
                    break
                else:
                    sequence += seq.strip()
            sequences[line.strip()] = sequence

    # Making the matrix for connection O3
    k = 3
    for key1 in sequences:
        seq1 = sequences[key1]
        for key2 in sequences:
            seq2 = sequences[key2]
            if seq1 != seq2 and seq1[-k:] == seq2[:k]:
                print(key1[1::], key2[1::])
