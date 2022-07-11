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
        for idx in range(1,len(lst)):
            if lst[idx-1] > lst[idx]:
                return False
        return True

    def search(self, val):
        def _search(current, val):
            if not current:
                return False
            
            if current.val == val:
                return True

            return _search(current.left, val) or\
                   _search(current.right, val)

        return _search(self.root, val)

    #  Node Deletion using predecessor
    def max_node(self, cur):
        while cur and cur.right:
            cur = cur.right
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

            mx = self.max_node(current.left)
            current.val = mx.val
            current.left = process(current.left, val)
            return current

        process(self.root, val)

# Node Deletion without recursion
    def _delete(self, val):
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
                return current

            if not current.left:
                return current.right

            parent, child = current, current.right
            while child.left:
                parent, child = child, child.left

            if parent.left == child:
                parent.left = child.right
            
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

def test3():
    lst = [20, 70, 15, 45, 60, 73, 35]

    for val in lst:
        tree = Binarytree(50)
        tree.insert(lst)

        tree._delete(val)
        assert not tree.search(val)


def test4():
    lst = [20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58]

    for val in lst:
        tree = Binarytree(50)
        tree.insert(lst)

        tree._delete(val)
        assert not tree.search(val)

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
