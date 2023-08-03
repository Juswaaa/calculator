while True:
    try:
        # Ask two numbers from the user
        first_number = float(input("Please enter the first number: "))
        second_number = float(input("Please enter the second number: "))

        # Print the operation options
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = int(input("Please enter the operation number (1, 2, 3, 4): "))
    except ValueError:
        print("ERROR! Invalid input. Please enter valid numbers.")
        continue

    # Addition
    if operation == 1:
        sum_result = first_number + second_number
        print(f"The sum is {sum_result}\n")

    # Subtraction
    elif operation == 2:
        difference = first_number - second_number
        print(f"The difference is {difference}\n")

    # Multiplication
    elif operation == 3:
        product = first_number * second_number
        print(f"The product is {product}\n")

    # Division
    elif operation == 4:
        try:
            quotient = first_number / second_number
            print(f"The quotient is {quotient}\n")
        except ZeroDivisionError:
            print("ERROR! You have zero divisor. Please try again.\n")
    else:
        print("ERROR! Invalid operation number. Please enter a number from 1 to 4.\n")
