def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x/y
    else:
        return "Cannot divide by Zero(0)"

while True:
    print("Select an Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. End")

    choice = int(input("Please select an option (1, 2, 3, 4, 5) to Begin: "))
    if choice == 5 :
        print("Bye!, Bye!")
        break
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    match choice:
        case 1:
            print("Both numbers are Added: ", add(num1, num2), "\n")
        case 2:
            print("Both numbers are Subtracted: ", subtract(num1, num2), "\n")
        case 3:
            print("Both numbers are Multiply: ", multiply(num1, num2), "\n")
        case 4:
            print("Both numbers are Divided: ", divide(num1, num2), "\n")
        case _:
            print("Invalid choice, please try again")