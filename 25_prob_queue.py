# Queue using 2 Stacks: O(1) enqueue
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        assert self.items, 'No items!'
        return self.items.pop()

    def peak(self):
        assert self.items,'No items!'
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(sel.items)

class Queue:
    def __init__(self):
        self.stk1, self.stk2 = Stack(), Stack()

    @staticmethod
    def move(stk1,stk2):
        while not stk1.empty():
            stk2.push(stk1.pop())

    def enqueue(self,value):
        self.stk1.push(value)

    def dequeue(self):
        assert not self.empty()

        if self.stk2.empty():
            self.move(self.stk1, self.stk2)

        value = self.stk2.pop()
        return value

    def empty(self):
        return self.stk1.empty() and self.stk2.empty()

if __name__ == '__main__':
    qu = Queue()

    for i in range(1,5):
        qu.enqueue(i)

    while not qu.empty():
        print(qu.dequeue(), end=' ')
    
    print()

# Queue using 2 Stacks: O(1) dequeue
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        assert self.items,'No items!'
        return self.items.pop()
    
    def peek(self):
        assert self.items, 'No items!'
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.stk1, self.stk2 = Stack(), Stack()

    @staticmethod
    def move(stk1,stk2):
        while not stk1.empty():
            stk2.push(stk1.pop())

    def enqueue(self,value):
        self.move(self.stk1, self.stk2)
        self.stk1.push(value)
        self.move(self.stk2,self.stk1)

    def dequeue(self):
        assert not self.empty()
        value = self.stk1.pop()
        return value
    
    def empty(self):
        return self.stk1.empty()

if __name__ =='__main__':
    qu = Queue()

    for i in range(1,5):
        qu.enqueue(i)

    while not qu.empty():
        print(qu.dequeue(), end=' ')

    print()

# Develop the code for circular queue without added_elements
class Queue:
    def __init__(self,size):
        self.rear = self.front = 0
        self.array = [None]*max(1,size + 1)

    def next(self,pos):
        pos += 1
        if pos == len(self.array):
            pos = 0
        return pos

    def enqueue(self,value):
        assert not self.full()
        self.array[self.rear] = value
        self.rear = self.next(self.rear)

    def dequeue(self):
        assert not self.empty()
        value = self.array[self.front]
        self.front = self.next(self.front)
        return value

    def empty(self):
        return self.front == self.rear
    
    def full(self):
        return self.next(self.rear) == self.front

    def display(self):
        print(f'Front {self.front} - rear {self.rear}', end ='\t')

        if self.full():
            print('FULL', end='')
        elif self.empty():
            print('EMPTY\n')
            return
        
        print("")
        cur = self.front
        while cur != self.rear:
            print(self.array[cur], end=' ')
            cur = self.next(cur)

        print("")

if __name__ == '__main__':

    qu = Queue(6)

    assert qu.empty()
    qu.display()

    for i in range(1,7):
        assert not qu.full()
        qu.enqueue(i)
        qu.display()

    print()

    assert qu.full()
    for i in range(1, 7):
        assert not qu.empty()
        qu.dequeue()
        qu.display()

    print()

    for i in range(1, 7):
        assert not qu.full()
        qu.enqueue(i)
        qu.display()

    print()
    qu.dequeue()
    assert not qu.full()
    qu.enqueue(7)
    assert qu.full()
    qu.display()

    qu.dequeue()
    qu.dequeue()
    assert not qu.full()
    qu.enqueue(8)
    assert not qu.full()
    qu.display()
    qu.enqueue(9)
    assert qu.full()
    qu.display()

    assert qu.full()
    for i in range(1, 7):
        assert not qu.empty()
        qu.dequeue()
        qu.display()
    
    print()

# Priority Queue: 
# Assume that we have an OS comprised of tasks, each of priority 1, 2, or 3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
                represent += ','

        return represent

class Queue:
    def __init__(self):
        self.lst = Linkedlist()

    def enqueue(self, value):
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

class PriorityQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.q3 = Queue()

    def enqueue(self, value, priority):
        assert 1 <= priority <= 3

        if priority == 1:
            self.q1.enqueue(value)
        elif priority == 2:
            self.q2.enqueue(value)
        else:
            self.q3.enqueue(value)

    def dequeue(self):
        assert not self.empty()

        if not self.q3.empty():
            return self.q3.dequeue()

        if not self.q2.empty():
            return self.q2.dequeue()

        return self.q1.dequeue()

    def empty(self):
        return self.q1.empty() and self.q2.empty() and self.q3.empty()


    def display(self):
        if self.empty():
            print("EMPTY\n")
            return

        if not self.q3.empty():
            print('Priority #3 tasks', end=' ')
            self.q3.display()

        if not self.q2.empty():
            print('Priority #2 tasks', end=' ')
            self.q2.display()

        if not self.q1.empty():
            print('Priority #1 tasks', end=' ')
            self.q1.display()



if __name__ == '__main__':
    
    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)

    tasks.display()
    
    print(tasks.dequeue())  
    print(tasks.dequeue())  

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    tasks.display()
    
    while not tasks.empty():
        print(tasks.dequeue(), end = ' ')

    print()

# Sum of last K numbers (stream)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
            self.head = self.tail 

        return value

    def __repr__(self):
        represent = ''
        temp_head = self.head
        while temp_head is not None:
            represent += str(temp_head.data)
            if temp_head:
                represent += ','
        
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

    def display(self):
        if self.empty():
            print('EMPTY\n')
        else:
            print(self.lst)

class LastKnumsum:
    def __init__(self, k):
        self.k = k
        self.q = Queue()
        self.sum = 0

    def next(self,new_num):
        self.q.enqueue(new_num)
        self.sum += new_num

        if self.q.size() > self.k:
            self.sum -= self.q.dequeue()

        return self.sum

if __name__ == '__main__':
    processor = LastKnumsum(4)

    while True:
        num = int(input())
        print('Sum of last k numbers',processor.next(num))
