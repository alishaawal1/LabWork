#Write a funtion called fizz_buzz that takes a number
#if the number is divisible by 3,it should return 'fizz'
#if the number is divisible by 5,it should return 'fizz'
#if the number is divisible by both 3 and 5,it should 'fizzbuzz'
a = int(input("Enter a number: "))
def fizz_buzz(num):
    if num % 3 == 0  and num % 5==0:
        print("fizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

fizz_buzz(a)