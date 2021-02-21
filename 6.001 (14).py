import random
import string

a = 0
b = str()
a1 = int(input("how many letter should be in password?: "))
while a < a1:
    x = random.randint(0,3)
    if x == 0:
        y = random.randint(1,9)
        b = b + str(y)
        a += 1
    if x == 1:
        z = string.ascii_letters
        k = random.choice(z)
        b = b + str(k)
        a += 1
    if x == 2:
        l = string.punctuation
        m = random.choice(l)
        b = b + str(m)
        a += 1
print(b)