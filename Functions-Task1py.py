def courses(sub1, sub2, sub3, sub4, sub5):
    return (sub1 + sub2 + sub3 + sub4 + sub5)

def per(obtain):
    return ((obtain / 500) * 100)

def grade(name, perc):
    if perc >= 90:
        grade = f"Dear {name} Grade A+"
    elif perc >= 86:
        grade = f"Dear {name} Grade A"
    elif perc >= 82:
        grade = f"Dear {name} Grade A-"
    elif perc >= 78:
        grade = f"Dear {name} Grade B+"
    elif perc >= 74:
        grade = f"Dear {name} Grade B"
    elif perc >= 70:
        grade = f"Dear {name} Grade B-"
    elif perc >= 66:
        grade = f"Dear {name} Grade C+"
    elif perc >= 62:
        grade = f"Dear {name} Grade C"
    elif perc >= 58:
        grade = f"Dear {name} Grade C-"
    elif perc >= 54:
        grade = f"Dear {name} Grade D+"
    elif perc >= 50:
        grade = f"Dear {name} Grade D"
    else:
        grade = f"Dear {name} Grade Failed"
    return grade
        
sub1 = int(input("Enter your Subject 1 Marks: "))
sub2 = int(input("Enter your Subject 2 Marks: "))
sub3 = int(input("Enter your Subject 3 Marks: "))
sub4 = int(input("Enter your Subject 4 Marks: "))
sub5 = int(input("Enter your Subject 5 Marks: "))

print(grade("Muhammad Abu Bakar", per(courses(sub1, sub2, sub3, sub4, sub5))))