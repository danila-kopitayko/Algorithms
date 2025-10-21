import list
import random

def solution(list):
    curr = list.head
    prev=None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    list.head = prev
    return list





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
    reversed = list.LinkedList()
    reversed = solution(l)
    reversed.print_list()

main()