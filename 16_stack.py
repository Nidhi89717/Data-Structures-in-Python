class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        assert self.items, 'No items!'
        return self.items.pop()

    def peek(self):
        assert self.items, 'No items!'
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)

print(stk.peek())

stk.push(40)
print(stk.peek())

while not stk.isEmpty():
    print(stk.pop(),end=' ')

# for threaded programming
def builtin():
    from queue import LifoQueue

    stk = LifoQueue(maxsize = 6)

    stk.put(10)
    stk.put(20)
    stk.put(30)
    stk.put(40)

    print('\n',stk.qsize())

    while not stk.empty():
        print(stk.get(), end=' ')

builtin()
