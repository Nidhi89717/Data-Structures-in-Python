def hash_integer(num, range):
    return num % range

def hash_string1(str, range):
    sum = 0

    for ch in str:
        sum += ord(ch) - ord('a')
    return sum % range

def hash_string2(str,range):
    sum = 0 
    for ch in str:
        idx = ord(ch) - ord('a')
        sum = sum * 26 + idx 
    return sum % range 

if __name__ == '__main__':
    print(hash_integer(100, 1000))      
    print(hash_integer(100, 19))        

    print(hash_string1("abc", 7))       
    print(hash_string1("abcde", 70))    
    print(hash_string1("abcde", 7))     
    print(hash_string1("bcdea", 7))    
    print(hash_string1("abcwz", 7))     

    print(hash_string2("abc", 7))       
    
    print(hash_string2("abcde", 70))    
    print(hash_string2("abcde", 7))     
    print(hash_string2("bcdea", 7))     
    print(hash_string2("abcwz", 7))     
    print(hash(1234))       
    print(hash(15 ** 90))   
    print(hash("abcde"))    
    print(hash("bcdea"))   
    print(hash("bcdea"))    
    print(hash((90, -10, 50)))  
    #print(hash([90, -10, 50]))  # TypeError: unhashable type: 'list'
