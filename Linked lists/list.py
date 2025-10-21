class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head =  None
        self.tail =  None
    def add_new_head(self,n):
        node = Node(n)
        if self.head==None:
            self.head = node
        else:
            node.next = self.head
        self.head=node
    def append_front(self,n):
        node = Node(n)
        if self.head == None:
            self.head = node
            return 
        else:
            node.next = self.head
            self.head = node
    def append_back(self,n):
        node = Node(n)
        if self.head == None:
            self.tail = node
            return
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
            self.tail = node
    def connect(self,n):
        curr = self.head
        while curr.data!=n:
            curr = curr.next
        self.tail.next = curr
    def print_list(self):
        curr=self.head
        #print(f'tail = {self.tail.data}\nhead={self.head.data}')
        output=''
        counter=0
        while curr:
            output+=str(curr.data)
            if curr.next==self.tail and counter==1:
                break
            elif curr.next==self.tail and counter==0:
                counter+=1
            if curr.next:
                output += '==>'
            curr = curr.next
        print(output)
    def insert(self,after,n):
        curr = self.head
        while curr!=None:
            if curr.data == after:
                break
            curr = curr.next
        if curr!=None:
            node = Node()
            node.data=n
            if curr == self.tail:
                self.tail = node
            node.next = curr.next 
            curr.next = node
