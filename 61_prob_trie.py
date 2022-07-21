class Trie:
    def __init__(self):
        self.child = [None] * 26 
        self.is_leaf = False
    
    def to_idx(self, ch):
        return ord(ch) - ord('a') 
    
    # Iterative version 
    def insert(self, str):
        node = self 
        
        for ch in str:
            cur = self.to_idx(ch) 
            if node.child[cur] is None:
                node.child[cur] = Trie()
            node = node.child[cur] 
        node.is_leaf = True 
    
    def word_exist(self, str):
        node = self

        for ch in str:
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                return False
            node = node.child[cur]
        
        return node.is_leaf
    
    def prefix_exist(self, str):
        node = self 
        for ch in str:
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                return False 
            node = node.child[cur]
        
        return True 

    # Is suffix
    def _insert(self, str):
        str = reversed(str)

        node = self 

        for ch in str:
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                node.child[cur] = Trie()
            node = node.child[cur] 

        node.is_leaf = True 

    def suffix_exist(self, str):
        str = reversed(str)

        node = self

        for ch in str:
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                return False
            node = node.child[cur]

        return True

    def first_word_prefix(self, str):
        node = self

        for idx, ch in enumerate(str):
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                break 
            
            if node.child[cur].is_leaf:
                return str[:idx+1]
            node = node.child[cur]
        
        return None

if __name__ == '__main__':
    root = Trie()

    root.insert("abcd")
    root.insert("xyz")
    root.insert("xyzwfe")

    print(root.word_exist("xyz"))
    print(root.word_exist("xy"))
    print(root.prefix_exist("xy"))

    root1 = Trie()
    root1._insert("abcd")
    root1._insert("xyz")

    print(root1.suffix_exist("abc"))    
    print(root1.suffix_exist("bcd"))     
    print(root1.suffix_exist("xyz"))    
    print(root1.suffix_exist("xy"))      
    print(root1.suffix_exist("yz"))     
    print(root1.suffix_exist("xyzxyz"))

    print(root.first_word_prefix("xy"))     
    print(root.first_word_prefix("xyz"))    
    print(root.first_word_prefix("xyzw"))   
    print(root.first_word_prefix("xyzH"))   

    root.insert("x")
    print(root.first_word_prefix("xy"))     
    print(root.first_word_prefix("xyz")) 

# OS Paths
class LetterTree:
    def __init__(self):
        self.child = {}
        self.is_leaf = False 
    
    def insert(self, path_lst, idx=0):
        if idx == len(path_lst):
            self.is_leaf = True 
        else:
            cur = path_lst[idx]
            if not cur in self.child:
                self.child[cur] = LetterTree()
            self.child[cur].insert(path_lst, idx+1)
    
    def subpath_exist(self, path_lst, idx=0):
        if idx == len(path_lst):
            return True 
        
        cur = path_lst[idx]
        if not cur in self.child:
            return False 
        
        return self.child[cur].subpath_exist(path_lst, idx+1)

if __name__ == '__main__':


    root = LetterTree()

    root.insert(["home", "software", "eclipse"])
    root.insert(["home", "software", "eclipse", "bin"])
    root.insert(["home", "installed", "gnu"])
    root.insert(["user", "mostafa", "tmp"])

    print(root.subpath_exist(["user", "mostafa", "tmp"]))   
    print(root.subpath_exist(["user", "mostafa"]))          
    print(root.subpath_exist(["user"]))                     
    print(root.subpath_exist(["user", "most"]))             
    print(root.subpath_exist(["user", "NOT"]))     
