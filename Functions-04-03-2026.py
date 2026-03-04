def full_name(first_name, last_name):
    return (first_name + last_name)


f_name = input("Please enter your First Name: ")
l_name = " " + input("Please enter your Last Name: ")

print(f"The Full Name is: {full_name(f_name, l_name)}")