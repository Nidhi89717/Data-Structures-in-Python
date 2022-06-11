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

        self.debug_data = [] #add or remove nodes

        if initial_values:
            for i in initial_values:
                self.insert_end(i)

    def add_node(self, node):
        self.debug_data.append(node)
        self.length+=1

    def del_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)

        else:
            print("Node doesn't exist!")
            return

        self.length -=1

    # insert front
    def insert_front(self, item):
        value = Node(item)
        self.add_node(value)
        
        value.next = self.head
        self.head = value

        if self.length==1:
            self.head = self.tail 
    
    # insert end
    def insert_end(self,item):
        value = Node(item)
        self.add_node(value)
        if not self.head:
            self.head = self.tail = value
        else:
            self.tail.next = value
            self.tail = value 

    # delete front
    def delete_front(self):
        #assert self.length - getting assertion error

        next = self.head.next
        self.del_node(self.head)
        self.head = next

        if self.length <= 1:
            self.tail = self.head
    # get nth item
    def get_nth(self,n):
        temp_head = self.head
        cnt = 1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt+=1
        return None
    
    # get nth from back
    def get_nth_back(self,n):
        if self.length < n:
            return None
        return (self.get_nth(self.length - n +1))

    # is identical?
    def is_iden(self,other):
        h1 , h2 = self.head, other.head

        while h1 and h2:
            if h1.data != h2.data:
                return False
            
            h1, h2 = h1.next, h2.next
        return not h1 and not h2 #both ends are together 

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head.data
            temp_head = temp_head.next
        print() 

# linked list without tail/length
class LinkedList:
    def __init__(self, initial_values=None):
        self.head = None

        if initial_values:
            for value in initial_values:
                self.add_element(value)

    def add_element(self, value):
        item = Node(value)
        item.next = self.head
        self.head = item

    def get_tail(self):
        temp_head = self.head

        while temp_head is not None and temp_head.next is not None:
            temp_head = temp_head.next

        return temp_head

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent

lst = Linkedlist()
lst.insert_end(1)
lst.insert_end(2)
lst.insert_end(3)
lst.insert_end(5)
print()
#lst.delete_front()

lst1 = Linkedlist([1, 2, 3])
lst2 = Linkedlist([1, 2])
result = str(lst1.is_iden(lst2))
print(result)
print()

for i in lst:
    print(i,end='-->')
print()

lst.delete_front()
for i in lst:
    print(i,end='-->')
print()

result = lst.get_nth_back(2)
print(result)
print()

lst = LinkedList([1, 2, 3])
result = (lst)
print(result)
