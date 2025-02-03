num1 =int(input("enter a number"))
num2 =int(input("enter a number"))
def add_and_sub(num1,num2):
    add= num1+num2
    if num1>num2:
        sub = num1-num2
    else:
        sub = num2-num1
    return (add,sub)

sum_result=add_and_sub(num1,num2)
sub_result=add_and_sub(num1,num2)


print("addition result",sum_result)
print("subtraction result",sub_result)


    