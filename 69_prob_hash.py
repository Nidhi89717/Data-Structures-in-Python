# Number of Distinct Substrings
def count_unique_substrings(str):
    st = set()

    for start in range(len(str)):
        for end in range(start, len(str)):
            substr = str[start : end+1]
            st.add(substr)
    
    return st, len(st)

# Common substrings
def count_substrings_match(str1, str2):
    st1 = count_unique_substrings(str1)[0]
    st2 = count_unique_substrings(str2)[0]

    st = st1.intersection(st2)
    return len(st)

# Unique Anagrams
def count_anagram_substrings(str):  # O(L^3 logL)
    st = set()

    for start in range(len(str)):
        for end in range(start, len(str)):
            substr = tuple(sorted(str[start:end+1]))
            st.add(substr)
    
    return len(st)

def _count_anagram_substrings(str): #O(L^3)
    st = set()

    for start in range(len(str)):
        for end in range(start, len(str)):
            substr = str[start:end+1]
            lst = [0]*26
            for ch in substr:
                lst[ord(ch)-ord('a')] += 1
            st.add(tuple(lst))
    
    return len(st)

# Quadratic Probing
class DictProbing:
    _DELETED_MARK = object()

    def __init__(self, table_size, limit_load_factor = 0.75):
        self.table_size = table_size
        self.table = [None]*table_size
        self.limit_load_factor = limit_load_factor
        self.total_elements = 0

    def _find_idx(self, key):
        hkey = hash(key) % self.table_size
        original_hkey = hkey
        first_available = None 

        for step in range(self.table_size):
            item = self.table[hkey]
            if item is None or item == self._DELETED_MARK:
                if first_available is None:
                    first_available = hkey 
                
                if item is None:
                    break
            
            elif item[0] == key:
                return hkey, True
            
            hkey == (original_hkey + step *step) % self.table_size

            if hkey == original_hkey:
                break

        return first_available, False
    
    def print(self):
        for idx, item in enumerate(self.table):
            print(idx, end=": ")

            if item is None:
                print('E')

            elif item == self._DELETED_MARK:
                print('D')
            else:
                print(item)

    def add(self, key, value):
        assert self.total_elements < self.table_size
        hkey, found = self._find_idx(key)

        if hkey is None:
            self._rehash()
            return self.add(key, value)

        self.table[hkey] = [key, value]

        if not found:
            self.total_elements += 1
            self._rehash()

    def remove(self, key):
        hkey, found = self._find_idx(key)
        if found:
            self.table[hkey] = self._DELETED_MARK
            self.total_elements -= 1
        return found 

    def _rehash(self):
        cur_load_factor = float(self.total_elements) / self.table_size

        if cur_load_factor < self.limit_load_factor:
            return 
        
        print(f'Rehashing - new size will be: {2*self.table_size}')
        
        dct = DictProbing(2*self.table_size, self.limit_load_factor)

        for idx, item in enumerate(self.table):
            if item is None or item == self._DELETED_MARK:
                continue

            else:
                dct.add(item[0], item[1])

        self.table_size = dct.table_size
        self.table = dct.table
        self.total_elements = dct.total_elements


if __name__ == '__main__':
    assert count_unique_substrings("aaab")[1] == 7
    assert count_unique_substrings("aaaaa")[1] == 5
    assert count_unique_substrings("aaaba")[1] == 11
    assert count_unique_substrings("abcdef")[1] == 21

    assert count_substrings_match("aaab", "aa") == 2
    assert count_substrings_match("aaab", "ab") == 3
    assert count_substrings_match("aaaaa", "xy") == 0
    assert count_substrings_match("aaaaa", "aaaaa") == 5

    assert count_anagram_substrings("abba") == 6
    assert count_anagram_substrings("aaaaa") == 5
    assert count_anagram_substrings("abcba") == 9
    assert count_anagram_substrings("aabade") == 17

    assert _count_anagram_substrings("abba") == 6
    assert _count_anagram_substrings("aaaaa") == 5
    assert _count_anagram_substrings("abcba") == 9
    assert _count_anagram_substrings("aabade") == 17

    dct = DictProbing(table_size = 9)
    dct.add('Neha', 1)
    dct.add('Nidhi', 2)
    dct.add('Ada', 5)
    dct.add('Finn', 10)
    dct.add('Arthur', 4)
    dct.add('Zayn', 555) 

    dct.print()

    dct.remove('Finn')
    dct.remove('Ada')
    dct.print()

    dct.add('tommy', 75)
    dct.print()
