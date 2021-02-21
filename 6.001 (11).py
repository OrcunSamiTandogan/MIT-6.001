x = 27
high = x
low = 0.0
epsilon = 0.0001
ans = (high+low)/2.0
count = 0
while (abs(ans**3 - x)) >= epsilon:
    count +=1
    if ans**3 > x:
        high = ans
    else:
        low = ans
    ans = (high+low)/2.0
print(str(ans))
print(count)