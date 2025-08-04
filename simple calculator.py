def calculator():
    # Prompt the user to choose an operator
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # User Input for the Operator
    choice = input("Enter choice (1/2/3/4): ")

    # User Input for the Numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == '1' or choice == '+':
        print(f"{num1} + {num2} = {num1 + num2}")

    elif choice == '2' or choice == '-':
        print(f"{num1} - {num2} = {num1 - num2}")

    elif choice == '3' or choice == '*':
        print(f"{num1} * {num2} = {num1 * num2}")

    elif choice == '4' or choice == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid Input. Please enter a valid choice.")

if __name__ == "__main__":
    calculator()