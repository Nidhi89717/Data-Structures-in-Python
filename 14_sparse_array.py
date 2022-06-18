class Node:
    def __init__(self, index, data=None, next = None, prev = None):
        self.data = data
        self.index = index
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}@{self.index}'

class SparseArray:
    def __init__(self,array_length):
        # Create a dummy node of index = -1, to make the code the coding shorter and more robost
        self.tail = self.head = Node(-1,None)
        self.length = 1
        self.array_length = array_length

    @staticmethod
    def _link(first,second):
        if first:
            first.next = second
        if second:
            second.prev= first

    def _embed_after(self,node,index,data=None):
        # Add a node with value between node and its next node
        new_node = Node(index,data)
        self.length += 1
        self._link(new_node,node.next)
        self._link(node,new_node)

        return new_node

    # Return the node of this index
    def get_node(self,index,is_create_if_missing = True):
        # Find the largest node where node.index < index
        prev = self.head
        while prev.next and prev.next.index < index:
            prev = prev.next

        if prev.next and prev.next.index == index:
            return prev.next

        if not is_create_if_missing:
            return None

        return self._embed_after(prev,index,None)

    def set_value(self,index,data):
        assert 0 <= index < self.array_length
        self.get_node(index,True).data = data

    def get_value(self,index):
        assert 0 <= index < self.array_length
        node = self.get_node(index,False)
        if not node:
            return None
        return node.data

    def add(self,other):
        assert self.array_length == other.array_length
        if not self.array_length:
            return

        # Iterate on the other first, add it to the current one
        h = other.head.next
        while h:
            node = self.get_node(h.index, True)
            if node.data is None:
                node.data = h.data
            else:
                node.data += h.data
            h = h.next

    def print_as_array(self):
        cur =  self.head.next

        for c in range(self.array_length):
            if cur and cur.index == c:
                print(cur.data,end=' ')
                cur = cur.next
            else:
                print(0,end=' ')        
        print()

    def __repr__(self):
        represent = ''
        cur=self.head.next

        while cur is not None:
            represent += str(cur)
            cur = cur.next
            if cur:
                represent += ','

        return represent

array = SparseArray(15)
array.set_value(5,20)
array.set_value(2,20)
array.set_value(8,80)
array.set_value(4,4000)
array.set_value(4,40)

array.print_as_array()
result = str(array)
print(result)
print(array.get_value(4),array.get_value(9))

array2 = SparseArray(15)
array2.set_value(5, 3)
array2.set_value(14, 100)
print(array2)

array.add(array2)
result1 = str(array)
print(result1)
