#Write a Python program to get the largest number from a list. 
def max_num_in_list( list ):
    max = list[ 0 ]
    for i in list:
        if i > max:
            max = i
    return max
print((max_num_in_list([48, 29, 19, 50])), "is the largest number in list")
