class Node:
    def __init__(self,data,next = None,prev = None):
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

    def delete_node(self,node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node doesn't exist")
            return
        self.length += 1

    @staticmethod
    def _link(first,second):
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
        node = Node(value)
        self.add_node(node)

        self._link(node,self.head)
        self.head = node

        if self.length == 1:
            self.head = self.tail = node

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
    
    # Delete all nodes with key
    def delete_all_node_key1(self,key):
        if not self.length:
            return
        k = self.length
        while k:
            if self.head.data == key:
                self.delete_front()
            k -= 1
        cur = self.head
        while cur and key:
            if cur.data == key:
                self.delete_link_node(cur)
            cur = cur.next

    #               OR                
        
    def delete_all_node_key2(self,key):
        if not self.length:
            return
        
        #insert dummy
        self.insert_front(key - 1)

        cur = self.head
        while cur:
            if cur.data == key:
                cur = self.delete_link_node(cur)
            cur = cur.next
        
        self.delete_front()

    # Delete even positions:
    def delete_even_nodes(self):
        if not self.length:
            return
        
        cur = self.head.next
        while cur:
            self.delete_link_node(cur)
            if cur.next == None:
                break
            cur = cur.next.next

    #               OR

    def delete_even_nodes2(self):
        if self.length <= 1:
            return

        cur = self.head
        while cur:
            self.delete_link_node(cur.next)
            cur = cur.next
            
    def delete_odd_positions(self):
        #make odd positions even! Resuse the old code :)
        self.insert_front(-1)
        self.delete_even_nodes2()
        self.delete_front()
                
    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next
        print()

    def is_palindrome(self):
        if self.length <= 1:
            return True

        len = self.length // 2
        start , end = self.head, self.tail
        while len:
            len -= 1
            if start.data == end.data:
                print( 'Pallindrome list')   
            
            start, end = start.next, end.prev
        

lst = Linkedlist([2,2,1,2,2,3,4,5,6,7,8,2])
for i in lst:
    print(i,end='->')

lst.delete_all_node_key2(2)
for i in lst:
    print(i,end='->')

lst.delete_even_nodes2()
for i in lst:
    print(i,end='->')

lst1 = Linkedlist([1,2,3,4,5,6,7,8])
lst1.delete_odd_positions()
for i in lst1:
    print(i,end='->')           

lst2 = Linkedlist([1,2,1])
lst2.is_palindrome()
