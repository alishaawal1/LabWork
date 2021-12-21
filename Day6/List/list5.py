#Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings.
str = ["helloh","987655","hi","abca","wxyzw","aakansha"]
total = 0
for a in range(0,len(str)):
    b = str[a]
    if len(b)>=2:
        first = b[0]
        last = b[len(b)-1]
        if first == last:
            total = total+1
print("The Number of string having first and last character same and string length 2 is:",total)