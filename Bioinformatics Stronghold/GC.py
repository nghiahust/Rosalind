with open('rosalind_gc.txt','r') as file:
    lines = file.readlines()
    seq_data = {}
    for line in lines:
        if line[0] == '>':
            seq_name = line[1:-1:]
            seq_data[seq_name] = ''
            for seq in lines[lines.index(line)+1::]:
                if seq[0] == '>':
                    break
                else:
                    seq_data[seq_name] += seq[:-1:]
    max_ratio = 0
    max_id = ''
    for i in seq_data.keys():
        seq_len = len(seq_data[i])
        gc_content = seq_data[i].count('C') + seq_data[i].count('G')
        gc_ratio = gc_content / seq_len * 100
        if gc_ratio > max_ratio:
            max_ratio = gc_ratio
            max_id = i
    print(max_id)
    print(max_ratio)