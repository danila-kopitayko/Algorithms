from Tree import array_to_tree


def is_symmetric(root):
    if root is None:
        return True
    queue = [root]

    while len(queue) > 0:
        queue_len = len(queue)
        for i in range(queue_len):
            if queue[i] is None and queue[queue_len - i - 1] is None:
                continue
            if queue[i] is None or queue[queue_len - i - 1] is None:
                return False
            if queue[i].data != queue[queue_len - i - 1].data:
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[queue_len:]
    return True



def search(root,res):
    if root is None:
        return res
    search(root.left,res)
    res.append(root.data)
    search(root.right,res)
    return res

def dfs_is_symmetric(root):
    if root is None:
        return True
    data = []
    data = search(root,data)
    for i in range(len(data)//2):
        if data[i]!=data[len(data)-i-1]:
            return False
    return True

def main():
    arr = [3,8,8,6,9,9,6]

    t = array_to_tree(arr)

    print(is_symmetric(t[0]))
    print(dfs_is_symmetric(t[0]))
main()




