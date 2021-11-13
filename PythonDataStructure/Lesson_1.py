from collections import deque

##Stacks(LIFO) and Queue(FIFO)
l = [1,2,3]
l.append(55)

print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print("*"*25)
"""
l1 = [1,2,3]
l2 = [4,5,6]
l3 = list(zip(l1,l2))
"""
l1 =deque([11,22,33])
print(l1)
l1.append(44)
print(l1)
print(l1.popleft())
print(l1)
