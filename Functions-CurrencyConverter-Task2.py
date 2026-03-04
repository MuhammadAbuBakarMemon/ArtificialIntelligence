#DESIGN OUR VERY OWN CURRENCY CONVERTER

#PKR TO EURO & VICEVERSA
def pkrtoeuro(n1):
    return (n1 * 0.0031)

def eurotopkr(n1):
    return (n1 * 324.15)

#PKR TO LIRA & VICEVERSA
def pkrtolira(n1):
    return (n1 * 0.16)

def liratopkr(n1):
    return (n1 * 6.36)

#PKR TO RIYAL & VICEVERSA
def pkrtoriyal(n1):
    return (n1 * 0.013)

def riyaltopkr(n1):
    return (n1 * 74.43)

#PKR TO KUWAITI DINAR AND VICEVERSA
def pkrtodinar(n1):
    return (n1 * 0.0011)

def dinartopkr(n1):
    return (n1 * 908.63)

#PKR TO TAKKA AND VICERVERSA
def pkrtotakka(n1):
    return (n1 * 0.44)


def takkatopkr(n1):
    return (n1 * 2.29)

# CREATING THE MAIN PROGRAM

print("Welcome to Abu Bakar's very own currency converter\n")

rerun = True

while rerun == True:
    print("Select a conversion of your choice")
    print("1- PKR TO EURO")
    print("2- EURO TO PKR")
    print("3- PKR TO LIRA")
    print("4- LIRA TO PKR")
    print("5- PKR TO RIYAL")
    print("6- RIYAL TO PKR")
    print("7- PKR TO KUWAITI DINAR")
    print("8- KUWAITI DINAR TO PKR")
    print("9- PKR TO TAKKA")
    print("10- TAKKA TO PKR")
    print("Press any other key to exit.")

    choice = int(input())

    amt = float(input("Enter the amount: "))

    if(choice == 1):
        print(f"You have {pkrtoeuro(amt)} EUROS in your posession!!!")
    elif (choice == 2):
        print(f"You have {eurotopkr(amt)} PKR in your posession!!!")
    elif (choice == 3):
        print(f"You have {pkrtolira(amt)} LIRA in your posession!!!")
    elif (choice == 4):
        print(f"You have {liratopkr(amt)} PKR in your posession!!!")
    elif (choice == 5):
        print(f"You have {pkrtoriyal(amt)} RIYAL in your posession!!!")
    elif (choice == 6):
        print(f"You have {riyaltopkr(amt)} PKR in your posesson!!!")
    elif (choice == 7):
        print(f"You have {pkrtodinar(amt)} DINAR in your posession!!!")
    elif (choice == 8):
        print(f"You have {dinartopkr(amt)} PKR in your posession!!!")
    elif (choice == 9):
        print(f"You have {pkrtotakka(amt)} TAKKA in your posession!!!")
    elif (choice == 10):
        print(f"You have {takkatopkr(amt)} PKR in your posession!!!")
    else:
        print("Exitting Program!!!")
        rerun = False
    
