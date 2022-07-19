file = open('rosalind_pper.txt','r')
line = file.readline().split()
n = int(line[0])
k = int(line[1])
print(n, k)
result = 1
for i in range(k):
    print(n-i)
    result *= (n - i)
print(result % 1000000)
