class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}'

class Linkedlist:
    def __init__(self,initial_values = None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

    def add_node(self,node):
        self.debug_data.append(node)
        self.length += 1

    def delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)

        else:
            print("Node doesn't exist!")
            return
        self.length += 1

    def print_reversed(self):
        cur = self.tail

        while cur is not None:
            print(cur.data,end='->')
            cur = cur.prev
        print()

    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def insert_end(self,value):
        node = Node(value)
        self.add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self._link(self.tail,node)
            self.tail = node

    def insert_front(self,value):
        item = Node(value)
        self.add_node(item)

        self._link(item,self.head)
        self.head = item

        if self.length == 1:
            self.head = self.tail = item

    def embed_after(self,node,value):
        new_node = Node(value)
        self.add_node(new_node)

        self._link(new_node,node.next)
        self._link(node,new_node)

    
    def insert_sorted(self,value):
        if not self.length or value <= self.head.data:
            self.insert_front(value)
        elif self.tail.data <= value:
            self.insert_end(value)
        else:
            prev,cur = None,self.head
            while cur:
                if value <= cur.data:
                    self.embed_after(prev,value)
                    break
                prev, cur = cur, cur.next

    # delete front
    def delete_front(self):
        if not self.head:
            return
        next = self.head.next
        self.delete_node(self.head)
        self.head = next

        if self.head:
            self.head.prev = None

        if self.length == 1:
            self.tail = self.head

    # delete end
    def delete_end(self):
        if self.length <= 1:
            self.delete_front()
        
        previous = self.tail.prev
        self.delete_node(self.tail)
        self.tail = previous
        self.tail.next = None

    def delete_link_node(self,node):
        if not node:
            return
        is_tail = node == self.tail

        previous = node.prev
        self._link(previous,node.next)
        self.delete_node(node)
        
        if is_tail:
            self.tail = previous

        return previous

    # Delete node with key
    def delete_node_with_key(self,key):
        if not self.length:
            return
        if self.head.data == key:
            self.delete_front()
        else:
            cur = self.head
            while cur:
                if cur.data == key:
                    self.delete_link_node(cur)
                    break
                cur = cur.next 

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next
        print()

lst = Linkedlist([2,3,4,5])
for i in lst:
    print(i,end='->')

lst.print_reversed()

lst.insert_end(56)
for i in lst:
    print(i,end='->')

lst.insert_front(1)
for i in lst:
    print(i,end='->')

lst.insert_sorted(45)
for i in lst:
    print(i,end='->')

lst.delete_end()
for i in lst:
    print(i,end='->')

lst.delete_front()
for i in lst:
    print(i,end='->')

lst.delete_node_with_key(4)
for i in lst:
    print(i,end='->')
