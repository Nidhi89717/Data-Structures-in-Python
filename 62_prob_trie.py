class Trie:
    def __init__(self):
        self.child = [None]*26
        self._child = {}
        self.is_leaf = False

    def to_idx(self, ch):
        return ord(ch) - ord('a')

    def insert(self, str):
        node = self

        for ch in str:
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                node.child[cur] = Trie()
            node = node.child[cur]
        node.is_leaf = True

    def _insert(self, str):
        node = self

        for cur in str:
            if cur not in node._child:
                node._child[cur] = Trie()
            node = node._child[cur]
        node.is_leaf = True 
    
    def word_exist(self, str):
        node = self

        for cur in str:
            if cur not in node._child:
                return False
            node = node._child[cur]

        return node.is_leaf

    # Listing tree content
    def get_all_strings(self):
        ans = []

        def traverse(trie, cur_str):
            if trie.is_leaf:
                ans.append(cur_str)
            
            for idx, node in enumerate(trie.child):
                if node is None:
                    continue
                letter = chr(ord('a') + idx)
                traverse(node, cur_str + letter)
            
        traverse(self, '')
        return ans

    # Autocomplete
    def _get_all_strings(self, node,cur_str):
        ans = []

        def traverse(trie, cur_str):
            if trie.is_leaf:
                ans.append(cur_str)

            for idx, node in enumerate(trie.child):
                if node is None:
                    continue
                letter = chr(ord('a') + idx)
                traverse(node, cur_str + letter)

        traverse(node, cur_str)
        return ans  

    def autocomplete(self, str):
        node = self

        for ch in str:
            cur = self.to_idx(ch)
            if node.child[cur] is None:
                return []
            node = node.child[cur]
        
        return self._get_all_strings(node, str)
    
    def _word_exist_changes(self, str, allowed_changes=1, idx=0):
        if idx == len(str):
            return allowed_changes == 0 and self.is_leaf

        if str[idx] in self._child:
            if self._child[str[idx]]._word_exist_changes(str, allowed_changes, idx+1):
                return True

        if allowed_changes == 0:
            return False

        for letter in self._child:
            if letter != str[idx]:
                if self._child[letter]._word_exist_changes(str, allowed_changes-1, idx+1):
                    return True
            
        return False

class MagicDictionary(object):
    def __init__(self):
        self.root = Trie()

    def builddict(self, dictionary):
        for word in dictionary:
            self.root._insert(word)
    
    def search(self, searchWord):
        searchWord = list(searchWord)

        for idx, cur_letter in enumerate(searchWord):
            cpy_letter = cur_letter

            for char_idx in range(26):
                new_letter = chr(ord('a') + char_idx)

                if cpy_letter == new_letter:
                    continue
                
                searchWord[idx] = new_letter
                if self.root.word_exist(searchWord):
                    return True
            
            searchWord[idx] = cpy_letter

        return False
    # Other approach 
    def _search(self, searchWord):
        return self.root._word_exist_changes(searchWord, 1)

if __name__ == '__main__':

    root = Trie()

    root.insert("xyz")
    root.insert("abcd")
    root.insert("abf")
    root.insert("ab")
    root.insert("xyzwfe")

    print(root.get_all_strings()) 

    print(root.autocomplete('a'))
  
    print(root.autocomplete('xy'))

    dct = MagicDictionary()
    dct.builddict(["afgc", "axgh"])

    print(dct.search('afgh'))
    print(dct._search('afgh'))
