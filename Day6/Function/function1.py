#write a python function to print max of three numbers.
def num(num1,num2,num3):
    if (num1>num2)  and (num1>num3):
        print ("the max of three numbers is:", num1)
    elif (num2>num3) and (num2>num1):
        print ("The max of three numbers is:", num2)
    else:
        print ("the mas of three numbers is:", num3)
num(2,4,5)        
    