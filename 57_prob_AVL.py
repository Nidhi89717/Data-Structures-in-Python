class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.count = 1

    def ch_height(self, node):
        if not node:
            return -1 
        return node.height

    def ch_count(self, node):
        if not node:
            return 0
        return node.count

    def update_height(self):
        self.height = 1 + max(self.ch_height(self.left), self.ch_height(self.right))
        self.count = 1 + self.ch_count(self.left) + self.ch_count(self.right)

    def balance_factor(self):
        return self.ch_height(self.left) - self.ch_height(self.right)

    def is_leaf(self):
        return not self.right and not self.left

class AVLTree:
    def __init__(self, val):
        self.root = Node(val)

    def right_rotation(self, Q):
        print("right_rotation", Q.val)
        P = Q.left
        Q.left = P.right
        P.right = Q
        Q.update_height()
        P.update_height()
        return P 

    def left_rotation(self, P):
        print("left_rotation", P.val)
        Q = P.right
        P.right = Q.left
        Q.left = P 
        Q.update_height()
        P.update_height()
        return Q 
    
    def balance(self, node):
        if node.balance_factor() == 2:
            if node.left.balance_factor() == -1:
                node.left = self.left_rotation(node.left)
            node = self.right_rotation(node)

        if node.balance_factor() == -2:
            if node.right.balance_factor() == 1:
                node.right = self.right_rotation(node.right)
            node = self.left_rotation(node)

        return node

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    current.left = process(current.left, val)

            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    current.right = process(current.right, val)

            current.update_height()
            return self.balance(current)

        if not isinstance(val, list):
            val = [val]
        for item in val:
            self.root = process(self.root, item)

    def inorder(self,current):
        def process(current):
            if not current:
                return 
            process(current.left)
            lst.append(current.val)
            process(current.right)
        lst = []
        process(current)
        return lst

    def isValidBST(self,current):
        lst = self.inorder(current.root)
        for idx in range(1, len(lst)):
            lst[idx-1] > lst[idx]
            return False

        return True

    # Lower Bound
    def lower_bound(self, val):
        lst = self.inorder(self.root)
        #print(lst)
        for i in lst:
            if i >= val:
                return i
        return None

    # Lower Bound
    def _lower_bound(self, val):
        def process(current, val):
            if not current:
                return 
            
            if val <= current.val:
                ans = process(current.left, val)
                if ans is not None:
                    return ans 
                return current.val 
            
            return process(current.right, val)
        
        return process(self.root, val)

    # Upper bound
    def upper_bound(self, val):
        lst = self.inorder(self.root)
        #print(lst)
        for i in lst:
            if i > val:
                return i
        return None

    def _upper_bound(self, val):
        def process(current, val):
            if not current:
                return 
            
            if val < current.val:
                ans = process(current.left, val)
                if ans is not None:
                    return ans 
                return current.val 
            
            return process(current.right, val)
        
        return process(self.root, val)
    
    # Count inversions
    def upper_bound_count(self, val):
        def process(current, val):
            if not current:
                return 0
            
            if val < current.val:
                sum = 1 + current.ch_count(current.right)
                return sum + process(current.left, val)
            
            return process(current.right, val)

        return process(self.root, val)

def count_inversions():
    lst = [10, 5, 8, 2, 12, 6]
    answers = [1, 1, 3, 0, 3] 

    tree1 = AVLTree(lst[0])

    total = 0
    for idx, val in enumerate(lst[1:]):
        inversions = tree1.upper_bound_count(val)
        assert inversions == answers[idx]
        total += inversions
        tree1.insert(val)
    assert total == 8

if __name__=='__main__':
    tree = AVLTree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]
    for val in lst:
        tree.insert(val)

    print("Lower Bound")    
    lst2 = [20, 70, 15, 45, 60, 73, 35, 7, 13, 79]
    for val2 in lst2:
        print(f'{val2},{tree._lower_bound(val2)}')
    print("\nUpper Bound")
    for val2 in lst2:
        print(f'{val2},{tree._upper_bound(val2)}')

    count_inversions()
    print()

#Min nodes from AVL height
def avl_nodes_rec(height):
    if height == 0:
        return 1
    if height == 1:
        return 2
    return 1 + avl_nodes_rec(height - 1) + avl_nodes_rec(height - 2)

def avl_nodes_iter(height):
    if height == 0:
        return 1
    if height == 1:
        return 2

    height -= 1
    a, b = 1, 2
    c = None

    while height:
        c = a + b + 1
        a, b = b, c
        height -= 1
    
    return c

for i in range(20):
    print(i, avl_nodes_iter(i), avl_nodes_rec(i))
