class Node:
    def __init__(self, val = None, right = None, left = None):
        self.val = val
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def bsearch(self, val):
        def process(current, val):
            if not current:
                return False

            if val == current.val:
                return True
            if val < current.val:
                return process(current.left, val)
            return process(current.right, val)

        return process(self.root, val)

    def insertion(self, val):
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

if __name__ == '__main__':
    tree = Binarytree(50)
    tree.insertion([20, 70, 15, 45, 60, 73, 35])

    print(tree.bsearch(50))
    print(tree.bsearch(35))
    print(tree.bsearch(90))
