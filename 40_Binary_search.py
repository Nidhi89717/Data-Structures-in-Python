class Node:
    def __init__(self, val = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)
        current = self.root

        for i, val in enumerate(values_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(values_lst[i])
                else:
                    assert current.left.val == values_lst[i] 
                current = current.left

            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.val == values_lst[i]
                current = current.right

    def search(self, val):
        def _search(current, val):
            if not current:
                return False
            
            if current.val == val:
                return True

            return _search(current.left, val) or\
                   _search(current.right, val)

        return _search(self.root, val)

    def bsearch(self,val):
        def _search(current,val):
            if not current:
                return False

            if val == current.val:
                return True

            if val < current.val:
                return _search(current.left, val)
            return _search(current.right, val)

        return _search(self.root, val)

if __name__ == '__main__':
    tree = Binarytree(50)
    tree.add([70, 73], ['R', 'R'])
    tree.add([70, 60], ['R', 'L'])
    tree.add([20, 15], ['L', 'L'])
    tree.add([20, 45, 35], ['L', 'R', 'L'])

    print(tree.search(50))
    print(tree.search(35))
    print(tree.search(90))

    print(tree.bsearch(50))
    print(tree.bsearch(35))
    print(tree.bsearch(90))
