grade = int(input("Enter you score between 1 and 100: "))


if grade < 0 or grade > 100:
    print("Invalid input.")
elif grade >= 90:
    print("Grade: A  Amazing!")
elif grade >= 80:
    print("Grade: B  Good")
elif grade >= 70:
    print("Grade: C  Keep improving")
elif grade >= 60:
    print("Grade: D  Bad")
else:
    print("Grade: F  You got work to do")