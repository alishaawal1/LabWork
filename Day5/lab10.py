# write a Python Program that accepts a string and calculate number of digits and letters
str = input("Input a string: ")
d=l=0
for c in str:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Number of Letters is:", l)
print("Number of Digits is:", d)