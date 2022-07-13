class Minheap:
    def __init__(self, lst):
        self.array = lst
        self.size = len(lst)

        #self.heapify()
        self._heapify()
    
    # Floyd heapfiy algorithm 
    def heapify(self):
        for i in range(self.size-1, -1, -1):
            self.heapify_down(i)
    
    # Optimization - Skipping the leaves
    def _heapify(self):
        for i in range(self.size//2 - 1, -1, -1):
            self.heapify_down(i)

    def _left(self, node):
        p = 2*node + 1
        return -1 if p >= self.size else p 

    def _right(self,node):
        p = 2*node + 2
        return -1 if p >= self.size else p 
    
    def empty(self):
        return self.size == 0

    def heapify_down(self, par_pos):
        child_pos = self._left(par_pos)
        right_child = self._right(par_pos)

        if child_pos == -1:
            return 

        if right_child != -1 and self.array[right_child] < self.array[child_pos]:
            child_pos = right_child

        if self.array[par_pos] > self.array[child_pos]:
            self.array[par_pos], self.array[child_pos] = self.array[child_pos], self.array[par_pos]
            self.heapify_down(child_pos)

    def pop(self):
        assert not self.empty()
        self.size -= 1
        result = self.array[0]
        self.array[0] = self.array[self.size]
        self.heapify_down(0)
        return result

if __name__ == '__main__':
    lst = [2, 17, 22, 10, 8, 37, 14, 19, 7, 6, 5, 12, 25, 30]
    minHeap = Minheap(lst)

    while not minHeap.empty():
        print(minHeap.pop(), end=', ')
