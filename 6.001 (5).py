import random
a = random.randint(1,9)

b = 0
while b < 3:
    x = str(input("Find my number in 3 shots: "))
    if  x == ("quit"):
        break
    elif int(x) > a:
        print("so high")
        b +=1
        x
    elif int(x) < a:
        print("Too low")
        b+=1
        x
    elif int(x) == a:
        print("You have found it")
        b+=1
        break
print("try number: ", b)