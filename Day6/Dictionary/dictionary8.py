#Write a Python script to merge two Python dictionaries. 
dict1 = {"first":1,"second":2}
dict2 = {"second_last":3,"last":4}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)