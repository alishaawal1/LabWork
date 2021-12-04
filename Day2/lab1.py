#convert seconds to days,hours,minutes
time = int (input("Enter time in Seconds :"))
day = time // (60*60*24)
print ("total day for given seconds is : " , day)
hour = time // (60*60)
print ("total hour for given seconds is : ", hour)
minute = time // 60
print ("total minutes for given seconds in : ", minute)