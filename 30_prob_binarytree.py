class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value_lst, direction_lst):
        assert len(value_lst) == len(direction_lst)

        current = self.root
        for i,val in enumerate(value_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(value_lst[i])
                else:
                    assert current.left.data == value_lst[i]
                current = current.left
            else:
                if not current.right:
                    current.right = Node(value_lst[i])
                else:
                    assert current.right.data == value_lst[i]
                current = current.right
    
    # Tree Max
    def _tree_max(self,current):
            if not current:
                return float('-inf')
            
            return max(current.data, self._tree_max(current.left), self._tree_max(current.right))

    def tree_max(self):
            return self._tree_max(self.root)

# Is Perfect Tree : 1) Recursive Way
    def _tree_height(self, current):
        if not current:
            return -1
        
        return 1 + max(self._tree_height(current.left), self._tree_height(current.right))

    def tree_height(self):
        return self._tree_height(self.root)

    def _is_perfect(self, current, height):
        if not current.left and not current.right:
            return height == 0
        
        if not current.left and current.right:
            return False

        if current.left and not current.right:
            return False

        return self._is_perfect(current.left, height - 1) and \
               self._is_perfect(current.right, height - 1)

    def is_perfect(self):
        h = self.tree_height()
        return self._is_perfect(self.root , h)

    # 2) Formula based
    def tree_node(self, current):
        if not current:
            return 0
        return 1 + self.tree_node(current.left) + self.tree_node(current.right)

    def isperfect(self):
        h = self._tree_height(self.root)
        n= self.tree_node(self.root)
        p = 2 ** (h + 1)
        return n == p - 1

class Solution(object):
# Maximum Depth of Binary Tree
# Maximum depth is the number of nodes along the longest node
    def maxdepth(self,current):
        if not current:
            return 0
        
        return 1 + max(self.maxdepth(current.left), self.maxdepth(current.right))

# Sum of left leaves
    def sumofleftleaves(self, root, is_left = False):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return root.data if is_left else 0

        return self.sumofleftleaves(root.left, True) + self.sumofleftleaves(root.right, False)

# Cousins in Binary Tree
    def find(self, root, parent, value, depth=0):
        if not root:
            return None, depth

        if root.data == value:
            return parent, depth
        
        lparent, ldepth = self.find(root.left, root, value, depth+1)

        if lparent:
            return lparent, ldepth

        return self.find(root.right, root, value, depth+1)

    def iscousins(self,root,x,y):
        xparent , xdepth = self.find(root, None, x)
        yparent , ydepth = self.find(root, None, y)

        return xdepth == ydepth and xparent != yparent
        
if __name__ == '__main__':
    tree = Binarytree(1)
    tree.add([2, 4, 7],['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 15], ['R', 'R', 'L'])

    assert tree.tree_max() == 15

    sol = Solution()
    assert sol.maxdepth(tree.root) == 4
    assert sol.sumofleftleaves(tree.root) == 22

    assert sol.iscousins(tree.root, 9, 10) == True
    assert sol.iscousins(tree.root, 5, 4) == False
    assert sol.iscousins(tree.root, 5, 6) == True

    
    tree2 = Binarytree(1)

    assert tree2.is_perfect()
    assert tree2.isperfect()

    tree2.add([2], ['L'])
    assert not tree2.is_perfect()
    assert not tree2.isperfect()

    tree2.add([3], ['R'])
    assert tree2.is_perfect()
    assert tree2.isperfect()

    tree2.add([2, 4, 7], ['L', 'L', 'L'])
    tree2.add([2, 4, 8], ['L', 'L', 'R'])
    tree2.add([2, 5, 9], ['L', 'R', 'R'])
    tree2.add([3, 6, 15], ['R', 'R', 'L'])
    assert not tree2.is_perfect()
    assert not tree2.isperfect()

    tree2.add([2, 5, 13], ['L', 'R', 'L'])
    tree2.add([3, 6, 12], ['R', 'R', 'R'])
    tree2.add([3, 14, 15], ['R', 'L', 'L'])
    tree2.add([3, 14, 16], ['R', 'L', 'R'])
    assert tree2.is_perfect()
    assert tree2.isperfect()
