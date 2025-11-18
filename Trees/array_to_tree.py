class Node:
    def __init__(self,val=0,left=None,right=None):
        self.data = val
        self.left = left
        self.right = right

def build_tree(data,i):
    if i>=len(data):
        return None
    root = Node(data[i])

    root.left = build_tree(data, 2 * i + 1)

    print(f'root[{i}]={root.data}')

    root.right = build_tree(data, 2 * i + 2)

    return root



def main():
    arr = [8, 9, 11, 7, 16, 3, 1]
    print(arr)
    build_tree(arr,0)

    nodes = array_to_tree(arr)

    for node in nodes:
        print(node.data)

main()
