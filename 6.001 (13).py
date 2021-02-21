def iterPower(base, exp):
    z= 1
    while exp>0: 
        z = z*base
        exp -= 1
    print(z)
    return(z)
iterPower(2,3)

def odd(x,y):
    """ 
    mathematical induction is done
    even the result was satisfying, this thing did not work in website
    idk why
    """
    if y == 0:
        return 1
    else:
        return x * odd(x, y-1)
print(odd(2,3)) 
