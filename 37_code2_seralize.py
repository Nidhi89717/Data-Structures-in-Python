class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self,value):
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

    def parenthesize(self):
        def _parenthesize(current):
            repr = '(' + str(current.val)

            if current.left:
                lrepr = _parenthesize(current.left)
            else:
                lrepr = '()'
            
            if current.right:
                rrepr = _parenthesize(current.right)
            else:
                rrepr = '()'

            if lrepr < rrepr:
                repr += lrepr + rrepr + ')'
            else:
                repr += rrepr + lrepr + ')'
            
            return repr

        return _parenthesize(self.root)

if __name__ == '__main__':
    tree = Binarytree(1)
    tree.add([12, 4, 7], ['L', 'L', 'L'])
    tree.add([12, 4, 8], ['L', 'L', 'R'])
    tree.add([12, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    print(tree.parenthesize())
