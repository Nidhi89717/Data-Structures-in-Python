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

    def insert_front(self, item):
        value = Node(item)
        self.add_node(value)

        value.next = self.head
        self.head = value

        if self.length == 1:
            self.head == self.tail

    def delete_front(self):
        next = self.head.next
        self.del_node(self.head)
        self.head = next

        if self.length <= 1:
            self.head = self.tail

    def del_node(self,node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node doesn't exist")
            return
        self.length -= 1

    def delete_last(self):
        if self.length <= 1:
            self.delete_front()
            return

        prev = self.get_nth(self.length - 1)

        self.del_node(self.tail)
        self.tail = prev
        self.tail.next = None

    def get_nth(self,n):
        temp_head = self.head
        cnt =1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt += 1
        return None

    def delete_next_node(self,node):
        to_delete = node.next
        assert to_delete is not None
        
        is_tail = to_delete == self.tail

        node.next = node.next.next
        self.del_node(to_delete)

        if is_tail:
            self.tail = node

    # Arrange odd and even nodes
    def arrange_odd_even_node(self):
        if self.length <=2:
            return

        odd_node = self.head
        first_even = self.head.next

        while odd_node.next and odd_node.next.next:
            next_even = odd_node.next
            # connect odd with odd and even with even
            odd_node.next = odd_node.next.next
            next_even.next = next_even.next.next
            odd_node = odd_node.next

            # if odd self.length then self.tail has to be updated
            if self.length %2 == 1:
                self.tail = next_even

        # connect last odd node with first even node
        odd_node.next = first_even

    # insert alternating
    def insert_alternate(self,another_list):
        self.debug_data.extend(another_list.debug_data)

        def in_after(src,target):
            next = target.next
            target.next = src.next
            src.next = target
            return next 


        if not another_list.length:
            return
        if not self.length:
            self.head = another_list.head
            self.tail = another_list.tail
            self.length = another_list.length
            return

        self.length += another_list.length

        cur1, cur2 = self.head, another_list.head
        while cur1 and cur2:
            cur2 = in_after(cur1, cur2)

            if cur1 == self.tail:
                self.tail = another_list.tail
                cur1.next.next = cur2
                break
            
            cur1 = cur1.next.next 

    #Remove repeated values except one
    def remove_repeated_exceptone(self):
        if self.length <=1:
            return
        cur = self.head
        while cur and cur.next:
            if cur.data == cur.next.data:
                self.delete_next_node(cur)
            else:
                cur = cur.next

    #Remove all repeated
    def remove_all_repeated(self):
        # dummy head and tail for easy handling
        self.insert_front(self.head.data - 1)
        self.insert_end(self.tail.data + 1)

        prev, cur = self.head, self.head.next
        last_removed_value = self.head.data - 1

        while cur and cur.next:
            if cur.data == cur.next.data:
                last_removed_value = cur.data
                self.delete_next_node(cur)

            else:
                if last_removed_value == cur.data:
                    self.delete_next_node(prev)
                    cur = prev
                prev, cur = cur, cur.next

        self.delete_front() #undo dummy 
        self.delete_last()

    # Adding two huge integers
    def add_num(self,another_list):
        if not another_list.length:
            return
        cur1, cur2 = self.head, another_list.head
        carry = 0

        while cur1 and cur2:
            value1, value2 = 0,0
            if cur1:
                value1 = cur1.data
            if cur2:
                value2 = cur2.data
                cur2 = cur2.next

            value1 +=value2 + carry
            carry = value1 // 10
            value1 %= 10

            if cur1:
                cur1.data = value1
                cur1 = cur1.next
            else:
                self.insert_end(value1)
        if carry:
            self.insert_end(carry)

    # Reverse chain
    def reverse_chain(self,k):
        if self.length <= 1 or k == 1:
            return
        
        def reverse_subchain(cur,k):
            tail = cur
            prev, cur = cur, cur.next

            while k>1 and cur:
                k -= 1
                next = cur.next
                cur.next = prev
                prev,cur = cur, next
            return prev, tail, cur
        
        last_tail = None
        next_chain_head = self.head
        self.head = None

        while next_chain_head:
            chain_head, chain_tail, next_chain_head = reverse_subchain(next_chain_head,k)
            self.tail = chain_tail

            if not self.head:
                self.head = chain_head
            else:
                last_tail.next = chain_head
            last_tail = chain_tail

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next
        print()
    
lst = Linkedlist([6,10,11,11,34,65,70])

for i in lst:
    print(i,end='->')

lst.arrange_odd_even_node()

for i in lst:
    print(i,end='->')

lst2 = Linkedlist([4,5,3])
lst.insert_alternate(lst2)
for i in lst:
    print(i,end='->')

lst.remove_repeated_exceptone()
for i in lst:
    print(i,end='->')

lst_1 = Linkedlist([1,1,1,2,2,3,4,5,6])
lst_1.remove_all_repeated()
for i in lst_1:
    print(i,end='->')

lst1 = Linkedlist([1,2,3])
lst1.add_num(lst2)
for i in lst1:
    print(i,end='->')

lst3 = Linkedlist([4,7,67,68,45,88,98])
lst3.reverse_chain(3)
for i in lst3:
    print(i,end='->')
