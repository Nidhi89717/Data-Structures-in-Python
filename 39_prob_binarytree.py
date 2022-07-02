class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
    
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

class Solution(object):
    # Symmetric Tree
    # recursive approach
    def isSymmetric(self, root):
        def is_mirror(first, second):
            if not first and not second:
                return True
            
            if first and not second or not first and second:
                return False
            
            if first.val != second.val:
                return False

            return is_mirror(first.left, second.right) and is_mirror(first.right, second.left)
        
        return is_mirror(root.left, root.right)

    #  parenthesizing 
    def is_symmetric(self, root):
        def parenthesize(current, left_first):
            if not current:
                return ''
            
            repr = '(' + str(current.val)

            if current.left:
                lrepr = parenthesize(current.left, left_first)
            else:
                lrepr = '()'

            if current.right:
                rrepr = parenthesize(current.right, left_first)
            else:
                rrepr = '()'

            if left_first:
                repr += lrepr + rrepr + ')'
            else:
                repr += rrepr + lrepr + ')'

            return repr
        
        left = parenthesize(root.left, True)
        right = parenthesize(root.right, False)

        return left == right

    # Flip Equivalent Binary Trees
    def flip_equiv(self, root1, root2):
        def is_equiv(current):
            if not current:
                return ''

            repr = '(' + str(current.val)

            if current.left:
                lrepr = is_equiv(current.left)
            else:
                lrepr = '()'

            if current.right:
                rrepr = is_equiv(current.right)
            else:
                rrepr = '()'
            
            if lrepr < rrepr:
                repr += lrepr + rrepr + ')'
            else:
                repr += rrepr + lrepr + ')'

            return repr

        first = is_equiv(root1)
        second = is_equiv(root2)

        return first == second

# Print all duplicate subtrees 
    def print_duplicate_subtrees(self,root):
        def parenthesize(current):
            if not current:
                return ''
            
            if current.left:
                lrepr = parenthesize(current.left)
            else:
                lrepr = '()'

            if current.right:
                rrepr = parenthesize(current.right)
            else:
                rrepr = '()' 

            repr = '(' + str(current.val) + lrepr + rrepr + ')'

            if current.left or current.right:
                if repr in dct:
                    dct[repr] += 1
                else:
                    dct[repr] = 1
            
            return repr
        
        dct = {}
        parenthesize(root)
        lst = [item for item in dct.keys() if dct[item] > 1]
        print(lst)

if __name__ == '__main__':
    tree = Binarytree(1)
    tree.add([12, 4, 7], ['L', 'L', 'L'])
    tree.add([12, 4, 8], ['L', 'L', 'R'])
    tree.add([12, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    tree2 = Binarytree(1)
    tree2.add([2,3],['L','L'])
    tree2.add([2,4],['L','R'])
    tree2.add([2,3],['R','R'])
    tree2.add([2,4],['R','L'])

    sol = Solution()
    print(sol.isSymmetric(tree.root))
    print(sol.isSymmetric(tree2.root))

    print(sol.is_symmetric(tree.root))
    print(sol.is_symmetric(tree2.root))

    tree3 = Binarytree(1)
    tree3.add([2,4],['L','L'])
    tree3.add([2,5],['L','R'])    
    tree3.add([3,6],['R','L'])

    tree4 = Binarytree(1)
    tree4.add([3,6],['L','R'])
    tree4.add([2,5],['R','R'])
    tree4.add([2,4],['R','L'])

    print(sol.flip_equiv(tree3.root, tree4.root))

    tree5 = Binarytree(1)
    
    tree5.add([2,3],['L','L'])
    tree5.add([2,4],['L','R'])
    tree5.add([5,2,3],['R','L','L'])
    tree5.add([5,2,4],['R','L','R'])
    sol.print_duplicate_subtrees(tree5.root)
