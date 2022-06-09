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

    def insert_end(self,value):
        item = Node(value)
        if not self.head:
            self.head = self.tail = item 
        else:
            self.tail.next = item
            self.tail = item 

    def print_ll(self):
        temp_head = self.head
        while temp_head is not None:
            print(temp_head.data, end ='->')
            temp_head = temp_head.next
        print()

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next 

lst = Linkedlist()
lst.insert_end(6)
lst.insert_end(10)
lst.insert_end(8)
lst.insert_end(15)
lst.print_ll()

for i in lst:
    print(i, end='->')  # for __iter__
