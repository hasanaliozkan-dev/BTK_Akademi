def Ebob(n1,n2):
    for i in range(int((n1+n2)/2),0,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i

print(Ebob(12,16))
