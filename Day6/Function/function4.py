#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter). 
#For example, if limit is 20, 
#it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def num(limit):
    sum1=0
    for x in range(limit+1):
        if (x%3==0) and (x%5==0):
            sum1+=x
    return sum1
num1=int(input("Enter a a number:"))
sum1= num(num1)
print ("The sum of multiples of 3 and 5 is:",sum1)