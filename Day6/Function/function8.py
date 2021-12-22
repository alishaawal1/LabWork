#Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(number):
    if number>1:
        for i in range(2,number):
            if number%i == 0:
                return True
                break
            else:
                return False        
num = int(input("Enter a number to check whether it is Prime number or not:"))
if prime(num):
    print(num,"is not a Prime Number.")
else:
    print(num ,"is a Prime Number.")