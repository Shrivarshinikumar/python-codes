weight = int(input("enter the weight of the clothes"))

if(weight>8000):
    print("over loaded")
elif(weight==0):
    print("the time needed is zero")
elif(weight<0):
    print("invalid input")
else:
    if(weight<2000):
        print("the time needed is 25 min")
    elif(weight>2000 and weight<=3000):
        print("the needed time is 35")
    elif(weight>3000):
           print("the needed time is 45")
    else:
        print("invalid input")