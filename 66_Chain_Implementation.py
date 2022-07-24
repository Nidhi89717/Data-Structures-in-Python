class OurDict:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size
    
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
    
    def print(self):
        for key_values in self.table:
            if key_values is None or len(key_values) == 0:
                continue
            
            hkey = hash(key_values[0][0]) % self.table_size
            print(f'key {hkey} - Pairs {key_values}')
    
    def get(self, key):
        hkey = hash(key) % self.table_size 
        assert self.table[hkey] is not None, f'No such item{key}'

        items_equal_key = self.table[hkey]
        for item in items_equal_key:
            if item[0] == key:
                return item[1]
        
        assert  False, f'No value attached with item{key}'
    
    def exists(self, key):
        hkey = hash(key) % self.table_size

        if self.table[hkey] is None:
            return False 
        
        items_equal_key = self.table[hkey]
        for idx, item in enumerate(items_equal_key):
            if item[0] == key:
                return True
        
        return False 

    def remove(self, key):
        hkey = hash(key) % self.table_size

        if self.table[hkey] is None:
            return False 
        
        items_equal_key = self.table[hkey]
        for idx, item in enumerate(items_equal_key):
            if item[0] == key:
                items_equal_key.pop(idx) 
                return True 
            
        return False

if __name__ == '__main__':
    dct = OurDict(table_size=5)

    dct.add('Jared', 1)   
    dct.add('John', 2)      
    dct.add('Ana', 5)       
    dct.add('Amal', 6)      
    dct.add('Hany', 8)      
    dct.add('Tommy', 10)    
    dct.add('Ada', 11)    
    dct.add('Michel', 3)      
    dct.add('Richi', 4)    

    dct.add('John', 555)    

    dct.print()

    print(dct.exists('John'))  
    print(dct.exists('Finn')) 

    print(dct.get('Amal'))  
    print(dct.get('John'))  
    #print(dct.get('Finn'))  # AssertionError

    print(dct.remove('John'))   
    print(dct.remove('John'))   
    print(dct.remove('Finn'))   
