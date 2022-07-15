import heapq
# Kth Largest number (stream)
class KthLargestProcessor:
    def __init__(self, k):
        self.k = k
        self.min_heap = []

    def next(self, number):
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, number)
        elif number > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, number)

        return self.min_heap[0]

if __name__ =="__main__":
    lst = [2, 17, 22, 10, 8, 37, 14, 19, 7, 6, 5, 12, 25, 30]
    k = 4

    processor = KthLargestProcessor(k)

    for idx, val in enumerate(lst):
        ans = processor.next(val)
        print(idx, ans)

        right_answer = heapq.nlargest(k, lst[:idx+1])
        assert ans == right_answer[-1]
    print()

class PriorityQueue:
    def __init__(self):
        self.array = []
        self.value = []
        self.size = 0

    def _left(self, node):
        p = 2*node + 1
        return -1 if p > self.size else p 

    def _right(self, node):
        p = 2*node + 2
        return -1 if p >self.size else p 

    def _parent(self, node):
        return -1 if node == 0 else (node - 1)//2

    def heapify_down(self, par_pos):
        child_pos = self._left(par_pos)
        right_child = self._right(par_pos)

        if child_pos == -1:
            return 

        if right_child != -1 and self.array[right_child] > self.array[child_pos]:
            child_pos = right_child

        if self.array[par_pos] < self.array[child_pos]:
            self.array[par_pos], self.array[child_pos] = self.array[child_pos],self.array[par_pos]
            self.value[par_pos], self.value[child_pos] = self.value[child_pos],self.value[par_pos]
            self.heapify_down(child_pos)

    def heapify_up(self, child_pos):
        par_pos = self._parent(child_pos)
        if child_pos == 0 or self.array[par_pos] > self.array[child_pos]:
            return

        self.array[child_pos], self.array[par_pos] = self.array[par_pos], self.array[child_pos] 
        self.value[child_pos], self.value[par_pos] = self.value[par_pos], self.value[child_pos]
        self.heapify_up(par_pos)

    def enqueue(self, value, priority):
        if self.size + 1 >= len(self.array):
            self.array.append(None)
            self.value.append(None)

        self.array[self.size] = priority
        self.value[self.size] = value
        self.size += 1
        self.heapify_up(self.size - 1)

    def empty(self):
        return self.size == 0

    def dequeue(self):
        assert not self.empty()
        self.size -= 1
        result = self.value[0]
        self.array[0] = self.array[self.size]
        self.value[0] = self.value[self.size]
        self.heapify_down(0)
        return result

if __name__ == "__main__":

    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)
    tasks.enqueue(7761, 7)

    print(tasks.dequeue())
    print(tasks.dequeue())

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    while not tasks.empty():
        print(tasks.dequeue(), end = ' ')
    print()

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)

        current = self.root
        for i, val in enumerate(values_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(values_lst[i])
                else:
                    assert current.left.val == values_lst[i]
                current = current.left

            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.val == values_lst[i]
                current = current.right

    def level_order_traversal_sorted(self):
        nodes_heap_cur = [(self.root.val, self.root)]
        nodes_heap_next = []
        level = 0

        while nodes_heap_cur:
            print(f'\nLevel{level}:', end=' ')
            while nodes_heap_cur:
                val, cur = heapq.heappop(nodes_heap_cur)

                print(val, end=' ')

                if cur.left:
                    heapq.heappush(nodes_heap_next,(cur.left.val, cur.left))
                if cur.right:
                    heapq.heappush(nodes_heap_next,(cur.right.val, cur.right))

            level += 1
            nodes_heap_cur, nodes_heap_next = nodes_heap_next, nodes_heap_cur

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([20, 50, 8], ['L', 'L', 'L'])
    tree.add([20, 50, 17], ['L', 'L', 'R'])
    tree.add([20, 40, 10], ['L', 'R', 'L'])
    tree.add([20, 40, 11], ['L', 'R', 'R'])

    tree.add([90, 60, 88], ['R', 'L', 'L'])
    tree.add([90, 60, 13], ['R', 'L', 'R'])
    tree.add([90, 7, 95], ['R', 'R', 'L'])
    tree.add([90, 7, 15], ['R', 'R', 'R'])

    tree.level_order_traversal_sorted()
