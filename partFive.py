day = input("Enter the current day of the week:")

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("It's a Weekday.")
else:
    if day == "Saturday" or day == "Sunday":
        print("It's the weekend!")