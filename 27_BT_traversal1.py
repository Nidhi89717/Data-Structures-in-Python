class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_postorder(current):
    print(current.left.val, end=' ')
    print(current.right.val, end=' ')
    print(current.val, end = ' ')

def print_preorder(current):
    print(current.val, end=' ')
    print(current.left.val, end=' ')
    print(current.right.val, end=' ')

def print_inorder(current):
    print(current.left.val, end=' ')
    print(current.val, end=' ')
    print(current.right.val, end=' ')

if __name__ == '__main__':
    plus = Node('+')
    node2 = Node(2)
    node3 = Node(3)
    plus.left = node2
    plus.right= node3

    print_inorder(plus)
    print()
    print_postorder(plus)
    print()
    print_preorder(plus)
