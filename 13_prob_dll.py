class Node:
    def __init__(self,data):
        self.data  = data
        self.next = None
        self.prev = None

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
        self.length -= 1
    
    @staticmethod
    def _link(first,second):
        if first:
            first.next = second
        if second:
            second.prev = first
        
    def insert_end(self,value):
        item = Node(value)
        self.add_node(item)

        if not self.head:
            self.head = self.tail = item
        else:
            self._link(self.tail , item)
            self.tail = item

    def get_nth(self,n):
        temp_head = self.head
        cnt = 1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt += 1

        return None
    
    # Find the middle
    def find_mid(self):
        len = self.length // 2
        if self.length % 2 == 1:
            m = self.get_nth(len+1)
            return m 
        else:
            m = self.get_nth(len)
            n = self.get_nth(len+1)
            return m,n

    # Find middle without using length variable
    def middle_value(self):
        if not self.head:
            return None
        
        h,t = self.head, self.tail
        while h != t and h.next != t:
            h , t = h.next, t.prev
        
        return t.data

    def middle_value2(self):         # using SLL
    # Tortise and Hare algorithm
        if not self.head:
            None

        slow, fast = self.head, self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data 

    # swap forward and backward
    def swap_kth(self,k):
        if k > self.length:
            return
        kth_back = self.length - k + 1

        if k == kth_back:
            return
        
        if k > kth_back:
            k,kth_back = kth_back,k

        first = self.get_nth(k)
        last = self.get_nth(kth_back)

        first_prev, first_next = first.prev, first.next
        last_prev,last_next = last.prev,last.next

        if k + 1 == kth_back:    # consecutive neighbours
            self._link(first_prev,last)
            self._link(last,first)
            self._link(first,last_next)

        else:
            self._link(first_prev,last)
            self._link(last,first_next)

            self._link(last_prev,first)
            self._link(first,last_next)

        if k == 1:
            self.head, self.tail = self.tail,self.head

    # Reverse list nodes:
    def reverse_nodes(self):
        if self.length <= 1:
            return

        first,second = self.head,self.head.next
        while second:
            first_, second_ = second, second.next
            self._link(second,first)
            first,second = first_, second_

        self.head ,self.tail = self.tail,self.head
        self.head.prev = self.tail.next = None   

    # Merge two sorted lists
    def merge_lists(self,other):
        if not self.head:
            return
        
        if self.head:
            cur1 , cur2 = self.head , other.head
            self.head = last = None

            while cur1 and cur2:
                if cur1.data <= cur2.data:
                    next = cur1
                    cur1 = cur1.next 
                else:
                    next = cur2
                    cur2 = cur2.next

                self._link(last,next)
                last = next
                if not self.head:
                    self.head = last
            
            if cur2:
                self.tail = other.tail
                self._link(last,cur2)
            elif cur1:
                self._link(last,cur1)

        else:
            self.tail = other.head
            self.tail = other.tail

        self.length += other.length
        self.debug_data.extend(other.debug_data)

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next
        print()

lst = Linkedlist([1,2,3,4,5,6])
for i in lst:
    print(i,end='->')

result = lst.find_mid()
print(result)

result = lst.middle_value()
print(result)

result = lst.middle_value2()
print(result)

lst.swap_kth(3)
for i in lst:
    print(i,end='->')

lst.reverse_nodes()
for i in lst:
    print(i,end='->')

lst1 = Linkedlist([1,5,6,23,78,98,100])
lst2 = Linkedlist([2,3,33,54,69,88,99,101])
lst1.merge_lists(lst2)
for i in lst1:
    print(i,end='->')
