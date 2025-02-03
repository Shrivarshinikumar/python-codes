num = abs(int(input("Enter a number: "))) 
if num < 10:
    print("Number has only one digit!")
else:
    print("Second last digit:", str(num)[-2])