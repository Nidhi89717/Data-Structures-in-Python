# Reverse an integer using stack
def reverse_num(num):
    if num == 0:
        return 0

    stk = []
    while num:
        stk.append(num % 10)
        num //= 10

    tens = 1
    while stk:
        num = stk[-1]*tens + num
        tens *= 10
        stk.pop()

    return num

print(reverse_num(62345))
print(reverse_num(1234000))

class Soln:
    ## Valid parentheses
    def valid_paren(self,str):
        dict = {')':'(', '}':'{', ']':'['}
        stk = []

        for char in str:
            if char not in dict:
                stk.append(char)
            elif not stk or dict[char] != stk.pop():
                return False
        
        return not stk

    #Remove All Adjacent Duplicates In String
    def remove_duplicates(self,str):
        stk = []
        for char in str:
            if stk and char == stk[-1]:
                stk.pop()
            else:
                stk.append(char)

        return ''.join(stk) 
    
    # asteriod collision
    def asteriod_collision(self,asteriod):
        results = []
        for ast in asteriod:
            while results and ast < 0 < results[-1]:
                if results[-1] < -ast:
                    results.pop()
                    continue
                elif results[-1] == -ast:
                    results.pop
                break
            else:
                results.append(ast)
        return results
             
    
if __name__ == '__main__':
    sol = Soln()
    result = sol.valid_paren('{([)}[]')
    print(result)
    result = sol.valid_paren('{()}[{}]')
    print(result)

    print(sol.remove_duplicates('abbbca'))
    print(sol.remove_duplicates('abba'))

    print(sol.asteriod_collision([10,2,-5,-20]))
    print(sol.asteriod_collision([-10, 5, 10]))
