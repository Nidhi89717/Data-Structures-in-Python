# #Find all substrings 
class Trie:
    def __init__(self):
        MAX_CHAR = 26
        self.child = [None] * MAX_CHAR
        self.is_leaf = False
    
    def to_idx(self, ch):
        return ord(ch) - ord('a')
    
    def insert(self, str, idx = 0):
        if idx == len(str):
            self.is_leaf = True
        
        else:
            cur = self.to_idx(str[idx])
            if self.child[cur] is None:
                self.child[cur] = Trie()
            self.child[cur].insert(str, idx+1)
    
    def prefix_exist(self, str, idx=0):
        if idx == len(str):
            return True
        
        cur = self.to_idx(str[idx])
        if self.child[cur] is None:
            return False 

        return self.child[cur].prefix_exist(str, idx+1)

    def get_all_matches(self, str, start_idx):
        node = self
        steps = 0
        ans = []
        for idx in range(start_idx, len(str)):
            steps += 1
            cur = self.to_idx(str[idx])
            if node.child[cur] is None:
                break
            node = node.child[cur]
            if node.is_leaf:
                ans.append(str[start_idx : start_idx + steps])
        return ans 

def list_substrs(long_str, queries_lst):
    trie = Trie()

    for idx in range(len(long_str)):
        suffix = long_str[idx:]
        trie.insert(suffix)

    ans = []
    for word in queries_lst:
        if trie.prefix_exist(word):
            ans.append(word)
    
    return ans
# Alternate
def _list_substrs(long_str, queries_lst):
    trie = Trie()

    for word in queries_lst:
        trie.insert(word)
    
    ans =[]

    for idx in range(len(long_str)):
        sub_list = trie.get_all_matches(long_str, idx)
        ans.extend(sub_list)
    
    return ans

if __name__ == '__main__':
    long_str = 'heyabcdtwxyw'
    queries_lst = ["xy", "ab", "t", "yz"]
    ans = _list_substrs(long_str, queries_lst)
    print(ans)

    ans = list_substrs(long_str, queries_lst)
    print(ans)
