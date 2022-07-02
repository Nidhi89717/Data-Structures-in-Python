class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def print_preorder(self):
        def preorder(current):
            print(current.val, end=' ')

            if current.left:
                preorder(current.left)
            else:
                print(-1, end=' ')
            
            if current.right:
                preorder(current.right)
            else:
                print(-1, end=' ')
        
        preorder(self.root)

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

if __name__ == '__main__':
    tree = Binarytree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    tree.print_preorder()
