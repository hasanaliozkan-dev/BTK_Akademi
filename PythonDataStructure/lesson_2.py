l = list()
for i in range(1,11):
    l.append(i**2)
print(l)
print(i)
print("* "*25)
squares = list(map(lambda x:x**2 ,range(1,11)))
print(squares)
print(range(1,11))
def f (x):
    return x+5

print("* "*25)
print(list(map(f,range(1,7))))
print("* "*25)
print(list(map(lambda x:x+5,range(1,7))))
#print(x) x artık dışarda görünmüyor.
print("* "*25)
squares1 = list(z**2 for z in range(1,11))
print(squares1)
print("* "*25)
l1 = list((x,y) for x in[1,2,3] for y in [3,1,4] if x!=y)
print(l1)
print("* "*25)
l1Lamda = list(map())
