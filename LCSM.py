with open('rosalind_lcsm.txt','r') as file:

    # Input the sequences into a list
    lines = file.readlines()
    sequences = []
    for line in lines:
        if line[0] == '>':
            sequence = ''
            for seq in lines[lines.index(line)+1::]:
                if seq[0] == '>':
                    break
                else:
                    sequence += seq.strip()
            sequences.append(sequence)

    # Find the longest possible string = min len of sequences
    min_len = len(sequences[0])
    min_seq = sequences[0]
    for sequence in sequences:
        if len(sequence) < min_len:
            min_len = len(sequence)

    # Making list of possible substring from all sequences
    seq_list = []
    for sequence in sequences:
        sublist = []
        for i in range(2, min_len+1):
            for j in range(0, len(sequence)-i+1):
                substring = sequence[j:j+i]
                if substring not in sublist:
                    sublist.append(substring)
        seq_list.append(sublist)

    # Looping to find the sequences
    for sub in seq_list[0]:
        for seq in seqlist[1::]:
            if sub in seq:

