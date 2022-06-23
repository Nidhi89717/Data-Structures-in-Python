class Queue:
    def __init__(self,size):
        self.added_elements = 0
        self.rear = self.front = 0
        self.array = [None] * max(1,size)
    
    def next(self,pos):
        pos +=1
        if pos == len(self.array):
            pos = 0
        return pos
        # return (pos + 1) % size --> shorter way

    def empty(self):
        return self.added_elements == 0
    
    def full(self):
        return self.added_elements == len(self.array)

    def enqueue(self,value):
        assert not self.full()
        self.array[self.rear] = value
        self.rear = self.next(self.rear)
        self.added_elements += 1

    def dequeue(self):
        assert not self.empty()
        value = self.array[self.front]
        self.front = self.next(self.front)
        self.added_elements -= 1
        return value

    def display(self):
        print(f"Front{self.front} - rear{self.rear}", end='\t')

        if self.full():
            print('FULL',end='')
        elif self.empty():
            print('EMPTY\n')
            return

        print("")
        cur = self.front

        for step in range(self.added_elements):
            print(self.array[cur],end=' ')
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
    for i in range(1,7):
        assert not qu.empty()
        qu.dequeue()
        qu.display
