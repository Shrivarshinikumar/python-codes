num = int(input("Enter a number: "))  
armstrong = sum(int(digit) ** len(str(num)) for digit in str(num))  
if num ==(armstrong):
    print("the number is a armstrong")
else:
    print("the number is not a armstrong")



