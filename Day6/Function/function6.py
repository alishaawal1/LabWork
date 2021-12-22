#Write a Python program to reverse a string. 
word=input("Enter a word:")
def reverse(input_word):
    w=""
    for i in range (1,len(input_word)+1):
        l=len(input_word)-i
        w=w+input_word[l]
    return w
reversee=reverse(word)
print ("The reverse of ",word,"is:",reversee)