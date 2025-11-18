class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

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
    return 0

main()