from Tree2 import make_tree, Node

def solution(root):
    if root is None:
        return True
    queue = [root]
    seen = False

    while len(queue)>0:
        node = queue.pop(0)
        if node:
            print(node,node.data)
        if node is None:
            seen = True
            #print(seen)
        else:
            if seen:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True


def main():
    arr = [9,6,7,8]

    n = make_tree(arr)

    print(solution(n[0]))

main()