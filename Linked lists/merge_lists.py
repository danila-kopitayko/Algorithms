import random
import list

def solution(list1, list2):
    l = list.LinkedList()
    curr1 = list1.head
    curr2 = list2.head

    while curr1!=None and curr2!=None:
        if curr1.data<=curr2.data and l.head is None:
            l.add_new_head(curr1.data)
            curr1 = curr1.next
        elif curr1.data<=curr2.data and l.head!=None:
            l.append_back(curr1.data)
            curr1 = curr1.next
        elif curr1.data>=curr2.data and l.head is None:
            l.add_new_head(curr2.data)
            curr2 = curr2.next
        elif curr1.data>=curr2.data and l.head!=None:
            l.append_back(curr2.data)
            curr2 = curr2.next

    if curr1 == list1.tail:
        while curr2!=None:
            l.append_back(curr2.data)
            curr2 = curr2.next
    elif curr2 == list1.tail:
        while curr1!=None:
            l.append_back(curr1.data)
            curr1 = curr1.next
    return l



def generate_rand_list():
    l = list.LinkedList()
    n = random.randint(5,10)
    arr = []
    for i in range(n):
        arr.append(random.randint(0,10))
    arr = sorted(arr)
    l.add_new_head(arr[0])
    for i in range(1,n):
        l.append_back(arr[i])
    return l

def main():
    l1 = generate_rand_list()
    l1.print_list()
    l2 = generate_rand_list()
    l2.print_list()

    l = solution(l1,l2)
    l.print_list()

main()


