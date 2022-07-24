# Handling all letters and digits
def hash_string(str):
    sum = 0
    base = 2 * 26 + 10 # lower, upper and 10 digits

    for ch in str:
        # lowers from [0-25], upper [26-51] and digits [52-61]
        if ch.islower():
            idx = ord(ch) -  ord('a')
        elif ch.isupper():
            idx = ord(ch) - ord('A') + 26
        else:
            idx = ord(ch) - ord('0') + 26*2
        sum = sum * base + idx 
    return sum 

# Folding for hashing 
def hash_string_folding(str):
    sum = 0

    for start in range(0, len(str), 4):
        substr = str[start:start+4]
        sum += hash_string(substr)
    return sum

if __name__ == '__main__':
    print(hash_string_folding('01230123012'))

# Rehashing 
class OurDict:
    def __init__(self, table_size, limit_load_factor):
        self.table_size = table_size
        self.table = [None] * table_size
        self.limit_load_factor = limit_load_factor
        self.total_elements = 0

    def add(self, key, value):
        hkey = hash(key) % self.table_size
        new_item = [key, value]

        if self.table[hkey] is None:
            self.table[hkey] = [new_item]
        else:
            items_equal_key = self.table[hkey]
            for item in items_equal_key:
                if item[0] == key:
                    item[1] = value
                    return
            self.table[hkey].append(new_item)
        
        self.total_elements += 1
        self._rehash()
    
    def print(self):
        for key_values in self.table:
            if key_values is None or len(key_values) == 0:
                continue
            
            hkey = hash(key_values[0][0]) % self.table_size
            print(f'Key {hkey} - Pairs {key_values}')

    def _rehash(self):
        cur_load_factor = float(self.total_elements)/ self.table_size

        if cur_load_factor < self.limit_load_factor:
            return 

        print(f'Rehashing - new size will be:{2*self.table_size}')
        dct = OurDict(2*self.table_size, self.limit_load_factor)

        for key_values in self.table:
            if key_values is None or len(key_values) == 0:
                continue

            for item in key_values:
                dct.add(item[0], item[1])

        self.table_size = dct.table_size
        self.table = dct.table
        self.total_elements = dct.total_elements 

if __name__ == '__main__':
    dct = OurDict(10, 0.5)

    dct.add('Nidhi', 1)
    dct.add('Neha', 2)
    dct.add('Ana', 3)
    dct.add('Ada', 4)
    dct.add('Monica', 5)
    dct.add('Erlich', 6)
    dct.add('Jared', 7)
    dct.add('Dinesh', 8)
    dct.add('Tommy', 9)
    dct.add('Arthur', 10)
    dct.add('John', 11)
