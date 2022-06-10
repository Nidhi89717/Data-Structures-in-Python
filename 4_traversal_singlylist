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

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

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
        print()

    # get nth item
    def get_nth(self,n):
        temp_head = self.head
        cnt = 1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt+=1
        return None #Still more steps needed implies nth element not found 
    
    #Search for an item
    def index(self,value):
        temp_head = self.head
        idx = 0
        while temp_head:
            if temp_head.data == value:
                return idx

            temp_head = temp_head.next
            idx+=1
        return None

    # Improved search index transposition
    def ind_transposition(self,value):
        prev, cur = None, self.head
        idx = 0

        while cur:
            if cur.data == value:
                if not prev:
                    return idx
                prev.data, cur.data = cur.data, prev.data
                return idx - 1
            prev, cur = cur, cur.next
            idx += 1
        return None
def test_get_nth():
    lst = Linkedlist()
    lst.insert_end(6)
    lst.insert_end(10)
    lst.insert_end(8)
    lst.insert_end(15)

    for i in range(1,6):
        print(f'Find n = {i} ==> {lst.get_nth(i)}')

def test_index():
    lst = Linkedlist()
    lst.insert_end(6)
    lst.insert_end(10)
    lst.insert_end(8)
    lst.insert_end(15)

    for value in [6,10,8,15,99]:
        print(f'index of {value} ==> {lst.index(value)}')

def test_ind_transposition():
    lst = Linkedlist()
    lst.insert_end(6)
    lst.insert_end(10)
    lst.insert_end(8)
    lst.insert_end(15)

    for value in [15, 15, 15, 15, 15]:
        print(f'Index of {value} ==> {lst.ind_transposition(value)}')
        lst.print_ll()

    for value in [8, 6, 99]:
        print(f'Index of {value} ==> {lst.ind_transposition(value)}')
        lst.print_ll()

def index_transposition2():

    lst = Linkedlist([6, 10, 8, 15])

    for value in [15, 15, 15, 15, 15]:
        print(f'Index of {value} ==> {lst.ind_transposition(value)}')
        lst.print_ll()

    for value in [8, 6, 99]:
        print(f'Index of {value} ==> {lst.ind_transposition(value)}')
        lst.print_ll()


lst = Linkedlist()
lst.insert_end(6)
lst.insert_end(10)
lst.insert_end(8)
lst.insert_end(15)
lst.print_ll()

for i in lst:
    print(i, end='->')  # for __iter__

if __name__ == '__main__':
    test_get_nth()
    print('\n')
    test_index()
    print('\n')
    test_ind_transposition()
    print('\n')
    index_transposition2()
