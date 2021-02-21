def is_prime(n):
    import math
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

x = int(input("give me a fucking number: "))
if is_prime(x):
    print("this is a prime number")
else:
    print("this is not a primbe number: ")
    
    
    