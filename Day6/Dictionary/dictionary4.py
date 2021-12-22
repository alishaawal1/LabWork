#Write a Python script to check if a given key already exists in a dictionary.  
a = input("Enter a key to remove from Dictionary:")
integer = {"first":1,"third":3,"fifth": 5,"second":2,"seventh":7}
for key_value in integer.items():
    if str(key_value) == a:
        integer.pop(a)
print(integer)
