file = open('rosalind_cat.txt')
lines = file.readlines()
sequence = ''
for line in lines:
    if line[0] != '>':
        sequence += line.strip()

def cat(seq, low, high, dp):
    augc = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
    n = high - low + 1
    if n % 2 == 1:
        return 0
    elif low >= high or high >= len(seq) or high < 0:
        return 1
    elif (low, high) in dp:
        return dp[(low, high)]
    else:
        target = augc[seq[low]]
        result = 0
        for i in range(low+1, high+1, 2):
            if seq[i] == target:
                left = cat(seq, low+1, i-1, dp)
                right = cat(seq, i+1, high, dp)
                result += (left * right)
        dp[(low, high)] = result
        return result
print(cat(sequence, 0, len(sequence)-1, {})%1000000)
