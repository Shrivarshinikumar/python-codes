def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial (n-1)

num =int(input("enter the number"))

if(num<0):
    print("there is no factorial for negative numbers")
else:
    print(f"factorial of {num} is {factorial(num)}.")

