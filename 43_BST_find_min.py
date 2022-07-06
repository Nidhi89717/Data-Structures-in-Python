class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def min(self):
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val

if __name__ == '__main__':
    tree = Binarytree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    print(tree.min())
