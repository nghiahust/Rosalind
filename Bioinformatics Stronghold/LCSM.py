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

    srt_seqs = sorted(sequences, key=len)
    min_seq = srt_seqs[0]
    for i in range(len(min_seq), 1, -1):
        for j in range(len(min_seq)-i+1):
            ref_seq = min_seq[j:j+i]
            check_sub = False
            for seq in sequences[1::]:
                if ref_seq in seq:
                    check_sub = True
                else:
                    check_sub = False
                    break
            if check_sub == True:
                print(ref_seq)
                break
        if check_sub == True:
            break
