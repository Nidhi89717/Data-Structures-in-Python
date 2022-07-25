class OurDictPropbing:
    _DELETED_MARK = object()

    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size 
        self.total_elements = 0

    def _find_idx(self, key):
        hkey = hash(key) % self.table_size
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
            
            hkey = (hkey + 1) % self.table_size
        
        return first_available, False

    def print(self):
        for idx, item in enumerate(self.table):
            print(idx, end=': ')

            if item is None:
                print('E')
            elif item == self._DELETED_MARK:
                print('D')
            else:
                print(item)

    def add(self, key, value):
        assert self.total_elements < self.table_size, 'Table is Full'
        hkey, found = self._find_idx(key)
        self.table[hkey] = [key, value]
        self.total_elements += not found 
    
    def get(self, key):
        hkey, found = self._find_idx(key)
        assert found, f'No such item {key}'
        return self.table[hkey][1]

    def exist(self, key):
        hkey, found = self._find_idx(key)
        return found 
    
    def remove(self, key):
        hkey, found = self._find_idx(key)
        if found:
            self.table[hkey] = self._DELETED_MARK
            self.total_elements -= 1
        return found 

if __name__ == '__main__':

    dct = OurDictPropbing(table_size=9)

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
