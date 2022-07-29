file = open('rosalind_deg.txt','r')
lines = file.readlines()
nodes = [int(x) for line in lines for x in line.strip().split()]
nodes.pop(0)
nodes.pop(0)
nodes_set = set(nodes)
n = len(nodes_set)
print(n)
deg = [0] * n
for i in nodes:
    deg[i-1] +=1
print(*deg, end=' ')