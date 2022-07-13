import heapq

def test1():
    minheap = []
    lst = [2, 17, 22, 10, 8, 37, 14,
           19, 7, 6, 5, 12, 25, 30]

    for val in lst:
        heapq.heappush(minheap, val)
    print(minheap)

    print()

    for step in range(len(minheap)):
        print(heapq.heappop(minheap), end=', ')

    print()

def test2():
    minheap = [2, 17, 22, 10, 8, 37, 14,
           19, 7, 6, 5, 12, 25, 30]
    
    heapq.heapify(minheap)

    print(minheap)
    print()

    for step in range(len(minheap)):
        print(heapq.heappop(minheap), end=', ')
    print()

def test3():
    lst = [2, 17, 22, 10, 8, 37, 14,
           19, 7, 6, 5, 12, 25, 30]

    k = 3
    print(heapq.nlargest(k, lst))
    print(heapq.nsmallest(k, lst))

    print(lst)

if __name__ == '__main__':
    test1()
    test2()
    test3()
