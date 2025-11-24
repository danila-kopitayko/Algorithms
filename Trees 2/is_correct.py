from Tree2 import make_tree

def solution(arr):
    left = 1
    right = 2
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left<len(arr) and arr[i]<arr[left]:
            return False
        if right<len(arr) and arr[i]<arr[right]:
            return False
    return True

def solution_fast(arr):
    left = 1
    right = 2
    n = len(arr)
    print((n-2)//2)
    for i in range((n-2)//2+1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left<n and arr[i]<arr[left]:
            return False
        if right<n and arr[i]<arr[right]:
            return False
    return True

def bfs_solution(root):
    if root is None:
        return True

    queue = [root]
    should_be_leaf = False

    while len(queue) > 0:
        node = queue.pop(0)
        if node.left:
            if should_be_leaf or node.left.data > node.data:
                return False
            queue.append(node.left)
        else:
            should_be_leaf = True

        if node.right:
            if should_be_leaf or node.right.data > node.data:
                return False
            queue.append(node.right)
        else:
            should_be_leaf = True
    return True




def main():
    arr = [21,19,18,11,12,15,16,9,8,10]

    print(solution_fast(arr))
    print(solution(arr))

    n = make_tree(arr)

    print(bfs_solution(n[0]))
    return 0


main()
