#write a python program to multiply all the items in a list.
def multiply(items):
    r=1
    for x in items:
        r*=x
    return r
print (multiply([1,12,3,56]))