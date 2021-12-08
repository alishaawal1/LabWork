#Check whether the given year is leap year or not.
# If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
year = int (input("Enter a year: "))
if (year%4)==0:
    if (year%100)==0:
        if (year % 400 ) ==0:
            print (year, "is leap year.")
        else:
            print (year, "is common year.")
    else:
        print (year ,"is  leap year.")
else:
    print (year, "is common year.")