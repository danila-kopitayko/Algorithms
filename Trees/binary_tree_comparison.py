from Tree import array_to_tree, Node

def solution(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    return solution(t1.left, t2.left) and solution(t1.right, t2.right)


def main():

    arr1 = [6, 3, 8, 1, 4, 7, 9]
    arr2 = [6, 3, 8, 1, 4, 7, 10]

    t1 = array_to_tree(arr1)
    t2 = array_to_tree(arr2)

    print(solution(t1[0],t2[0]))

    return 0

main()