class Minheap:
    def __init__(self):
        self.array = []
        self.size = 0

    def _left(self, node):
        p = 2*node + 1
        return -1 if p >= self.size else p

    def _right(self,node):
        p = 2*node + 2
        return -1 if p >= self.size else p

    def _parent(self, node):
        return -1 if node == 0 else (node-1) // 2

    def heapify_up(self, child_pos):
        par_pos = self._parent(child_pos)
        if child_pos == 0 or self.array[par_pos] < self.array[child_pos]:
            return

        self.array[child_pos], self.array[par_pos] = self.array[par_pos], self.array[child_pos]
        self.heapify_up(par_pos)

    def push(self,key):
        if self.size + 1 > len(self.array):
            self.array.append(None)

        self.array[self.size] = key
        self.size += 1
        self.heapify_up(self.size - 1)

    def top(self):
        assert not self.empty()
        return self.array[0]

    def empty(self):
        return self.size == 0

    def heapify_down(self, parent_pos):
        child_pos = self._left(parent_pos)
        right_child = self._right(parent_pos)

        if child_pos == -1:
            return 

        if right_child != 1 and self.array[right_child] < self.array[child_pos]:
            child_pos = right_child

        if self.array[parent_pos] > self.array[child_pos]:
            self.array[parent_pos], self.array[child_pos] = self.array[child_pos], self.array[parent_pos]
            self.heapify_down(child_pos)

    def pop(self):
        assert not self.empty()
        self.size -=1
        result = self.array[0]
        self.array[0] = self.array[self.size]
        self.heapify_down(0)
        return result

if __name__ == '__main__':
    minheap = Minheap()

    lst = [2, 17, 22, 10, 8, 37, 14, 19, 7, 6, 5, 12, 25, 30]

    for val in lst:
        minheap.push(val)

    print(minheap.array)
    
    while not minheap.empty():
        print(minheap.pop(), end=', ')
