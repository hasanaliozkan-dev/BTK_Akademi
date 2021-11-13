def fibo1(n):
    a,b = 0,1
    while b<n:
        print(b,end=" ")
        a,b = b, a+b
    print()

def fibo2(n):
    a,b = 0,1
    fibolist = list()
    while b<n:
        fibolist.append(b)
        a,b = b,a+b
    return fibolist

