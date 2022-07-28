file = open('rosalind_mer.txt','r')
lines = file.readlines()
n = int(lines[0].strip())
A = [int(i) for i in lines[1].strip().split()]
m = int(lines[2].strip())
B = [int(i) for i in lines[3].strip().split()]
C = []
i,j = 0,0
while i < n or j < m:
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    elif A[i] > B[j]:
        C.append(B[j])
        j += 1
    else:
        C += [A[i], B[j]]
        i += 1
        j += 1
    if i == n and j < m:
        C += B[j:m]
        break
    elif j == m and i < n:
        C += A[i:n]
        break
print(*C)
