#Write a Python program to remove an item from a set if it is present in the set.  
integers = {1,2,3,4,5}
a = int(input("Enter a number to remove from set:"))
for i in integers:
    if i == a:
        integers.remove(a)
        break   
print(integers)