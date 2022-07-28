file = open('rosalind_ddeg.txt','r')
lines = file.readlines()
file.close()
n = int(lines[0].strip().split()[0])
edges = [[int(i) for i in line.strip().split()] for line in lines[1::]]
deg = [0] * n
for edge in edges:
    for i in edge:
        deg[i-1] += 1
ddeg = [0] * n
for i in range(n):
    for edge in edges:
        if i+1 in edge:
            for j in edge:
                if i+1 != j:
                    ddeg[i] += deg[j-1]
print(*ddeg)
