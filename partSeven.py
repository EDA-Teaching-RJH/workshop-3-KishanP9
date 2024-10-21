def calculator():
    while True:
        num_1 = input("Enter 1st number or type 'quit' to exit: ")
        if num_1.lower() == "quit":
            print("Goodbye!")


        num_2 = input("Enter 2nd number: ")
        operation = input("Select an operation  (+, -, *, /, ^, %): ")

        try:
            num1 = float(num_1)
            num2 = float(num_2)

            match operation:
                case '+':
                    result = num1 + num2
                    print(f"{num1} + {num2} = {result}")
                case '-':
                    result = num1 - num2
                    print(f"{num1} - {num2} = {result}")
                case '*':
                    result = num1 * num2
                    print(f"{num1} * {num2} = {result}")
                case '/':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"{num1} / {num2} = {result}")
                    else:
                        print("Error!!!")
                case '^':
                    result = num1 ** num2
                    print(f"{num1} ^ {num2} = {result}")
                case '%':
                    if num2 != 0:
                        result = num1 % num2
                        print(f"{num1} % {num2} = {result}")
                    else:
                        print("Error!!!")
                case _:
                    print("Invalid operation")
        except ValueError:
            print("Invalid input. Enter valid number:")

calculator()