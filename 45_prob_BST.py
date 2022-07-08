# Parent Link
class Node:
    def __init__(self, val = None, parent=None, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val, current)
                else:
                    process(current.left, val)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val, current)
                else:
                    process(current.right, val)

        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)

    def min(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def find_node(self,val):
        def process(current, val):
            if not current:
                return None
            if val == current.val:
                return current
            if val < current.val:
                return process(current.left, val)
            return process(current.right, val)

        return process(self.root, val)

    def successor (self, target):
        child = self.find_node(target)
        if not child:
            return None

        if child.right:
            return self.min(child.right)
        if not child.parent:
            return None

        parent = child.parent
        while parent and parent.right == child:
            child, parent = parent, parent.parent

        if not parent:
            return None
        return parent.val

if __name__ == '__main__':
    tree = Binarytree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]
    tree.insert(lst)

    lst.append(50)
    lst.append(51)
    lst = sorted(lst)
    print(lst)

    for val in lst:
        print(val, tree.successor(val))

#  Queries of successors
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self,value):
        self.root = Node(value)

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

    def successor_queries(self, deque):
        traversal, answers = [], []

        def process(current):
            if not current or not deque:
                return 
            
            if deque[0] < current.val:
                process(current.left)

            if deque and traversal and traversal[-1] == deque[0]:
                answers.append((deque[0], current.val))
                deque.popleft()

            traversal.append(current.val)

            if deque and deque[0] >= current.val:
                process(current.right)
            
        process(self.root)
        return answers

if __name__ == '__main__':

    tree = Binarytree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]
    tree.insert(lst)

    lst.append(50)
    lst = sorted(lst)

    import collections
    nodes_queue = collections.deque()

    for val in lst:
        nodes_queue.append(val)

    print(tree.successor_queries(nodes_queue))

# Is degenerate ?
def is_degenerate(preorder):
    if len(preorder) <= 2:
        return True

    mn, mx = float('-inf'), float('inf')

    for i in range(1, len(preorder)):
        if not (mn < preorder[i] < mx):
            return False

        if preorder [i] > preorder[i - 1]:
            mn = preorder[i - 1]
        else:
            mx = preorder[i - 1]

    return True

if __name__ == '__main__':
    assert is_degenerate([25, 8, 11, 13, 12]) == True
    assert is_degenerate([100, 70, 101]) == False
    assert is_degenerate([100, 70, 60, 75]) == False
    assert is_degenerate([100, 70, 60, 65]) == True
    assert is_degenerate([9, 8, 7, 6, 5, 4, 3]) == True
    assert is_degenerate([500, 400, 300, 200 , 250 , 275, 260]) == True
    assert is_degenerate([500, 400, 300, 200 , 250 , 275, 260, 280]) == False
