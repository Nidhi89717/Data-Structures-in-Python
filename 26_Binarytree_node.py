class Node:
    def __init__(self, val = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    root.left = node2
    root.right = node3
    
    node2.left = node4
    node2.right = node5

    node5.right = node7

    node3.right = node6

    node6.left = node8

    print(root.left.right.right.val)  # 7
    print(    node2.right.right.val)  # 7
    print(          node5.right.val)  # 7
    print(                node7.val)  # 7

    print(root.right.right.val)        # 6
    print(root.right.right.left.val)   # 8
    print(root.right.right.right)      # None
