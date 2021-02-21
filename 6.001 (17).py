#x = input("user 1")
#y = input("user 2")
#def play(x,y):
#    if (x == "R" or x == "r"):
#        if y == "R" or y == "r":
#            return print("draw")
#        elif y == "S" or y == "s":
#            return print("user 1 wins")
#        else:
#            return print("user 2 wins")
#    elif x == "S" or x == "s":
#         if  y == "S" or y == "s":
#             return print("draw")
#         elif y == "R" or y == "r":
#             return print("user 2 wins")
#         else:
#             return print("user 1 wins")
#    else:
#        return print("nobody wins")
#
#while input != "quit":
#    play(x,y)
#    z = input("do you wanna play again, y/n?")
#    if z == "y" or z == "Y":
#        x = input("user 1")
#        y = input("user 2")
#    elif z == "N" or z == "n":
#        break
#import random
#a = random.randint(1,10)
#x = int()
#while x != a:
#    x = int(input(("give number")))
#    if x > a:
#        print("pick lower")
#    elif x < a:
#        print("pick higher")
#    else:
#        print("you found it ", x)
##        break
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#for i in a:
#    if i in b:
#        c.append(i)
#for i in b:
#    if i in a and i not in c:
#        c.append(i)
#c.sort()
#print(c)
#x = int(input("give me a prime number"))
#for i in range(2,x):
#    count = 1
#    if x %i == 0:
#        print("it can not be")
#        count = count + 1
#        print(count)
#        break 
#    else:
#        print("it`s prime number")
#        count = count + 1
#        print(count)
#        break
#def ab(x):
#    c=[]
#    c.append(x[0])
#    c.append(x[-1])
#    print(c)
#a = [5, 10, 15, 20, 25]
#ab(a)

#x = int(input("how many fibo number you need?"))
#f = [1,1,2]
#k = f[-1] + f[-2]
#for i in range(len(f),x-1):
#    k = f[-1] + f[-2]
#    f.append(k)
#print(f)
#k = f[-1] + f[-2]
#print(k)
#
#def st(a):
#    b=[]
#    for i in a:
#        if i not in b:
#            b.append(i)
#    print(b)
#x= [1,2,3,4,5,6,6,7,8]
#st(x)
#
#a = 'abcd defg'
#print(a, a[::-1])
#def ar(x):
#    r = x.split()
#    r2 = r[::-1]
#    r3 = ' '.join(r2)
#    print(r, r2, r3)
#ar(a)    
#
#import random
#x = int(input("how many letters password do you need?"))
#a = ['a','s','d','F','T']
#def pas(z):
#    c = []
#    while len(c) < z:
#        c.append(random.choice(a))
#    d = ''.join(c)
#    print(d)
#    d2 = d.split()
#    random.shuffle(d2)
#    print(d2)
#    d2 = ''.join(d2)
#    print(d2)
#pas(x)
#
#import requests
#from bs4 import BeautifulSoup
# 
#base_url = 'https://steamdb.info/sales/'
#r = requests.get(base_url)
#r.status_code #bu 200-400 bir sey cikmali
#r.content #bunda da uzunca bir yazi gelmeli
#
#
#soup = BeautifulSoup(r.content,'lxml') #lxml yerine baska seyler de kullanilabiliyor
# 
#soup.find_all("tr",attrs = {"class":"app appimg odd"})
#
#
#
#varA = a
#varB = b
#if type(a*b)== str:
#    print("strinn involved")
#elif a > b:
#    print("bigger")
#elif a == b:
#    print("equal")
#else:
#    print("smaller")
#
#end = 6
#x = 0
#count = 0
#while count != end:
#    x += count + 1
#    count += 1
#    if count == end:
#        print(x)
#        break
#a = range(0,10,2)
#for i in a:
#    print(i)
#
#print("Hello!")
#a = range(2,12,2)
#b = a[::-1]
#for i in b:
#    print(i)
#end=6
#a = range(end+1)
#x = 0
#for i in a:
#    x += i
#print(x)
#
#for iteration in range(5):
#    count = 0
#    while True:
#        for letter in "hello, world":
#            count += 1
#        print("Iteration " + str(iteration) + "; count is: " + str(count),'a')
#        break
#
#import string
#a = list(string.ascii_lowercase)
#b = len(a)
#c = list(range(1,b+1))
#print(a,b,c)
#res = dict(zip(a,c)) 
#print(res)
#x= 'abcde'
#def find(x):
#    for i in x:
#        if i in res:
#            y.append(res{i})
#find(x)
#    
##    
#s = "azcbobobegghakl"
#longest = s[0]
#current = s[0]
#for c in s[1:]:
#    if c >= current[-1]:
#        current += c
#        print(current)
#        if len(current) > len(longest):
#            longest = current
#    else:
#        current = c
#print ("Longest substring in alphabetical order is:", longest    )
##    
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#        if iteration % 2 == 0:
#            break
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
#    
#
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) < epsilon:
#        break
#    else:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))
#
#a = 0
#b = 100
#import random
#c = random.randint(a,b) 
#ab = (a+b)/2
##print("is this your number, or lower or higher: ", c)
##y = input()
#
#while True:
#    print("is that your number: ", (a+b)/2)
#    x = input("enter h, l or y")
#    if x == "y":
#        print(abs((a+b)/2))
#        break
#    elif x == "l":
#        b = (a+b)/2
#    elif x == "h":
#        a = (a+b)/2
#    else:
#        print("repeat plz")
##    
#x = 5
#if x < 0 :
#    isNeg = True
#    x = abs(x)
#else:
#    isNeg = False
#result = ''
#if x == 0:
#    result = '0'
#while x > 0:
#    result = str(x%2) + result
#    x = x // 2
#if isNeg:
#    result = '-' + result
#print(result)
#
#epsilon = 0.1
#y = 24.0
#guess = y / 2.0
#numGuess= 0
#while abs((guess**2) - y) >= epsilon:
#    numGuess +=1
#    guess = guess - (((guess**2)-y)/(2*guess))
#print("guess number: ", numGuess)
#print(guess)

#def square(x):
#    '''
#    x: int or float.
#    '''
#    # Your code here
#    y = (abs(x))**(1/2)
#    return print(y)
#square(-25.454)
#
# YALANCIKTAN ITERATIVE ASLIDNA RECURSIVE SDFSDFS
#def iterPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    # Your code here
#    res = float(base)
#    if exp == 0:
#        return 1
#    while (exp-1) > 0:
#        exp -= 1
#        res = res * base
#    
#    return res
#
#iterPower(-3.99,3)

#def iterPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    # Your code here
#    res = float(1)
#    if exp == 0:
#        return print(1)
#    while (exp) > 0:
#        exp -= 1
#        res *= base
#    return print(res)
#
#iterPower(-3.99,1)
#
## RECURSION, en kucugu hedef al ve onu tanimla
#def recurPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    # Your code here
#    if exp == 0:
#        return 1
#    else:
#        return base * recurPower(base, exp-1)
#def gcdIter(a, b):
#    '''
#    a, b: positive integers
#    
#    returns: a positive integer, the greatest common divisor of a & b.
#    '''
#    # Your code here
#    if a == 1 or b == 1:
#        return 1
#    if a >= b:
#        c=[]
#        for i in range(2,b+1):
#            if b % i == 0:
#                if a % i == 0:
#                    c.append(i)
#                    print(i)
#    elif b > a:
#        c=[]
#        for i in range(2,a+1):
#            if b % i == 0:
#                if a % i == 0:
#                    c.append(i)    
#    c.sort()
#    return c[-1]   
#
#print(gcdIter(1,14))
#
#def gcdRecur(a, b):
#    '''
#    a, b: positive integers
#    
#    returns: a positive integer, the greatest common divisor of a & b.
#    '''
#    # Your code here
#    if a % b == 0:
#        return b
#    elif a % b != 0:
#        
#        return gcdRecur(b,a%b)
##
#def isIn(char, aStr):
#    char = c
#    if len(aStr)== 0:
#        return True
#    elif len(aStr)== 1:
#        return True
#    elif aStr[0] < aStr[1]:
#        return aStr[1:]
#    elif 
#
#a = input("name")
#b = int(input("age"))
#print(f"your name is: {a}",f"your age is: {b}")
#

#for i in range(4):
#    print("?", end="")
#print()
#import sys
#
#people = {
#    "EMMA": "617-555-0100",
#    "RODRIGO": "617-555-0101",
#    "BRIAN": "617-555-0102",
#    "DAVID": "617-555-0103"
#}
#while True:
#    if "EMMA" in people:
#        print(f"Found {people['EMMA']}")
#        break
#    print("Not found")
#    break
#import re
#s = input("Do you agree?\n")
#
#if re.search("^y(es)?$", s, re.IGNORECASE):
#    print("Agreed.")
#elif re.search("^no?$", s, re.IGNORECASE):
#    print("Not agreed.")
#x = int(input("building level"))
#while True:
#    for i in range(x):
#        print(len(range(i+1))*"#")
#    break

## kac bozuk paran olacak minumum sadece 0.01, 0.25 ve 1 dolarlar var
#
#def bozuk():
#    while True:
#        x = float(input("how much money do u have?"))
#        if x < 0:
#            print("give another value")
#        elif x <1:
#            y = x / (0.25)
#            z = x % (0.25)*100
#            print(int(y+z))
#            break
#        elif x > 1 and x <10:
#            y = x / 1
#            z = x % 1
#            c = z / 0.25
#            v = (z % 0.25)*100
#            print(int(y+c+v))
#            break
#bozuk()
#
a = dict()
a["bir"] = 1
a["iki"] = 2
a["uc"] =3
print(a)
b = dict()
b = {"bir": 1, "iki": 2,"uc":3}
print(b)
for i,k in a.items():
    print("i olam bu",i)
    print("k",k)
print(a.get("iki"))

a.update({"bir":"bir"})
print(a)
del a['iki']
print(a)

for i,k in a.items():
    print(i,k)



    
    
    
    