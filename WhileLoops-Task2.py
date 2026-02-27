
attempts = True #flag variable

while attempts == True:
    
    user = input("Enter your Username: ").lower()
    password = input("Enter your password: ")
    
    if user == "abu bakar" and password == "1234":
        print("Login successfull")
        
        while True:
            select = int(input("Select your category: \n1.Clothing \n2.Grocery \n3.Books \n4.Games"))
            
            if select == 1:
                print("Welcome to the clothing store!")
            elif select == 2:
                print("Welcome to the Grocery store!")
            elif select == 3:
                print("Welcome to the Books store!")
            elif select == 4:
                print("Welcome to the Game store")
            else:
                print("Invalid options!")
            
            rerun = input("Do you want to continue? (yes/no): ").lower()
            
            if rerun == "yes":
                print("proceeding for options -->")
                continue
            else:
                print("Jazakallah for shopping!!!")
                
                attempts = False
                break
    else:
        print("Login failed!")
        
        rerun = input("Do you want to continue? (yes/no): ").lower()
        
        if rerun == "yes":
            continue
        else:
            attempts = False
            break
            
