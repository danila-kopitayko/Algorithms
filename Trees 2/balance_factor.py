class Node:
    def __init__(self,data=None,left=None,right=None,balance=0):
        self.data = data
        self.left = left
        self.right = right
        self.balance  = balance


def make_tree(arr):
    nodes = []
    for i in range(len(arr)):
        if arr[i] is None:
            nodes.append(None)
        else:
            nodes.append(Node(arr[i]))

    for i in range(len(arr)):
        if nodes[i] is None:
            continue
        if 2 * i + 1 < len(arr):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(arr):
            nodes[i].right = nodes[2 * i + 2]

    return nodes


def solution(root):
    if root is None:
        return 0
    height_left = solution(root.left)
    height_right = solution(root.right)

    root.balance = height_left - height_right

    return 1 + max(height_left,height_right)



def main():
    arr = [9, 3, 8, 16, 7, 11]
    n = make_tree(arr)
    print(solution(n[0]))

    for i in range(len(arr)):
        print(n[i].balance)

main()