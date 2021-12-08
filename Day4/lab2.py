#Write a Python program to sum three given integers.
#However, if two or more values areequal sum will be zero.
num1=int (input("Enter a number: "))
num2=int (input("Enter second number: "))
num3= int (input("Enter third number: "))
if(num1==num2 or num1==num3 or num2==num3):
    print ("the sum of given integers is zero.")
else :
    sum=num1+num2+num3
    print ("the sum of given integers is:" , sum)