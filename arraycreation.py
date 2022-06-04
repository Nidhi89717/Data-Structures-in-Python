import ctypes


class Array:
    def __init__(self, size):
        # FIXED size array from C language
        array_data_type = ctypes.py_object * size
        self.size = size
        self.memory = array_data_type()

        for i in range(size):
            self.memory[i] = None


if __name__ == '__main__':
    array = Array(6)    # fixed array

    for i in range(array.size): # set
        array.memory[i] = i+1

    for i in range(array.size): # get
        print(array.memory[i])

    #del array.memory[0] # NOT support
    del array.memory     # Delete whole array
    # in C++, corresponds to destroying whole array
