#Write a Python function that checks whether a passed string is palindrome or not.
def Palindrome(word1):
    w = ""
    for i in range(1,len(word1)+1):
        l = len(word1)-i
        w = w + word1[l]
    if w.upper() == word.upper():
        print(word,"is a Palindrome string")
    else:
        print(word ,"is not a Palindrome string")     
word = input("Enter a string to check whether it is Palindrome String or not: ")
Palindrome(word)