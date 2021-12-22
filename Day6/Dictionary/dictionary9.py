#Write a Python program to sum all the items in a dictionary. 
integer = {"first":1,"third":3,"fifth": 5,"second":2,"seventh":7}
a = 0
for key,value in integer.items():
    a = a+int(value)
print("Sum of all item in Dictionary is:", a)