# priority_queue
class Node:
    def __init__(self, val=None, attached_data=None, left=None, right=None):
        self.val = val 
        if attached_data is None:
            self.data_list = []
        else:
            self.data_list = [attached_data]
        self.left = left
        self.right = right
        self.height = 0

    def ch_height(self, node):
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
    def __init__(self, value, attached_data=None):
        self.root = Node(value, attached_data)
    
    def right_rotation(self, Q):
        P = Q.left 
        Q.left = P.right 
        P.right = Q 
        Q.update_height()
        P.update_height()
        return P 

    def left_rotation(self, P):
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

    def insert(self, val, attached_data = None):
        def process(current, val, attached_data):
            if val < current.val:
                if not current.left:
                    current.left = Node(val, attached_data)
                else:
                    current.left = process(current.left, val, attached_data)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val, attached_data)
                else:
                    current.right = process(current.right, val, attached_data)
            else:
                current.data_list.append(attached_data) 
        
            current.update_height()
            return self.balance(current)

        self.root = process(self.root, val, attached_data)

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

    def min_node(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur
    
    def delete(self, val):
        def process(current, val):
            if not current:
                return 
            
            if val < current.val:
                current.left = process(current.left, val)
                return current

            if val > current.val:
                current.right = process(current.right, val)
                return current
            
            if current.is_leaf():
                return None 
            
            if not current.right:
                current = current.left 
            elif not current.left:
                current = current.right
            
            else:
                mn = self.min_node(current.right)
                current.val = mn.val 
                current.right = process(current.right, mn.val)

            current.update_height()
            return self.balance(current)
        self.root = process(self.root, val)
    
    def max_node(self):
        cur = self.root 
        while cur and cur.right:
            cur = cur.right 
        return cur 
    

class PriorityQueue:
    def __init__(self):
        self.avl = AVLTree(-1)
        self.items_cnt = 0

    def enqueue(self, task_id, priority):
        self.items_cnt += 1
        self.avl.insert(priority, attached_data = task_id)
    
    def dequeue(self):
        assert not self.empty()
        self.items_cnt -= 1

        bst_node = self.avl.max_node()
        item = bst_node.data_list.pop()

        if not bst_node.data_list:
            self.avl.delete(bst_node.val)
        
        return item 
    
    def empty(self):
        return self.items_cnt == 0
    
if __name__ == '__main__':

    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)

    print(tasks.dequeue())  # 3161
    print(tasks.dequeue())  # 3111

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    while not tasks.empty():
        print(tasks.dequeue(), end=' ')
