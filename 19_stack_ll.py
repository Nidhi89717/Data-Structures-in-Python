class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self,value):
        item = Node(value)
        item.next = self.head
        self.head = item
        self.length += 1

    def pop(self):
        assert self.head, 'No items!'

        node = self.head
        self.head = self.head.next
        self.length -= 1

        return node.data

    def peek(self):
        assert self.head, 'No items!'
        return self.head.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

if __name__ == '__main__':
    stk = Stack()

    stk.push(10)
    stk.push(20)
    stk.push(30)
    print(stk.peek())
    stk.push(40)
    print(stk.peek())

    while not stk.isEmpty():
        print(stk.pop(),end=' ')
