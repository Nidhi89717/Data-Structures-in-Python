#AVL Dictionary
class Node:
    def __init__(self, val=None, is_full_word = True, left = None, right=None):
        self.val = val
        self.is_full_word = is_full_word
        self.left = left
        self.right = right
        self.height = 0

    def ch_height(self, node):
        if not node:
            return -1
        return node.height 

    def update_height(self):
        self.height = 1 + max(self.ch_height(self.left), self.ch_height(self.left))

    def balance_factor(self):
        return self.ch_height(self.left) - self.ch_height(self.right)

    def is_leaf(self):
        return not self.left and not self.right

class AVLTree:
    def __init__(self, value, is_full_word):
        self.root = Node(value, is_full_word)
    
    def right_rotation(self, Q):
        print("right_rotation", Q.val)
        p = Q.left 
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
        P.update_height()
        Q.update_height()
        return Q 

    def balance(self,node):
        if node.balance_factor() == 2:
            if node.left.balance_factor() == 1:
                node.left = self.left_rotation(node.left)
            
            node = self.right_rotation(node)

        elif node.balance_factor() == -2:
            if node.right.balance_factor() == 1:
                node.right = self.right_rotation(node.right)
            
            node = self.left_rotation(node)

        return node 

    def insert(self, val, is_full_word):
        def process(current,val, is_full_word):
            if val < current.val:
                if not current.left:
                    current.left = Node(val, is_full_word)
                else:
                    current.left = process(current.left, val, is_full_word)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val, is_full_word)
                else:
                    current.right = process(current.right, val, is_full_word)
            elif is_full_word:
                current.is_full_word = 1
            
            current.update_height()
            return self.balance(current)

        self.root = process(self.root, val, is_full_word)

    def insert_string(self, target):
        if target == "":
            return 

        cur = ''
        for i in range(len(target)):
            cur += target[i]
            self.insert(cur, i == len(target)-1)
    
    def search_word_status(self, val):
        def process(current, val):
            if not current:
                return -1
            
            if current.val == val:
                return current.is_full_word
            if val < current.val:
                return process(current.left, val)
            
            return process(current.right, val)
        
        return process(self.root, val)

    def word_exist(self,target):
        return self.search_word_status(target) == 1
    
    def prefix_exist(self, target):
        return self.search_word_status(target) != -1

if __name__ == '__main__':
    tree = AVLTree("", True)

    tree.insert_string("abcd")
    tree.insert_string("xyz")

    print(tree.word_exist("abcd"))      
    print(tree.word_exist("ab"))        
    print(tree.prefix_exist("abcd"))    
    print(tree.prefix_exist("ab"))      
    tree.insert_string("ab")

    print(tree.word_exist("ab"))        
    print(tree.word_exist("cd"))        
    print(tree.word_exist("abcde"))
