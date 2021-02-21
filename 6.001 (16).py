def isIn(char, aStr):
    if aStr == '':
        return False
    guess = aStr[len(aStr)//2]
    if guess != char and guess == aStr:
        return False
    elif guess == char:
        return True
    elif guess > char:
        return isIn(char, aStr[0:len(aStr)//2])
    elif guess < char:
        return isIn(char, aStr[len(aStr)//2:])
    
    if len(aStr) <= 1:
        return char == aStr
    half = len(aStr) // 2
    if char == aStr[half]:
        return True
    elif char > aStr[half]:
        return isIn(char, aStr[half:])
    else:
        return isIn(char, aStr[:half])
    
def odd(x,y):
    if y == '':
        return False
    g = y[len(y)//2]
    if g != x and g == y:
        return False
    elif g == x:
        return
    elif g > x:
        return odd(x, y[0:len(y)//2])
    elif g < x:
        return odd(x, y[len(y)//2:])
