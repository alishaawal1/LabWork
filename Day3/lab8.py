#Given a n-digit number,find the sum of its digits.
num= int(input("Enter a number: "))
sumOfDigits = 0
for digit in str(num):
    sumOfDigits += int(digit)
print (sumOfDigits)