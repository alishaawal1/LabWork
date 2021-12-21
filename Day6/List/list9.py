#Write a Python program to select an item randomly from a list.
import random
abc = ["hello","hi","98130","ksd","654","copy","append","lab"]
i = random.randint(0,len(abc))
print ("The Randomly selected item  is:", abc[i])