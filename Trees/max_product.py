from Tree import array_to_tree, Node


def solution(data):
    if len(data)<=3:
        return -1
    min_idx = 1
    max_idx = 2
    i = 0
    while 2 * min_idx + 1 < len(data):
        #print(f'min_idx={min_idx}\t len(data)={len(data)}')
        min_idx = 2 * min_idx + 1
    while 2 * max_idx + 2 < len(data):
        #print(f'max idx:{max_idx}')
        max_idx = 2 * max_idx + 2
    #print(data[max_idx], data[min_idx])
    return data[max_idx] * data[min_idx]

def find_min(root):
    if root.left is None:
        return root.data
    while root.left:
        #print(root.data)
        root = root.left
    return root

def find_max(root):
    if root.right is None:
        return root.data
    while root.right:
        #print(root.data)
        root = root.right
    return root

def alternative_solution(root):
    min_ = find_min(root)
    max_ = find_max(root)
    return min_.data*max_.data

def main():

    arr = [6, 3, 8, 1, 4, 7, 9]

    t = array_to_tree(arr)

    print('solution',solution(arr))
    print('alternative solution', alternative_solution(t[0]))

    return 0


main()
