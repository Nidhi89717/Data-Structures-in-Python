#append functon in list 
# using capacity trick
import ctypes


class Array:
    def __init__(self, size):
        self.size = size                    # user size
        self._capacity = max(16, 2*size)    # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def expand_capacity(self):
        # Double the actual array size
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        # create a new array of _capacity
        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):  # copy
            new_memory[i] = self.memory[i]

        # use the new memory and delete old one
        del self.memory
        self.memory = new_memory

    def append(self, value):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = value
        self.size += 1

    def __len__(self):
        return self.size


if __name__ == '__main__':

    array = Array(3)

    for i in range(len(array)):
        array[i] = i + 1

    array.append('12')
    array.append('hello')

    print(array)

    for i in range(10 ** 6):
        array.append(i)

    print(len(array))
    # Very fast!
