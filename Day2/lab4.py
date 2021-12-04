#N students take K apples and distribute them evenly
#how many apples will each student get and how many will remain in basket
N= int(input(" Enter the number of students : "))
K= int(input("Enter the number of apples in the basket : "))
student = K / N
remaining = K % N
print ("The number of apples for each student is :" , student)
print ("The number of remaining apples in the basket is :" , remaining)