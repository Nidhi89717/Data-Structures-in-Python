# Max-Heap
class Maxheap:
    def __init__(self):
        self.array = []
        self.size = 0

    def _left(self, node):
        p = 2*node + 1
        return -1 if p > self.size else p

    def _right(self, node):
        p = 2*node + 2
        return -1 if p > self.size else p 
    
    def _parent(self, node):
        return -1 if node == 0 else (node-1)//2

    def heapify_up(self, child_pos):
        par_pos = self._parent(child_pos)
        if child_pos == 0 or self.array[par_pos] > self.array[child_pos]:
            return 
        
        self.array[par_pos], self.array[child_pos] = \
            self.array[child_pos], self.array[par_pos]
        self.heapify_up(par_pos)

    def push(self,key):
        if self.size + 1 >= len(self.array):
            self.array.append(None)

        self.array[self.size] = key
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_down(self, par_pos):
        child_pos =self. _left(par_pos)
        right_child =self. _right(par_pos)

        if child_pos == -1:
            return
        
        if right_child != -1 and self.array[right_child] > self.array[child_pos]:
            child_pos = right_child

        if self.array[par_pos] < self.array[child_pos]:
            self.array[par_pos], self.array[child_pos] = self.array[child_pos], self.array[par_pos]
            self.heapify_down(child_pos)

    def top(self):
        assert not self.empty()
        return self.array[0]

    def empty(self):
        return self.size == 0

    def pop(self):
        assert not self.empty()
        self.size -= 1
        result = self.array[0]
        self.array[0] = self.array[self.size]
        self.heapify_down(0)
        return result

if __name__ == '__main__':
    maxheap = Maxheap()
    lst = [2, 17, 22, 10, 8, 37, 14, 19, 7, 6, 5, 12, 25, 30]
     
    for val in lst:
        maxheap.push(val)

    print(maxheap.array)
    print(maxheap.top())
    
    while not maxheap.empty():
        print(maxheap.pop(), end=', ')
    print()

class MinHeap:
    def __init__(self, lst):
        self.array = lst
        self.size = len(lst)

        self._heapify()

    def _heapify(self):
        for i in range(self.size//2-1, -1, -1):
            self.heapify_down(i)

    def _left(self, node):
        p = 2*node + 1
        return -1 if p >= self.size else p 

    def _right(self, node):
        p = 2*node + 2
        return -1 if p >= self.size else p

    def _parent(self,node):
        return -1 if node == 0 else (node-1)//2

    def heapify_up(self, child_pos):
        par_pos = self._parent(child_pos)
        if child_pos == 0 or self.array[par_pos] < self.array[child_pos]:
            return 

        self.array[child_pos], self.array[par_pos] =\
            self.array[par_pos], self.array[child_pos]
        self.heapify_up(par_pos)

    def push(self, key):
        if self.size + 1 >= len(self.array):
            self.array.append(None)

        self.array[self.size]  = key
        self.size += 1
        self.heapify_up(self.size - 1)

    def empty(self):
        return self.size == 0

    def heapify_down(self, par_pos):
        child_pos = self._left(par_pos)
        right_child = self._right(par_pos)

        if child_pos == -1:
            return 

        if right_child != -1 and self.array[right_child]<self.array[child_pos]:
            child_pos = right_child

        if self.array[par_pos] > self.array[child_pos]:
            self.array[par_pos], self.array[child_pos] = \
                self.array[child_pos], self.array[par_pos]
            self.heapify_down(child_pos)

    def pop(self):
        assert not self.empty()
        self.size -= 1
        result = self.array[0]
        self.array[0] = self.array[self.size]
        self.heapify_down(0)
        return result

    # Find smaller values
    def smallest_than(self, val):
        lst = []
        
        def process(par_pos):
            if par_pos == -1 or self.array[par_pos] >= val:
                return

            lst.append(self.array[par_pos])

            process(self._left(par_pos))
            process(self._right(par_pos))

        process(0)
        return lst 

    # Is Heap
    def is_heap(self, par_pos=0):
        if par_pos == -1:
            return True

        left_child = self._left(par_pos)
        right_child = self._right(par_pos)

        if left_child != -1 and self.array[par_pos] > self.array[left_child]:
            return False

        if right_child != -1 and self.array[par_pos] > self.array[right_child]:
            return False

        return self.is_heap(left_child) and self.is_heap(right_child)

    # Heap Sort
    def sort_heap(self):
        for idx in range(self.size-1, -1, -1):
            self.array[0], self.array[idx] = self.array[idx],self.array[0]
            self.size -=1
            self.heapify_down(0)

        self.array.reverse()    

# Using the MinHeap code build a MaxHeap
class MaxHeap:
    def __init__(self, lst):
        lstneg = [-x for x in lst]
        self.minHeap = MinHeap(lstneg)

    def push(self, key):
        self.minheap.push(-key)
    
    def empty(self):
        return self.minHeap.empty()

    def pop(self):
        return -self.minHeap.pop()

if __name__ == "__main__":
    lst = [2, 17, 22, 10, 8, 37, 14, 19, 7, 6, 5, 12, 25, 30]
    maxHeap = MaxHeap(lst)

    while not maxHeap.empty():
        print(maxHeap.pop(), end=', ')
    
    print()

    minHeap = MinHeap(lst)
    print(minHeap.smallest_than(10))
    print()

    assert minHeap.is_heap()

    minHeap.array[0], minHeap.array[-1] = minHeap.array[-1], minHeap.array[0]
    assert not minHeap.is_heap()

    min_heap = MinHeap(lst)
    min_heap.sort_heap()
    print(min_heap.array)
