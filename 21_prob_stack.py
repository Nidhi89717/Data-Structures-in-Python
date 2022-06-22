# Extend code to include individual lowercase and uppercase
def infixToPostfix(infix):
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    infix += '-'		    
    operators.append('#')  

    for char in infix:
        if char.isdigit() or char.islower() or char.isupper():
            postfix += char
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                postfix += operators[-1]
                operators.pop()
            operators.pop() # pop (
        else:
            while precedence(operators[-1]) >  precedence(char) or \
                  precedence(operators[-1]) == precedence(char) and char != '^':
                postfix += operators[-1]
                operators.pop()
            operators.append(char)

    return postfix


if __name__ == '__main__':
    
    print(infixToPostfix('1+2^3^4*5-6'))
    print(infixToPostfix('(1+2)^3^(4*5-6)^2+1'))
    print()

# Postfix evaluation 
def operation(a,b,oper):
    if oper == '+':
        return a+b
    if oper == '-':
        return a-b
    if oper == '/':
        return a/b
    if oper == '*':
        return a*b
    return a**b

def evaluate_postfix(postfix):
    num = []
    for char in postfix:
        if char.isdigit():
            num.append(float(char))
        else:
            a,b = num[-1],num[-2]
            num.pop()
            num.pop()
            num.append(operation(b,a,char))
    
    return num[-1]

if __name__ == '__main__':
    print(evaluate_postfix('52/'))
    print(evaluate_postfix('12+3+'))
    print(evaluate_postfix('5432^^+9-'))
    print(evaluate_postfix('23452*-*93/6+*+'))
    print()

# Implement an infix to prefix program
def infixtopostfix(infix):
    def reversedinfixtopostifix(infix):
        operators = []
        postfix = ''

        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            if op == '^':
                return 3
            return 0

        for char in infix:
            if char.isdigit() or char.islower() or char.isupper():
                postfix += char
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators[-1] != '(':
                    postfix += operators[-1]
                    operators.pop()
                operators.pop()
            else:
                while operators and (precedence(operators[-1]) > precedence(char) or
                      precedence(operators[-1]) == precedence(char) and char == '^'):
                    postfix += operators[-1]
                    operators.pop()
                operators.append(char)

        postfix += ''.join(reversed(operators))
        return postfix

    reversed_infix = infix[::-1].replace('(', '$').replace(')', '(').replace('$', ')')
    reversed_postfix = reversedinfixtopostifix(reversed_infix)
    return reversed_postfix[::-1]

if __name__ == '__main__':
    print(infixtopostfix('1+2'))
    print(infixtopostfix('9-2+3'))
    print(infixtopostfix('2^3^4^5^6'))
    print(infixtopostfix('(1+2)^3^(4-6)^2+1'))
    print(infixtopostfix('a+(c^d-e)^(f+g*h)-i'))
    print(infixtopostfix('a+B-c'))
    print(infixtopostfix('2+(3*(4-5)*(9/3+6))'))
    print(infixtopostfix('1+3-8/2'))
    print()

# Given an expression containing single digit numerals, 
#and the characters + - ( ), remove all brackets from the expression, and 
#simplify it: 
def removebrackets(str):
    def sign(a,b):
        if a==b:
            return '+'
        return '-'
    
    stk= ['+']
    res = ''

    for idx, c in enumerate(str):
        if c.isdigit():
            res += c
        elif c == '+' or c == '-':
            res += sign(stk[-1], c)
        elif c == '(' and stk:
            if str[idx-1] != '(':
                stk.append(sign(stk[-1], str[idx - 1]))
            else:
                stk.append(stk[-1])
        else:
            stk.pop()
        
    return res

if __name__=='__main__':
    print(removebrackets('1+2-3-4+5-6-7+8'))
    print(removebrackets('1-(2-3+((4-5)-(6-7)))'))
    print(removebrackets('1-(2-3-((4-5)-(6-7)))'))
    print(removebrackets('1-(((4-5)-(6-7))))'))
    print(removebrackets('1-((4+5)-(6-7)))')) 
