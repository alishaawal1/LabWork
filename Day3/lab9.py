for a in range (0,3):
    username = (input ("Enter your username: "))
    password = (input("Enter your password: "))
    if username == str("facebook"):
        if int (password)==987654321:
            print ("Logged in Successfully.")
            break
    else:
        print ("invalid credentials")