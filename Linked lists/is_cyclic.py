import list
import random

def solution(list):
    slow = list.head
    fast = list.head.next
    if list.head is None or list.head.next is None:
        return False

    while slow!=fast:
        if fast is None or fast.next is None:
            return False
        print(slow.data, fast.data)
        fast = fast.next.next
        slow = slow.next
    return True





def main():
    l = list.LinkedList()
    n = random.randint(5,10)
    arr = []
    for i in range(n):
        arr.append(random.randint(0,10))
    l.add_new_head(arr[0])
    for i in range(1,n):
        l.append_back(arr[i])
    l.print_list()
    connection = arr[random.randint(0,len(arr)-1)]
    #print('connection',connection)
    #l.connect(connection)
    #l.print_list()
    print(solution(l))
    return  0
main()