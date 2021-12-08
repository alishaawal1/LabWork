#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user.
#Number of classes held,Number of classes attended.
#And print:percentage of class attended,Is student is allowed to sit in exam or not.
class_held = int(input("Enter the number of total classes held: "))
attended = int (input("Enter the number of classes student attended: "))
percent = (attended / class_held)*100
print ("The total number of classes held: ", class_held)
print ("The number of classes aatended by student is: ", attended)
print ("percentage of class attended is: ", percent ,"%")
if percent>75 and percent<=100:
    print ("You are allowed to sit in exam.")
else:
    print ("You are not allowed to sit in exam.")