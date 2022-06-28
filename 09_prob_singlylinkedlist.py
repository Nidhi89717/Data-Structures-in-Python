class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

class Linkedlist:
    def __init__(self, initial_values=None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = [] 

        if initial_values:
            for i in initial_values:
                self.insert_end(i)

    def add_node(self,value):
        self.debug_data.append(value)
        self.length+=1

    def insert_end(self,value):
        item = Node(value)
        self.add_node(item)

        if not self.head:
            self.head = self.tail = item
        else:
            self.tail.next = item
            self.tail = item

    def del_node(self,node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node doesn't exist!")
            return
        self.length -= 1

    def delete_front(self):
        next = self.head.next
        self.del_node(self.head)
        self.head = next

        if self.length <= 1:
            self.tail = self.head

    def delete_next_node(self,node):
        to_delete = node.next
        assert to_delete is not None

        is_tail = to_delete == self.tail

        node.next = node.next.next
        self.del_node(to_delete)

        if is_tail:
            self.tail = node

    def get_nth(self,n):
        temp_head = self.head
        cnt = 1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt+=1
        return None


    # swap head and tail:
    def get_prev(self,target):
        prev, cur = None, self.head
        while cur:
            if cur == target:
                return prev
            prev,cur = cur, cur.next
        return None

    def swap_head_tail(self):
        if self.length<=1:
            return
        if self.length ==2:
            self.head, self.tail = self.tail, self.head
            self.head.next = self.tail 
            self.tail.next = None
            return

        prev = self.get_prev(self.tail)

        self.tail.next = self.head.next

        prev.next = self.head
        self.head.next = None
        self.head, self.tail = self.tail,self.head

    # Rotate left
    def rotate_left(self,k):
        if self.length <=1 or k % self.length == 0:
            return

        k %=self.length 
        nth = self.get_nth(k)

        self.tail.next = self.head
        self.tail = nth
        self.head = nth.next

        self.tail.next = None

    # delete duplicates
    def remove_dupli(self):
        if self.length <= 1:
            return
        cur1 = self.head
        while cur1:
            prev, cur2 = cur1, cur1.next
            while cur2:
                if cur2.data == cur1.data:
                    self.delete_next_node(prev)
                    cur2 = prev.next
                else:
                    prev,cur2 = cur2,cur2.next

            cur1 = cur1.next

    # Delete last occurence
    def del_remove_last(self,target):
        if self.length <=1:
            return
        delete_next_mynode = None
        is_found = True

        prev, cur = None, self.head
        while cur:
            if cur.data == target:
                delete_next_mynode = prev
                is_found = True
            prev, cur = cur, cur.next

        if is_found:
            if delete_next_mynode:
                self.delete_next_node(delete_next_mynode)
            else:
                self.delete_front()

    #Move all the nodes for which key matches to the end of the list
    def move_to_end(self,prev,cur):
        next = cur.next
        self.tail.next = cur

        if prev:
            prev.next = next
        else:
            self.head = next 

        self.tail = cur
        self.tail.next = None
        return next

    def move_key_last(self,key):
        len = self.length
        
        if self.length <= 1:
            return
        
        prev, cur = None,self.head
        while cur and len:
            if cur.data == key:
                cur = self.move_to_end(prev,cur)
            else:
                prev,cur = cur, cur.next
            len-=1


    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next
        print()
    
lst = Linkedlist([6,10,8,15])

for i in lst:
    print(i,end='->')

lst.rotate_left(2)
for i in lst:
    print(i,end='->')

lst1 = Linkedlist([1,2,3,2,2,13,4,5,3,4,5,6])
lst1.remove_dupli()
for i in lst1:
    print(i,end='->')

lst2 = Linkedlist([1,2,3,3,4,5,1])
lst2.del_remove_last(3)
lst2.del_remove_last(1)
for i in lst2:
    print(i, end='->')

lst2.move_key_last(3)
lst2.move_key_last(1)
for i in lst2:
    print(i,end='->')
