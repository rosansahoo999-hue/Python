# Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

num1 = int(input("Enter the first number: "))
opr = input("choose operation: ")
num2 = int(input("Enter the second number: "))


match opr:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)