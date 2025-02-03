num = int(input("enter a number"))
if(num%3==0 and num%6==0):
    print("fizz buzz")
elif(num%3==0):
    print("fizz")
elif(num%6==0):
    print("buzz")
else:
    print("num")