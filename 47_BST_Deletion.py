class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

class Binarytree:
    def __init__(self, value):
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
        lst = self.inorder(current)
        for idx in range(1, len(lst)):
            if lst[idx-1] >= lst[idx]:
                return False
            
        return True

    def search(self, val):
        def _search(current, val):
            if not current:
                return False
            
            if current.val == val:
                return True

            if val < current.val:
                return _search(current.left, val)

        return _search(self.root, val)

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
                return current.left

            if not current.left:
                return current.right

            mn = self.min_node(current.right)
            current.val = mn.val
            current.right = process(current.right, mn.val)
            return current

        process(self.root, val)

def test1():
    lst = [20, 70, 15, 45, 60, 73, 35]

    for val in lst:
        tree = Binarytree(50)
        tree.insert(lst)

        tree.delete(val)
        assert not tree.search(val)


def test2():
    lst = [20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58]

    for val in lst:
        tree = Binarytree(50)
        tree.insert(lst)

        tree.delete(val)
        assert not tree.search(val)


if __name__ == '__main__':
    test1()
    test2()
