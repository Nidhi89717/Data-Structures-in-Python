class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

class Linkedlist:
    def __init__(self, initial_values = None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []

        if initial_values:
            for i in initial_values:
                self.insert_end(i)

    def add_node(self,node):
        self.debug_data.append(node)
        self.length+=1

    def del_node(self,node):
        if node in self.debug_data:
            self.debug_data.remove(node)

        else:
            print("Node doesn't exist")

        self.length -=1

    def insert_end(self,item):
        value = Node(item)
        self.add_node(value)

        if not self.head:
            self.head = self.tail = value

        else:
            self.tail.next = value
            self.tail = value

    def get_nth(self,n):
        temp_head = self.head
        cnt = 1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt+=1
        return None    

    def delete_front(self):
        next = self.head.next
        self.del_node(self.head)
        self.head = next

        if self.length <=1:
            self.tail = self.head
    
    def delete_end(self):
        if self.length <=1:
            self.delete_front()

        prev = self.get_nth(self.length - 1)
        self.del_node(self.tail)
        self.tail = prev
        self.tail.next = None

    def delete_nth(self,n):
        if n < 1 or n > self.length:
            print("Error. No such node exist!")
        elif n == 1:
            self.delete_front()
        else:
            before_nth = self.get_nth(n-1)
            nth = before_nth.next
            is_nth_tail = nth == self.tail
            before_nth.next = nth.next

        if is_nth_tail:
            self.tail = before_nth
        
        self.del_node(nth)

    def __iter__(self):
        temp_head = self.head

        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next
        print()

lst = Linkedlist([6,5,3,7,8])

for i in lst:
    print(i,end='->')

lst.delete_nth(2)
for i in lst:
    print(i,end='->')

lst.delete_front()
for i in lst:
    print(i,end='->')

lst.delete_end()
for i in lst:
    print(i,end='->')
