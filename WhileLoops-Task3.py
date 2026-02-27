#nested while nested if and or multple conditions
#control loop statemensts as well

keepgoing = True
count = 3

while keepgoing == True and count > 0:
    
    print("Welcome to Abu Bakar's Ice-Cream factory!!!")
    
    uid = input("Enter your user account: \n").lower()
    pwd = input("Enter password: \n")
    
    loginstatus = False
    
    if uid == "abu bakar" and pwd == "1234":
        
        print("Mr.Abu Bakar, Successfully Logged In!!!")
        loginstatus = True
        print("Assalam u Alaikum, and welcome to abu bakar's Ice-cream factory, the only company that produces DAIRY Ice-Creams in Pakistan, we do not sell Frozen Desserts!")
    
    elif uid == "ali" and pwd == "1234":
        
        print("Mr.Ali, Successfully Logged In!!!")
        loginstatus = True
        print("Assalam u Alaikum, and welcome to abu bakar's Ice-cream factory, the only company that produces DAIRY Ice-Creams in Pakistan, we do not sell Frozen Desserts!")
        
    else:
        
        if count != 0:
            print("Invalid credentials, user does not exist in the database!!!")
            count -= 1
            
            print(f"You have {count} attempts remaining.")
            continue
        elif count == 0:
            print("Invalid credentials, user does not exist in the database!!!")
            print("You have ran out of attempts to try and Login!\nTry again after 30 minutes!!!")
            #idk how to try and make my system sleep for about 30 seconds, all I know is how to use a break statement and exit my program
            break
            
            
    while loginstatus == True:
        
        print("1. Devour a Cone.\n2. Devour an Ice-cream Tub.\n3. Donate an Ice-Cream.\n4. Exit.\nAnyother option also leads you to exitting the program.")
        
        opt = int(input("Choose an option: "))
        
        if opt == 1:
            print("Choose your flavour: ")
            print("1. Choclate Fudge.\n2. Mango Delight.\n3. Choclate Fudge.\n4. Go Back")
            choice = int(input())
            
            if choice == 1 or choice == 2:
                print("Choclate Fudege Cone, an excellent choice!!!")
            
            elif choice == 2:
                print("Mango Delight Cone, an excellent choice!!!")
                
            else:
                print("Going Back to Main Menu.")
                continue
                
            nestedchoice = input("Do you wish to choose another option? (Y=Yes, N=No)").lower()
            if nestedchoice == "y":
                loginstatus = True
            elif nestedchoice == "n":
                loginstatus = False
            else:
                print("Invalid character entered, choosing default option, No.")
                break
            
        elif opt == 2:
            print("Choose your flavour: ")
            print("1. Choclate Fudge.\n2. Mango Delight.\n3. Choclate Fudge.\n4. Go Back")
            choice = int(input())
            
            if choice == 1 or choice == 2:
                print("Choclate Fudege Tub, an excellent choice!!!")
            
            elif choice == 2:
                print("Mango Delight Tub, an excellent choice!!!")
                
            else:
                print("Going Back to Main Menu.")
                continue
            
            nestedchoice = input("Do you wish to choose another option? (Y=Yes, N=No)").lower()
            if nestedchoice == "y":
                loginstatus = True
            elif nestedchoice == "n":
                loginstatus = False
            else:
                print("Invalid character entered, choosing default option, No.")
                break
            
        elif opt == 3:
            print("You are such a nice person, may Allah Almighty bless you.")
            print("Jazakallah for donating an Ice-cream, we wll make sure it reaches the children who can't afford one!!!")
            
            nestedchoice = input("Do you wish to choose another option? (Y=Yes, N=No)").lower()
            if nestedchoice == "y":
                loginstatus = True
            elif nestedchoice == "n":
                loginstatus = False
            else:
                print("Invalid character entered, choosing default option, No.")
                break
            
        else:
            print("Sed to see you go, We wish to see you again soon!!!")
            print("Allah Hafiz, Tata Bye Bye Kiddo!!!")
            loginstatus = False
            break
    
    inp = input("Do you wish to switch accounts? (Y = Yes, N = No)").lower()
    
    if inp == "y":
        keepgoing = True
    elif inp == "n":
        keepgoing = False
    else:
        print("Invalid character entered, opting for the default option.")
        keepgoing = True
            
            
            
        
