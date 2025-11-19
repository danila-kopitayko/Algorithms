from Tree import array_to_tree

def solution(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left and root.right:
        return 1 + min(solution(root.left),solution(root.right))
    if root.left:
        return 1 + solution(root.left)
    if root.right:
        return 1 + solution(root.right)
#попробовать через поиск в ширину

def main():

    arr = [8, 9, 11, 7, 16, 3, 1]

    t = array_to_tree(arr)

    print(solution(t[0]))
    return 0

main()