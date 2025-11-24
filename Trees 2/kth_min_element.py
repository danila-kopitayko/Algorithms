from Tree2 import Node, make_tree

def solution(root, k):
    stack = []
    counter = 0
    curr = root
    while len(stack) or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop(-1)
        counter+=1

        if counter == k:
            return curr.data
        curr = curr.right
    return None

def inorderMin(root, k, counter):
    if root is None:
        return None
    res = inorderMin(root.left, k, counter)
    if res:
        return res
    counter += 1

    if counter==k:
        return root.data
    return inorderMin(root.right, k, counter)



def main():
    arr = [16, 10, 22, 6, 12, 18, 24, 2, 8, 11, 13, 17, 21, 23, 27]
    n = make_tree(arr)
    print(solution(n[0],3))
    print(inorderMin(n[0], 3, 1))
    return 0


main()