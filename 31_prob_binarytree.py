class Node:
    def __init__(self, val = None, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

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
                    assert current.left.val == value_lst[i]
                current = current.left

            else:
                if not current.right:
                    current.right = Node(value_lst[i])
                else:
                    assert current.right.val == value_lst[i]
                current = current.right

    #Inorder iterative
    def inorder_iterative(self):
        nodes_stk = []

        nodes_stk.append([self.root, False])
        res = []

        while nodes_stk:
            current, is_completed = nodes_stk[-1]
            nodes_stk.pop()

            if is_completed:
                res.append(current.val)
            
            else:
                if current.right:
                    nodes_stk.append([current.right, False])

                nodes_stk.append([current, True])

                if current.left:
                    nodes_stk.append([current.left, False])
            
        return res

    # Left tree boundary
    def _traverse_left_boundry(self, current):
        if not current:
            return []

        if current.left:
            ans = self._traverse_left_boundry(current.left)
        else:
            ans = self._traverse_left_boundry(current.right)

        ans.append(current.val)
        return ans

    def traverse_left_boundry(self):
        res = self._traverse_left_boundry(self.root)
        return res[::-1]

# Diameter of a Binary Tree
class Solution:
    def diameterofbinarytree(self,root):
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, current):
        if not current:
            return 0
        
        lheight = self.height(current.left)
        rheight = self.height(current.right)

        self.diameter = max(self.diameter, lheight + rheight)

        return 1 + max(lheight, rheight)

def test1():
    tree = Binarytree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    assert tree.traverse_left_boundry() == [1, 2, 4, 7]

def test2():
    tree = Binarytree(1)

    tree.add([2, 4, 5, 6, 7, 9, 11], ['L', 'L', 'R', 'R', 'L', 'L', 'R'])
    tree.add([2, 4, 5, 6, 8], ['L', 'L', 'R', 'R', 'R'])
    tree.add([2, 4, 5, 6, 7, 10], ['L', 'L', 'R', 'R', 'L', 'R'])
    tree.add([3], ['R'])

    assert tree.traverse_left_boundry() == [1, 2, 4, 5, 6, 7, 9, 11]

if __name__ == '__main__':
    tree = Binarytree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    sol = Solution()
    assert sol.diameterofbinarytree(tree.root) == 6

    assert tree.inorder_iterative() == [7,4,8,2,5,9,1,3,10,6]

    test1()
    test2()

#Expression Tree Inorder Traversal      
class BinaryTree():
    def __init__(self, postfix):
        nodes_stk = []

        for char in postfix:
            node = Node(char)

            if not char.isdigit():
                node.right = nodes_stk[-1]
                node.left = nodes_stk[-2]
                nodes_stk.pop()
                nodes_stk.pop()

            nodes_stk.append(node)

        assert len(nodes_stk) == 1
        self.root = nodes_stk[0]

    def _is_leaf(self, current):
        return current and not current.left and not current.right
    
    def _print_inorder_expression(self, current):
        if current.left:
            if not self._is_leaf(current.left):
                print("(", end='')

            self._print_inorder_expression(current.left)

            if not self._is_leaf(current.left):
                print(")", end="")

        print(current.val, end='')

        if current.right:
            if not self._is_leaf(current.right):
                print("(", end='')

            self._print_inorder_expression(current.right)

            if not self._is_leaf(current.right):
                print(")", end="")
    
    def print_inorder_expression(self):
        self._print_inorder_expression(self.root)
        print()

if __name__=="__main__":
    tree2 = BinaryTree('23+4*')
    tree2.print_inorder_expression()
    
    tree2 = BinaryTree('51+2/')
    tree2.print_inorder_expression()
        
    tree2 = BinaryTree('534*2^+')
    tree2.print_inorder_expression()
