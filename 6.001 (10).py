
def fibo(s):
    f = [1,1]
    for i in range(s-2):
        f.append(f[-1]+f[-2])
    return f
fibo(7)
