class Node:
    def __init__(self,val = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_postorder(current):
    if not current:
        return
    print_postorder(current.left)
    print_postorder(current.right)
    print(current.val, end=' ')

if __name__ == '__main__':
    plus = Node('+')
    node2 = Node('2')
    node3 = Node('3')
    plus.left = node2
    plus.right = node3

    multiply = Node('*')
    node4 = Node(4)
    multiply.left = plus
    multiply.right = node4

    print_postorder(multiply)
