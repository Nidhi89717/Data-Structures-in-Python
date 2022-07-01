class Node:
    def __init__(self, val = None, left = None, right=None):
        self.val = val
        self.right = right
        self.left = left
    
class Binarytree:
    def __init__(self,value):
        self.root = Node(value)

    def add(self,values_lst,direction_lst):
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

    def tree_height(self,current):
        if not current:
            return -1
        
        return 1 + max(self.tree_height(current.left), self.tree_height(current.right))
    
    # Recursive level order traversal
    def print_nodes_level(self,current,level):
        if not current:
            return
        
        if level == 0:
            print(current.val, end=' ')
        elif level:
            self.print_nodes_level(current.left, level-1)
            self.print_nodes_level(current.right, level-1)
        
    def level_order_traversal_recursive(self):
        h = self.tree_height(self.root)

        for level in range(h+1):
            print(f"\nLevel{level}:", end="")
            self.print_nodes_level(self.root, level)

class Solution:
    #Binary Tree Zigzag Level Order Traversal
    def zigzaglevelorder(self, root):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(root)
        level, forward_level = 0, True
        ans = []

        while nodes_queue:
            row = []
            sz = len(nodes_queue)

            for step in range(sz):
                if forward_level:
                    cur = nodes_queue.popleft()
                    row.append(cur.val) 

                    if cur.left:
                        nodes_queue.append(cur.left)
                    if cur.right:
                        nodes_queue.append(cur.right)

                else:
                    cur = nodes_queue.pop()
                    row.append(cur.val)

                    if cur.right:
                        nodes_queue.appendleft(cur.right)
                    if cur.left:
                        nodes_queue.appendleft(cur.left)
            
            level, forward_level = level+1, not forward_level
            ans.append(row)
        
        return ans
    
    #Check Completeness of a Binary Tree
    def iscompletetree(self,root):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(root)

        no_more_allowed = False

        while nodes_queue:
            for step in range(len(nodes_queue)):
                cur = nodes_queue.popleft()

                if cur.left:
                    if no_more_allowed:
                        return False
                    nodes_queue.append(cur.left)
                else:
                    no_more_allowed = True

                if cur.right:
                    if no_more_allowed:
                        return False
                    nodes_queue.append(cur.right)
                else:
                    no_more_allowed = True
        return True

if __name__ == "__main__":
    tree = Binarytree(1)
    tree.add([2, 4, 8], ['L', 'L', 'L'])
    tree.add([2, 4, 9], ['L', 'L', 'R'])
    tree.add([2, 5, 10], ['L', 'R', 'L'])
    tree.add([2, 5, 11], ['L', 'R', 'R'])

    tree.add([3, 6, 12], ['R', 'L', 'L'])
    tree.add([3, 6, 13], ['R', 'L', 'R'])
    tree.add([3, 7, 14], ['R', 'R', 'L'])
    tree.add([3, 7, 15], ['R', 'R', 'R'])

    tree.level_order_traversal_recursive()
    print()

    print(Solution().zigzaglevelorder(tree.root))

    print(Solution().iscompletetree(tree.root))
