class Node:
    def __init__(self,val=0,left=None,right=None):
        self.data = val
        self.left = left
        self.right = right
    def __mul__(self1,self2):
        return self1.data * self2.data

def array_to_tree(data):
    nodes = []
    for el in data:
        nodes.append(Node(el))

    for i in range(len(nodes)):
        if 2*i+1<len(nodes):
            nodes[i].left = nodes[2*i+1]
        if 2*i+2<len(nodes):
            nodes[i].right = nodes[2*i+2]
    return nodes

