import list as list_
import random

def solution(list,val):
    dummy = list_.Node()

    dummy.next = list.head
    prev = dummy
    curr = list.head
    while curr!=None:
        if curr.data==val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        list.head = dummy.next
    return list






def main():
    l = list_.LinkedList()
    n = random.randint(5,10)
    arr = []
    for i in range(n):
        arr.append(random.randint(0,10))
    l.add_new_head(arr[0])
    for i in range(1,n):
        l.append_back(arr[i])
    l.print_list()

    edited_list = list_.LinkedList()
    to_delete = arr[random.randint(0,n-1)]
    print(f'ELement to delete = {to_delete}')
    edited_list = solution(l,to_delete)
    edited_list.print_list()
main()