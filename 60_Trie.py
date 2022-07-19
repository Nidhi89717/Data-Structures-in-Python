class Trie:
    def __init__(self):
        MAX_CHAR = 26
        self.child = [None] * MAX_CHAR
        self.is_leaf = False
    
    def to_idx(self, ch):
        return ord(ch) - ord('a')
    
    def insert(self, str, idx=0):
        if idx == len(str):
            self.is_leaf = True
        else:
            cur = self.to_idx(str[idx])
            if self.child[cur] is None:
                self.child[cur] = Trie()
            self.child[cur].insert(str, idx+1)
        
    def word_exist(self, str, idx=0):
        if idx == len(str):
            return self.is_leaf
        
        cur = self.to_idx(str[idx])
        if self.child[cur] is None:
            return False
        
        return self.child[cur].word_exist(str, idx+1)
    
    def prefix_exist(self, str, idx=0):
        if idx == len(str):
            return True 
        
        cur = self.to_idx(str[idx])
        if self.child[cur] is None:
            return False
        
        return self.child[cur].prefix_exist(str, idx + 1)
    
if __name__ == '__main__':
    root = Trie()

    root.insert("abcd")
    root.insert("xyz")
    root.insert("abf")
    root.insert("xn")
    root.insert("ab")
    root.insert("bcd")

    print(root.word_exist("xyz"))
    print(root.word_exist("xy"))
    print(root.prefix_exist("xy"))
