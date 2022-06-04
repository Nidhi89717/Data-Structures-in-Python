# sum upto n nos
'''n= int(input("enter the value for n"))
def sum1(n):
    if n ==0:
        return 0
    else:
        return n + sum1(n-1)
print(sum1(n))'''

#sum of  [1, 2, [3,4], [5,6]]?
p = [1, 2, [3,4], [5,6]]
def sumo(p):
  tot = 0
  for i in p:
    if type(i) == type([]):
      tot =  tot + sumo(i) 
    else:
      tot =  tot + i
  return tot
print(sumo(p))
