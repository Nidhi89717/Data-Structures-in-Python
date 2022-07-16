class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0

    def ch_height(self, node): # child height
        if not node:
            return -1
        return node.height

    def update_height(self):
        self.height = 1 + max(self.ch_height(self.left), self.ch_height(self.right))
    
    def balance_factor(self):
        return self.ch_height(self.left) - self.ch_height(self.right)
    
    def is_leaf(self):
        return not self.left and not self.right

class AVLTree:
    def __init__(self, value):
        self.root = Node(value)

    def right_rotation(self, Q):
        print('right_rotation', Q.val)
        P = Q.left
        Q.left = P.right
        P.right = Q
        Q.update_height()
        P.update_height()
        return P 

    def left_rotation(self, P):
        print('left_rotation', P.val)
        Q = P.right
        P.right = Q.left
        Q.left = P 
        P.update_height()
        Q.update_height()
        return Q

    def balance(self, node):
        if node.balance_factor() == 2:
            if node.left.balance_factor() == -1:
                node.left = self.left_rotation(node.left)

            node = self.right_rotation(node)

        elif node.balance_factor() == -2:
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

    def inorder(self, current):
        def process(current):
            if not current:
                return
            process(current.left)
            lst.append(current.val)
            process(current.right)
        
        lst = []
        process(current)
        return lst

    def isValidBST(self, current):
        lst = self.inorder(current.root)
        for idx in range(1, len(lst)):
            if lst[idx-1] >= lst[idx]:
                return False

        return True

def test1():
    tree = AVLTree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]

    for val in lst:
        tree.insert(val)
        tree.isValidBST(tree)

    tree.inorder(tree.root) == sorted(lst + [50])

def test2():
    lst = [20, 60, 15, 45, 70,
           35, 73, 14, 16, 36, 58]

    tree = AVLTree(50)

    for val in lst:
        tree.insert(val)
        tree.isValidBST(tree)

    tree.inorder(tree.root) == sorted(lst + [50])


if __name__ == '__main__':
    test1()
    test2()
