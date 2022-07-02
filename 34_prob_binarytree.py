class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
     
    def is_leaf(self):
        return not self.left and not self.right

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

# Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildtree(self, preorder, inorder):
        if not inorder:
            return None
        
        root = Node(preorder.pop(0))
        pos = inorder.index(root.val)

        root.left = self.buildtree(preorder, inorder[:pos])
        root.right = self.buildtree(preorder, inorder[pos + 1:])

        return root

Solution().buildtree([1,2,4,7,8,5,9,3,6,10],[7,4,8,2,5,9,1,3,10,6])

# Generate a full binary tree
class Binarytree:
    def __init__(self,value):
        self.root = Node(value)
    
    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)
        current = self.root

        for i,val in enumerate(values_lst):
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

    def preorder_leaf(self):
        import collections
        preorder = collections.deque()

        def _preorder_leaf(current):
            if not current:
                return 
            preorder.append([current.val, current.is_leaf()])
            if not current.is_leaf():
                _preorder_leaf(current.left)
                _preorder_leaf(current.right)

        _preorder_leaf(self.root)

        return preorder

    def create_from_preorder(self,preorder_dq):
        def build(preorder_dq):
            val, is_leaf = preorder_dq.popleft()
            current = Node(val)

            if not is_leaf:
                current.left = build(preorder_dq)
                current.right = build(preorder_dq)
            return current

        bt = Binarytree(Node)
        bt.root = build(preorder_dq)
        return bt

if __name__ == '__main__':
    tree = Binarytree(1)
    tree.add([3], ['R'])
    tree.add([2, 4], ['L', 'L'])
    tree.add([2, 5, 7], ['L', 'R', 'R'])
    tree.add([2, 5, 6], ['L', 'R', 'L'])

    deq = tree.preorder_leaf()

    tree2 = tree.create_from_preorder(deq)
    print(tree2.preorder_leaf())
