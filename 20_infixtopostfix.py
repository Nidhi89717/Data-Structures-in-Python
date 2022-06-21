def infixtopostfix(infix):
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        return 2

    for char in infix:
        if char.isdigit():
            postfix += char

        else:
            while operators and precedence(operators[-1]) >= precedence(char):
                postfix += operators[-1]
                operators.pop()
            operators.append(char)

    postfix += ''.join(reversed(operators))
    return postfix


#                       OR

def Infixtopostfix(infix):
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    infix += '-'
    operators.append('#')

    for char in infix:
        if char.isdigit():
            postfix += char
        else:
            while precedence(operators[-1]) >= precedence(char):
                postfix += operators[-1]
                operators.pop()
            operators.append(char)
    
    return postfix


# Paranthesis
def infixtopostfix_paraen(infix):
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0
    
    infix += '-'
    operators.append('#')

    for char in infix:
        if char.isdigit():
            postfix += char
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                postfix += operators[-1]
                operators.pop()
            operators.pop()  # pop '('
        else:
            while precedence(operators[-1]) >= precedence(char):
                postfix += operators[-1]
                operators.pop()
            operators.append(char)

    return postfix

if __name__ == '__main__':
    print(infixtopostfix('1+2+3'))	
    print(infixtopostfix('1+2*3')) 
    print(infixtopostfix('2*3+4')) 
    print(infixtopostfix('1+3*5-8/2'))  
    print(infixtopostfix('2+3*4-5*6+7'))

    print()
    print(Infixtopostfix('1+2+3'))	
    print(Infixtopostfix('1+2*3')) 
    print(Infixtopostfix('2*3+4')) 
    print(Infixtopostfix('1+3*5-8/2'))  
    print(Infixtopostfix('2+3*4-5*6+7'))
    print()

    print(infixtopostfix_paraen('1+2+3'))	
    print(infixtopostfix_paraen('1+2*3')) 
    print(infixtopostfix_paraen('2*3+4')) 
    print(infixtopostfix_paraen('1+3*5-8/2'))  
    print(infixtopostfix_paraen('2+3*4-5*6+7'))
    
    print(infixtopostfix_paraen('2+(3*4)'))
    print(infixtopostfix_paraen('2+(3*(4-5*2)*(9/3+6))'))
