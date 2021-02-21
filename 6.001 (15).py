def gcdIter(a,b):
    x=[]
    if a >= b:
        for i in range(1,b):
            if (b % i == 0) and (a % i == 0):
                x.append(i)
    if b > a:
        for i in range(1,a):
            if (b % i == 0) and (a % i == 0):
                x.append(i)
    return x[-1]
gcdIter(6,15)

def odd(x,y):
    a=[]
    for i in range(1, min(x,y)):
        if y % i ==0 and x % i ==0:
            a.append(i)
    return max(a)
odd(6,12)

def gcdRecur(a, b):
    if b == 0:
            return a
    else:
            return gcdRecur(b, a%b)
print(gcdRecur(6,12))
     