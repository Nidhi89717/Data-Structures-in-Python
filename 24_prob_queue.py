#Deque is a Double ended queue where you can add/remove from either 
#rear or front. It is not FIFO anymore, but provides great flexibility
class Deque:
    def __init__(self,size):
        self.added_elements = 0
        self.rear = self.front = 0
        self.array = [None] * max(1,size)

    def next(self,pos):
        pos += 1 
        if pos == len(self.array):
            pos = 0
        return pos

    def prev(self, pos):
        pos -= 1
        if pos == -1:
            pos = len(self.array) - 1
        return pos

    def enqueue_rear(self, value):
        assert not self.full()
        self.array[self.rear] = value
        self.rear = self.next(self.rear)
        self.added_elements += 1

    def enqueue_front(self,value):
        assert not self.full()
        self.front = self.prev(self.front)
        self.array[self.front] = value
        self.added_elements += 1

    def dequeue_front(self):
        assert not self.empty()
        value = self.array[self.front]
        self.front = self.next(self.front)
        self.added_elements -= 1
        return value

    def dequeue_rear(self):
        assert not self.empty()
        self.rear = self.prev(self.rear)
        value = self.array[self.rear]
        self.added_elements -= 1
        return value

    def empty(self):
        return self.added_elements == 0

    def full(self):
        return self.added_elements == len(self.array)

    def display(self):
        print(f'Front {self.front} - Rear {self.rear}',end='\t')

        if self.full():
            print('Full',end='')
        elif self.empty():
            print('EMPTY\n')
            return
        
        print()
        cur = self.front

        for step in range(self.added_elements):
            print(self.array[cur],end=' ')
            cur = self.next(cur)

        print()

if __name__ == '__main__':
    dq = Deque(6)
    dq.enqueue_front(3)
    dq.display()
    dq.enqueue_front(2)
    dq.enqueue_rear(4)
    dq.enqueue_front(1)
    dq.enqueue_front(5)
    dq.enqueue_front(6)

    dq.display() 
    print(dq.dequeue_rear())    
    dq.display() 
    print(dq.dequeue_front())   
    dq.display() 

    print(dq.dequeue_rear())    
    print(dq.dequeue_front())   

    while not dq.empty():
        dq.dequeue_rear()

    dq.display()
    for i in range(0, 6):
        dq.enqueue_rear(i + 10)
    dq.display()

# Implement a stack using a single queue
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_end(self,value):
        node = Node(value)
        self.length += 1

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_front(self):
        if not self.head:
            return

        value = self.head.data
        next = self.head.next
        self.length -= 1
        self.head = next

        if self.length <= 1:
            self.tail = self.head

        return value

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent


class Queue:
    def __init__(self):
        self.lst = Linkedlist()

    def enqueue(self,value):
        self.lst.insert_end(value)

    def dequeue(self):
        assert not self.empty()
        return self.lst.delete_front()

    def empty(self):
        return self.lst.length == 0

    def size(self):
        return self.lst.length

    def front(self):
        assert not self.empty()
        return self.lst.head.data

    def display(self):
        if self.empty():
            print('EMPTY\n')
        else:
            print(self.lst)

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self,item):
        sz = self.queue.size()
        self.queue.enqueue(item)

        for step in range(sz):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        return self.queue.dequeue()

    def peek(self):
        return self.queue.front()

    def empty(self):
        return self.queue.empty()

if __name__ == '__main__':
    stk = Stack()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    print(stk.peek())   # 30
    stk.push(40)
    print(stk.peek())   # 40

    while not stk.empty():
        print(stk.pop(), end=' ')
