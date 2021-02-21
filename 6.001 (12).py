import random
print("please think number btw 0,100")
l = 0
h = 100
y = random.randint(l,h)
count = 0
x = str()
while x != "y":
    print("If your number higher than this, put h ; if lower than this, put l, if this is your number, put y: ", y)
    x = input(str("...: "))
    if x == "y":
        print("I found it")
        count += 1
        break
    elif x == "h":
        h = y
        y = random.randint(l,h)
        count += 1
    elif x == "l":
        l = y
        y = random.randint(l,h)
        count += 1
    else:
        print("wtf")
print(count)
# mesela ayni sayilari tekrar tekrar sorabiliyor, bunu yapmamali