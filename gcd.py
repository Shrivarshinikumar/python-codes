import math
def lcm(a,b):  
    return(a*b)//math.gcd(a,b)

a = int(input("enter the value of a"))
b = int(input("enter the value of b"))

print("the lcm of the given numbers is ",lcm(a,b))