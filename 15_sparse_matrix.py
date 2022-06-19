class Node:
    def __init__(self, index, data=None, next=None, prev=None):
        self.data = data
        self.index = index
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}@{self.index}'


class SparseArray:
    def __init__(self, array_length):
        self.tail = self.head = Node(-1, None)
        self.length = 1  # total number of nodes
        self.array_length = array_length

    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def _embed_after(self, node, index, data=None):
        new_node = Node(index, data)
        self.length += 1
        self._link(new_node, node.next)
        self._link(node, new_node)

        return new_node

    def get_node(self, index, is_create_if_missing=True):
        prev = self.head
        while prev.next and prev.next.index < index:
            prev = prev.next

        if prev.next and prev.next.index == index:  # found
            return prev.next

        if not is_create_if_missing:
            return None

        return self._embed_after(prev, index, None)

    def set_value(self, index, data):
        assert 0 <= index < self.array_length
        self.get_node(index, True).data = data

    def get_value(self, index):
        assert 0 <= index < self.array_length
        node = self.get_node(index, False)
        if not node:
            return None
        return node.data

    def add(self, other):  # O(Nodes1 * Nodes2)
        assert self.array_length == other.array_length
        if not self.array_length:
            return

        h = other.head.next
        while h:
            node = self.get_node(h.index, True)
            if node.data is None:
                node.data = h.data
            else:
                node.data += h.data
            h = h.next

    def __repr__(self):
        represent = ''
        cur = self.head.next

        while cur is not None:
            represent += str(cur)
            cur = cur.next
            if cur:
                represent += ', '

        return represent

    def print_as_array(self):
        cur = self.head.next

        for c in range(self.array_length):
            if cur and cur.index == c:
                print(cur.data, end=' ')
                cur = cur.next
            else:
                print(0, end=' ')
        print()


class SparseMatrix:
    def __init__(self, rows, cols):
        # create a linked list here to represent the rows we have
            # later, each row will be another linked list for the columns of this ROW
        self.rows_sparse_array = SparseArray(rows)
        self.rows, self.cols = rows, cols

    def set_value(self, row, col, data):
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols

        # get the target row
        row_node = self.rows_sparse_array.get_node(row, True)
        
        # if the row doesn't exist it will be created, but its data is none then
        if row_node.data is None:
            # Now, we create a linked list inside this node to represent the columns
            row_node.data = SparseArray(self.cols)
        
        # get the exact (row, col) node and set tis data
        col_node = row_node.data.get_node(col, True)
        col_node.data = data

    def get_value(self, row, col):
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols

        row_node = self.rows_sparse_array.get_node(row, False)
        if not row_node:
            return None

        col_node = row_node.get_node(col, False)
        if not col_node:
            return None

        return col_node.data

    def add(self, other):
        assert self.rows == other.rows and self.cols == other.cols

        # Iterate row by row. Find corresponding row. Add together
        other_row_node = other.rows_sparse_array.head.next
        while other_row_node:
            self_row_node = self.rows_sparse_array.get_node(other_row_node.index, True)

            if self_row_node.data is None:
                self_row_node.data = SparseArray(self.cols)

            self_row_node.data.add(other_row_node.data)
            other_row_node = other_row_node.next

    def __repr__(self):
        represent = ''
        row_node = self.rows_sparse_array.head.next

        while row_node is not None:
            if represent != '':
                represent += '\n'
            represent += f'Row {row_node.index}: '
            represent += str(row_node.data)
            row_node = row_node.next
        return represent

    def print_as_2darray(self, end='\n'):
        row_node = self.rows_sparse_array.head.next

        empty_row = ' '.join(['0'] * self.cols)

        for r in range(self.rows):
            if row_node and row_node.index == r:
                row_node.data.print_as_array()
                row_node = row_node.next
            else:
                print(empty_row)

        print("")

mat = SparseMatrix(7, 7)
# (row, col, value) order
mat.set_value(2, 5, 900)
mat.set_value(2, 5, 8)
mat.set_value(1, 6, -3)
mat.set_value(6, 6, -8)
mat.set_value(3, 0, 9)
mat.set_value(3, 3, 7)
mat.set_value(3, 5, 4)
mat.set_value(5, 5, 1)
mat.set_value(5, 2, 6)

result = str(mat)
print(result)
print()
mat.print_as_2darray()
print()

mat2 = SparseMatrix(7, 7)
mat2.set_value(1, 6, 8)
mat2.set_value(3, 1, 4)
mat2.print_as_2darray()
print()

mat.add(mat2)
result = str(mat)

print(result)
print()

mat.print_as_2darray()
