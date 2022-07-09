class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self):
        nodes_lst = []

        def process(current):
            if not current:
                return 

            nodes_lst.append(current.val)
            process(current.left)
            process(current.right)
        
        process(self.root)
        return nodes_lst

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    process(current.left, val)

            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    process(current.right, val)

        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)

    # BST from preorder
    # Method 1 O(n^2)
    def get_tree_from_preorder(self, nodes_lst):
        def process(nodes_lst):
            if not nodes_lst:
                return None

            node = Node(nodes_lst[0])
            split = None
            for idx in range(1, len(nodes_lst)):
                if nodes_lst[idx] > nodes_lst[0]:
                    split = idx
                    break
            
            if split is None:
                node.left = process(nodes_lst[1:])
            else:
                node.left = process(nodes_lst[1:split])
                node.right = process(nodes_lst[split:])
            
            return node

        tree = Binarytree(None)
        tree.root = process(nodes_lst)
        return tree


    # Method 2  O(n)
    def preorder2(self):
        import collections
        nodes_deque = collections.deque()
        
        def process(current):
            if not current:
                return 

            nodes_deque.append(current.val)
            process(current.left)
            process(current.right)  
        
        process(self.root) 
        return nodes_deque

    def get_tree_from_preorder2(self, nodes_deque):
        def process(nodes_deque, mn, mx):
            def next_between(nodes_deque, mn, mx):
                if not nodes_deque:
                    return False
                return mn < nodes_deque[0] < mx 

            if not nodes_deque:
                return None

            node = Node(nodes_deque.popleft())

            if next_between(nodes_deque, mn, node.val):
                node.left = process(nodes_deque, mn, node.val)

            if next_between(nodes_deque, node.val, mx):
                node.right = process(nodes_deque, node.val, mx)

            return node

        tree = Binarytree(None)
        tree.root = process(nodes_deque, float('-inf'), float('inf'))
        return tree

    # BST from level-order traversal
    def level_order_traversal(self):
        import collections
        nodes_queue =collections.deque()
        nodes_queue.append(self.root)

        traversal = collections.deque()

        while nodes_queue:
            sz = len(nodes_queue)
            for step in range(sz):
                cur = nodes_queue.popleft()

                traversal.append(cur.val)

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)

        return traversal

    def get_tree_from_levelorder(self, nodes_deque):
        def next_between(nodes_deque, mn, mx):
            return nodes_deque and mn < nodes_deque[0] < mx

        import collections
        nodes_queue = collections.deque()

        tree = Binarytree(nodes_deque.popleft())
        nodes_queue.append([tree.root, float('-inf'), float('inf')])

        while nodes_queue:
            cur, mn, mx = nodes_queue.popleft()

            if next_between(nodes_deque, mn, cur.val):
                cur.left = Node(nodes_deque.popleft()) 
                nodes_queue.append([cur.left, mn, cur.val])

            if next_between(nodes_deque, cur.val, mx):
                cur.right = Node(nodes_deque.popleft())
                nodes_queue.append([cur.right, cur.val, mx])

        return tree 

def test1():
    tree = Binarytree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    lst1 = tree.preorder()    
    tree2 = tree.get_tree_from_preorder(lst1.copy())
    lst2 = tree2.preorder()

    assert lst1 == lst2


def test2():
    tree = Binarytree(50)
    tree.insert([20, 60, 15, 45, 70, 35, 73, 14, 16, 36, 58])

    lst1 = tree.preorder()
    tree2 = tree.get_tree_from_preorder(lst1.copy())
    lst2 = tree2.preorder()

    assert lst1 == lst2

def test3():
    tree = Binarytree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    deq1 = tree.preorder2()
    tree2 = tree.get_tree_from_preorder2(deq1.copy())
    deq2 = tree2.preorder2()

    assert deq1 == deq2

def test4():
    tree = Binarytree(50)
    tree.insert([20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58])

    deq1 = tree.preorder2()
    tree2 = tree.get_tree_from_preorder2(deq1.copy())
    deq2 = tree2.preorder2()

    assert deq1 == deq2

def test5():
    tree = Binarytree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    deq1 = tree.level_order_traversal()
    tree2 = tree.get_tree_from_levelorder(deq1.copy())
    deq2 = tree2.level_order_traversal()

    assert deq1 == deq2


def test6():
    tree = Binarytree(50)
    tree.insert([20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58])

    deq1 = tree.level_order_traversal()
    tree2 = tree.get_tree_from_levelorder(deq1.copy())
    deq2 = tree2.level_order_traversal()

    assert deq1 == deq2
    
if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
