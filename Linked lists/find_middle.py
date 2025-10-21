import list
import random

def solution(list):
    slow = list.head
    fast = list.head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

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
    print(solution(l))

main()