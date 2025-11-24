class Node:
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

def make_tree(arr):
    nodes = []
    for i in range(len(arr)):
        if arr[i] is None:
            nodes.append(None)
        else:
            nodes.append(Node(arr[i]))

    for i in range(len(arr)):
        if 2 * i + 1 < len(arr):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(arr):
            nodes[i].right = nodes[2 * i + 2]

    return nodes

def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left<n and data[left]>data[largest]:
        largest = left
    if right<n and data[right]>data[largest]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        #print(data)
        heapify(data, n, largest)


def make_heap(arr):
    n = len(arr)
    i = (n - 2) // 2
    while i>=0:
        #print('i',i)
        heapify(arr,n,i)
        i-=1
    #print('len',n)
    nodes = make_tree(arr)
    return nodes

def heap_sort(arr):
    n = len(arr)
    i = (n - 2) // 2
    while i>=0:
        heapify(arr,n,i)
        i-=1
    i = n - 1
    while i>0:
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        i-=1
    nodes = make_tree(arr)
    return nodes


def show(root,res):
    if root is None:
        return

    show(root.left,res)
    res.append(root.data)
    show(root.right,res)

def show_bfs(root):
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)




def main():
    heap = make_heap([12,11,13,5,6,7,21,16])
    s = [12,11,13,5,6,7,21,16]
    t = [[1,23,3],[3,3,1]]
    s = heap_sort(t)
    print('heap_sort')
    show_bfs(s[0])

    print(s.pop(0).data)
    '''
    r = []
    print('heap')
    show_bfs(heap[0])
    print('heap lnr')
    show(heap[0],r)
    for i in range(len(r)):
        print(r[i],end=' ')
    '''
main()

