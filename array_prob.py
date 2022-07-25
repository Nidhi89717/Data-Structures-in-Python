import ctypes

class Array:
    def __init__(self, size, initial_value = None):
        self.size = size 
        self._capacity = max(16, 2*size)

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = initial_value

    def expand_capacity(self):
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):
            new_memory[i] = self.memory[i]

        del self.memory
        self.memory = new_memory 

    def append(self, item):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = item
        self.size += 1 
    
    def insert(self, idx, item):
        if idx >= self.size:
            self.append(item)
            return 
        if idx < -self.size:
            idx = -self.size
        
        if idx < 0:
            idx += self.size 

        if self.size == self._capacity:
            self.expand_capacity()

        for p in range(self.size - 1, idx - 1, -1):
            self.memory[p + 1 ] = self.memory[p]
        self.memory[idx] = item
        self.size += 1

    # Right rotation
    def right_rotate(self):
        if self.size == 0:
            return 

        last_element = self.memory[self.size - 1]
        for idx in range(self.size - 2, -1, -1):
            self.memory[idx + 1] = self.memory[idx]
        self.memory[0] = last_element   

    # Left rotation
    def left_rotate(self):
        if self.size == 0:
            return

        first_element = self.memory[0]
        for idx in range(1, self.size):
            self.memory[idx - 1] = self.memory[idx]
        self.memory[self.size - 1] = first_element
    
    # Right rotation with steps
    def right_rotate_steps(self, times):
        times %= self.size
        for steps in range(times):
            self.right_rotate()

    def pop(self, idx):
        assert idx >= -self.size and idx < self.size, 'pop index is out of range'

        if idx < 0:
            idx += self.size
        
        val = self.memory[idx]

        for p in range(idx + 1, self.size):
            self.memory[p-1] = self.memory[p]
        
        self.size -= 1
        return val 
    
    # Index transposition 
    def index_transposition(self, value):
        for idx in range(self.size):
            if self.memory[idx] == value:
                if idx == 0:
                    return 0 
                self.memory[idx], self.memory[idx - 1] = self.memory[idx - 1], self.memory[idx]
                return idx - 1
            return -1 
 
    def __getitem__(self, idx):
        return self.memory[idx]

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result

# 2D Array
class Array2D:
    def __init__(self, rows, cols, initial_value=None):
        self.rows, self.cols = rows, cols 

        self.grid = Array(rows)
        for i in range(rows):
            self.grid[i] = Array(cols, initial_value)

    def __getitem__(self, index):
        r, c = index[0], index[1]
        return self.grid[r][c]

    def __setitem__(self, index, value):
        r,c = index[0], index[1]
        self.grid[r][c] = value 

    def __repr__(self):
        result = ''
        for i in range(self.rows):
            result += str(self.grid[i]) + '\n'
        return result

def test_insert():
    array = Array(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    
    array.insert(-1, -10)
    print(array)  

    array.insert(-2, -20)
    print(array)  

    array.insert(-3, -30)
    print(array)  

    array.insert(-4, -40)
    print(array)  

    array.insert(-5, -50)
    print(array)  

    array.insert(8, 80)
    print(array)  

    array.insert(20, 90)
    print(array) 
    print()

def test_right_rotate():
    array = Array(0)

    array.right_rotate()
    print(array)

    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)

    array.right_rotate()
    print(array)
    array.right_rotate()
    print(array)
    print()

def test_left_rotate():
    array = Array(0)

    array.right_rotate()
    print(array)

    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)

    array.left_rotate()
    print(array)

    array.left_rotate()
    print(array)    
    print()

def test_right_rotate_steps():
    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    print(array)

    array.right_rotate_steps(3)
    print(array)

    array.right_rotate_steps(7)
    print(array)

    array.right_rotate_steps(123456789)
    print(array)
    print()

def test_pop():
    array = Array(0)
    array.append(10)
    array.append(20)
    array.append(30)
    array.append(40)
    print(array)
  
    print(array.pop(0))  
    print(array)
    
    print(array.pop(2))  
    print(array)
 
    array.append(60)
    array.append(70)
    array.append(80)
    print(array)

    print(array.pop(-1))  
    print(array)

    print(array.pop(-4))  
    print(array)
    print()

if __name__ == '__main__':
    test_insert()
    test_right_rotate()
    test_left_rotate()
    test_right_rotate_steps()
    test_pop()

    arr2d = Array2D(2,4,0)
    arr2d[(0, 2)] = 3
    arr2d[(1, 1)] = 5
    arr2d[(1, 3)] = 7
    print(arr2d)
    print(arr2d[(1, 3)])
