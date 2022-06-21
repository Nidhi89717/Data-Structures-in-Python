# Manual system stack
# Write a stack based code to simulate the solution
def f(n):
    if n <= 1:
        return 5
    if n%3 == 0:
        return 6 + f(n-1-n%3)
    return 8 + f(n-1-n%2)

def f_stk(n):
    if n <= 1:
        return 5

    class Recursivecall:
        def __init__(self, n, result = 0, is_completed = False):
            self.n = n
            self.result = result
            self.is_completed = is_completed

    stk =[Recursivecall(n)]
    
    while stk:
        n, result, is_completed = stk[-1].n, stk[-1].result, stk[-1].is_completed

        if not is_completed:
            if n<=1:
                stk.append(Recursivecall(n,5,True))
            elif n%3 == 0:
                stk.append(Recursivecall(n-1-n%3, 6, False))
            else:
                stk.append(Recursivecall(n-1-n%2, 8, False))

        else:
            stk.pop()

            if not stk:
                return result

            stk[-1].result += result
            stk[-1].is_completed = True

    return None

if __name__ == '__main__':
    print(f(500), f_stk(500))

    #print(f(100000))     # maximum recursion depth exceeded in comparison
    print(f_stk(100000))

# Score of parenthesis
# () has score 1
# AB has score A + B
# (A) has score 2*A where A and B are balanced parenthesis strings
class Solution:
    def scoreofparen(self,exp):
        stk = [0]

        for char in exp:
            if char == '(':
                stk.append(0)

            else:
                value = max(2 * stk.pop(), 1)
                stk[-1] += value
        
        return stk.pop()

if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreofparen('()((()))'))

# Daily Temperature
'''Given an array of integers temperatures represents the daily temperatures return an 
array answer such that answer[i] is the number of days you have to wait after the  ith 
day to get a warmer temperature. If there is no future day for which this is possible,
keep answer [i] == 0 instead.'''

class Solution:
    def daily_temp(self,tempt):
        n = len(tempt)
        answer = [0] * n 
        stk = []

        for curr_day, curr_temp in enumerate(tempt):
            while stk and tempt[stk[-1]]<curr_temp:
                prev_day = stk.pop()
                answer[prev_day] = curr_day - prev_day
            stk.append(curr_day)

        return answer
if __name__ == '__main__':
    sol = Solution()
    print(sol.daily_temp([73,74,75,71,69,72,76,73]))
