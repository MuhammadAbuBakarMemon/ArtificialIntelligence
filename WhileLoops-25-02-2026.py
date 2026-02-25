num = int(input("Enter a number to print the table of: "))
a = 1
while a <= 10:
    print(f"{num} x {a} : {num * a}")
    a += 1
else:
    print("Idk what to type here, but HTF does an else execute below a while block without an if statement.")