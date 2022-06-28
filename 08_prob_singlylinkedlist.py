class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

class Linkedlist():
    def __init__(self,initial_values = None):
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

    def delete_node(self,node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node doesn't exist!")
            return

    def insert_end(self,item):
        value = Node(item)
        self.add_node(value)

        if not self.head:
            self.head = self.tail = value
        else:
            self.tail.next = value
            self.tail = value 

    def insert_front(self, item):
        value = Node(item)
        self.add_node(value)

        value.next = self.head
        self.head = value

        if self.length == 1:
            self.head = self.tail = value

    def delete_front(self):
        next = self.head.next
        self.del_node(self.head)
        self.head = next

        if self.length <=1:
            self.tail = self.head

    def delete_next(self,node):
        to_delete = node.next
        assert to_delete is not None

        is_tail = to_delete == self.tail

        node.next = node.next.next
        self.delete_node(to_delete)

        if is_tail:
            self.tail = node

    # swap consecutive values
    def swap(self):
        temp_head = self.head
        while temp_head is not None and temp_head.next is not None:
            temp_head.data,temp_head.next.data = temp_head.next.data,temp_head.data
            temp_head = temp_head.next.next

    # Delete with key
    def del_key(self,key):
        if not self.length:
            return
        if self.head.data == key:
            self.delete_front()

        else:
            prev,cur = None,self.head
            while cur:
                if cur.data == key:
                    self.delete_next(prev)
                    break
                prev, cur = cur, cur.next

    # reverse list nodes
    def reverse_nodes(self):
        if self.length <=1:
            return

        self.tail = self.head
        prev = self.head
        self.head  = self.head.next
        while self.head:
            next = self.head.next 
            self.head.next = prev

            prev= self.head
            self.head = next

        #finalise head and tail;
        self.head = prev
        self.tail.next = None

    #Delete even positions
    def del_even(self):
        if self.length <1:
            return
        prev,cur = self.head,self.head.next
        while cur:
            self.delete_next(prev)
            if prev.next == None: #if tail
                break
            cur = prev.next.next
            prev = prev.next

    # insertion sort
    def insert_after(self,prev,value):
        new_node = Node(value)
        self.add_node(new_node)

        new_node.next = prev.next
        prev.next = new_node

    def insert_sort(self, value):
        if not self.length or value <= self.head.data:
            self.insert_front(value)
        elif self.tail.data <= value:
            self.insert_end(value)
        else:
            prev, cur = None, self.head
            while cur:
                if value <= cur.data:
                    self.insert_after(prev,value)
                    break
                prev,cur = cur, cur.next


    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next
        print()

lst = Linkedlist([10,20,30,41,15,34,69,88,100])
for i in lst:
    print(i,end='->')

lst.del_key(20)
for i in lst:
    print(i,end='->')

lst.swap()
for i in lst:
    print(i,end='->')

lst.reverse_nodes()
for i in lst:
    print(i,end='->')

lst.del_even()
for i in lst:
    print(i,end='->')
    
lst1 = Linkedlist()
lst1.insert_sort(10) 
lst1.insert_sort(2) 
lst1.insert_sort(30)
lst1.insert_sort(4) 
lst1.insert_sort(1) 
for i in lst1:
    print(i, end='->')
