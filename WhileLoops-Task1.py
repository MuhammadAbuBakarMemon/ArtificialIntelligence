print("Welcome to Abu Bakar's E-Commerce Store (JK I don't wish to own one anytime in the future)")

checker = True

print("Starting to shop")

while checker == True:

    print("1 - Shop For Kitchen Utensils")
    print("2 - Shop For Groceries")
    print("3 - Shop For Clothing")
    print("4 - Shop For Ice-Cream(my favorite)")
    print("5 - Shop For Medicine")
    print("6 - Exit")
    
    temp = int(input("Choose an option: "))
    
    if temp == 1:
        print("a - Frying Pan")
        print("b - Tawwaa")
        print("c - Belan")
        print("d - Checkout")
        
        choice = input("Choose your product: ")
        if choice == 'a' or choice == 'b' or choice == 'c':
            print("Jazakallah for placing your order!!!!")
        
        print("Do you wish to purchase from another category? [Y=YES], [N=NO]")
        ch = input()
        
        if ch == 'Y' or ch == 'y':
            shopmore = True
            continue
        else:
            shopmore = False
            print("Jazakallah for shopping!!!")
            break
        
    elif temp == 2:
        print("a - Cabbage")
        print("b - Tomato")
        print("c - Onion")
        print("d - Checkout")
        
        choice = input("Choose your product: ")
        if choice == 'a' or choice == 'b' or choice == 'c':
            print("Jazakallah for placing your order!!!!")
            
        print("Do you wish to purchase from another category? [Y=YES], [N=NO]")
        ch = input()
        
        if ch == 'Y' or ch == 'y':
            shopmore = True
            continue
        else:
            shopmore = False
            print("Jazakallah for shopping!!!")
            break
        
    elif temp == 3:
        print("a - Jeans")
        print("b - T-Shirt")
        print("c - Cardigan")
        print("d - Checkout")
        
        choice = input("Choose your product: ")
        if choice == 'a' or choice == 'b' or choice == 'c':
            print("Jazakallah for placing your order!!!!")
            
        print("Do you wish to purchase from another category? [Y=YES], [N=NO]")
        ch = input()
        
        if ch == 'Y' or ch == 'y':
            shopmore = True
            continue
        else:
            shopmore = False
            print("Jazakallah for shopping!!!")
            break
        
    elif temp == 4:
        print("a - Choclate Fudge")
        print("b - Pistachio Delight")
        print("c - Mango Melody")
        print("d - Checkout")
        
        choice = input("Choose your product: ")
        if choice == 'a' or choice == 'b' or choice == 'c':
            print("Jazakallah for placing your order!!!!")
            
        print("Do you wish to purchase from another category? [Y=YES], [N=NO]")
        ch = input()
        
        if ch == 'Y' or ch == 'y':
            shopmore = True
            continue 
        else:
            shopmore = False
            print("Jazakallah for shopping!!!")
            break
        
    elif temp == 5:
        print("a - Panadol")
        print("b - Brufen")
        print("c - Anesthesia")
        print("d - Checkout")
        
        choice = input("Choose your product: ")
        if choice == 'a' or choice == 'b' or choice == 'c':
            print("Jazakallah for placing your order!!!!")
            
        print("Do you wish to purchase from another category? [Y=YES], [N=NO]")
        ch = input()
        
        if ch == 'Y' or ch == 'y':
            shopmore = True
            continue
        else:
            shopmore = False
            print("Jazakallah for shopping!!!")
            break
    
    elif temp == 6:
        print("Exitting the store!!!\nWe hope to see you again.")
        checker = False
    
    else:
            print("Invalid option choosen.")
        
        