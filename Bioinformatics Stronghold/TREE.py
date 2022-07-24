file = open('rosalind_tree.txt','r')
lines = file.readlines()
file.close()
n = int(lines[0])
my_graph = []
for i in range(1, len(lines)):
    s = [int(x) for x in lines[i].strip().split()]
    my_graph.append(s)
branches = []
for edge in my_graph:
    if len(branches) == 0:
        branches.append(edge)
    else:
        add_edge = True
        for branch in branches:
            if edge[0] in branch:
                branch.append(edge[1])
                add_edge = False
                break
            elif edge[1] in branch:
                add_edge = False
                branch.append(edge[0])
                break
        if add_edge == True:
            branches.append(edge)
        continue
connected_node = 0
for branch in branches:
    connected_node += len(branch)
unconnected_node = n - connected_node
result = len(branches) - 1 + unconnected_node
print(result)
