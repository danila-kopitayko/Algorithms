class Queue:
    def __init__(self,len):
        self.len = len
        self.data = []#[0] * len
        self.head = None
        self.tail = None
    def push(self,n):
        if self.head is None:
            self.head = 0
            self.tail = 1 % self.len
            self.data.append(n) #[self.head]=n
        elif self.tail == self.head:
            print('Queue filled')
            return -1
        else:
            self.data.append(n)#self.data[self.tail] = n
            self.tail += (self.tail + 1) % self.len

    def pop(self):
        if self.head is None:
            print('Empty queue')
            return -2
        else:
            element = self.data[self.head]
            self.data[self.head] = 0
            #self.head+=1
            self.len -= 1
            print(self.len)
        return element
    def peek(self):
        if self.head is None:
            print('Empty queue')
            return -3
        else:
            print(self.head)
            element = self.data[self.head]
        return element

    def print_queue(self):
        for i in range(self.head,self.len):
            print(self.data[i],end=' ')
