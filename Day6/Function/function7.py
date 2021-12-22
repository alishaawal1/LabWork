#Write a Python function that accepts a string and 
#calculate the number of upper case letters and lower case letters. 
def case(string1):
    i,j = 0,0
    for l in range(len(string1)):
        k = string1[l]
        if k.isupper():
            i+=1
        else:
            j+= 1
    return i,j
word = input("Enter input a word: ")
Upper,Lower = case(word)
print("The total upper case is:",Upper, "and lower case is:",Lower)