age =  int(input("Please enetr age: "))
student = input("Are you a student: ")

if age <= 11 or age >= 65 and student == "No":
    print("Ticket Price: £5")
elif age >= 12 or age <= 64 and student == "Yes":
    print("Ticket price: £8")
else:
    if age >= 12 or age <= 64 and student == "No":
        print("Ticket price: £10")