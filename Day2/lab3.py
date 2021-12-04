#Given the integer N-the number of minutes that is passed since mindnight-how many hours and minutes are displayed on the 24h digital clock
N = int (input("Enter the number of minutes passed since midnight: "))
time = N // 60
hours = N % 60
print ("the hours passed is :" , time)
print ("the minutes passed is :" , hours)
