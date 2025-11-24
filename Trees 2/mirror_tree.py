from Tree2 import make_tree, show

def solution(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    solution(root.left)
    solution(root.right)
    return root

def solution_iterative(root):
    if root is None:
        return None
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        #print('before', curr.left.data, curr.right.data)
        buff = curr.left
        curr.left = curr.right
        curr.right = buff
        #print('after', curr.left.data, curr.right.data)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return root


def main():
    arr = [1,2,3,4,5,6,7]
    n1 = make_tree(arr)
    r1 = n1[0]
    res1 = []
    show(r1,res1)

    for i in range(len(res1)):
        print(res1[i])

    n2 = make_tree(arr)
    r2 = solution(n2[0])
    res2 = []
    show(r2, res2)
    print('================')
    for i in range(len(res2)):
        print(res2[i])


    n3 = make_tree(arr)
    r3 = solution_iterative(n3[0])
    res3 = []
    show(r3,res3)
    print('================')
    for i in range(len(res3)):
        print(res3[i])
    return 0


main()