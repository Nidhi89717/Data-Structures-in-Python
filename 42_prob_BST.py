class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    process(current.left, val)
            
            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    process(current.right, val)
            
        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)
            
    def height(self):
        def process(current):
            if not current:
                return -1

            return 1+ max(process(current.left),process(current.right))
        return process(self.root)

    # Search in a Binary Search Tree - iterative
    # Solution 1
    def b_search(self, val):
        l = self.height() + 1
        current = self.root
        for i in range(l):
            if not current:
                return False
            if val == current.val:
                return True
            
            if val > current.val:
                current = current.right
            else:
                current = current.left
            
            l += 1
    
class Solution(object):
    # Search in BST Solution 2
    def searchBST(self, current, val):
        while current:
            if val == current.val:
                return True
            if val < current.val:
                current = current.left
            else:
                current = current.right

        return None   

    def inorder(self, current):
        def process(current):
            if not current:
                return
            process(current.left)
            lst.append(current.val)
            process(current.right)
        
        lst = []
        process(current)
        return lst

    # Validate Binary Search Tree
        # Method 1
    def is_validBst(self, current):
        lst = self.inorder(current)
        for i in range(1, len(lst)):
            if lst[i - 1] >= lst[i]:
                return False
        return True
        
        # Method 2
    def isValidBST(self,current,mn=float('-inf'), mx=float('inf')):
        if not current:
            return True

        val, left, right = current.val, current.left, current.right

        if not(mn < val < mx ):
            return False

        return self.isValidBST(left, mn, val) and self.isValidBST(right, val, mx)

    def sotrtedarraytoBST(self, nums):
        def process(nums):
            if len(nums) == 0:
                return None

            mid = len(nums) // 2
            root = Node(nums[mid])
            root.left = process(nums[:mid])
            root.right = process(nums[mid+1:])
            return root

        return process(nums)
    
    # Kth Smallest Element in a BST
    def kthsmallest(self,root,k):
        def inorder(root, k):
            if k<0:
                return -1

            if not root:
                return k

            k = inorder(root.left, k)

            if k==1:
                self.answer = root.val
                return 0

            k = inorder(root.right, k-1)
            return k

        self.answer = None
        inorder(root,k)
        return self.answer

    # Lowest Common Ancestor of a Binary Search Tree
    def lca(self,root,p,q):
        if p < root.val and q < root.val:
            return self.lca(root.left,p,q)
        
        if p > root.val and q > root.val:
            return self.lca(root.right,p,q)

        return root.val

if __name__ == '__main__':
    tree = Binarytree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])
    sol = Solution()

    print(tree.height())

    print(tree.b_search(50))
    print(tree.b_search(35))
    print(tree.b_search(90))

    print(sol.searchBST(tree.root, 35))

    print(sol.is_validBst(tree.root))
    print(sol.isValidBST(tree.root))

    sol.sotrtedarraytoBST([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    tree2 = Binarytree(5)
    tree2.insert([3,6,2,4,1])
    print(sol.kthsmallest(tree2.root, 3))

    tree3 = Binarytree(50)
    tree3.insert([20,60,15,45,58,70,16,35,73,36,75])
    print(sol.lca(tree3.root,45,36))
    print(sol.lca(tree3.root,15,70))
    print(sol.lca(tree3.root,73,75))
