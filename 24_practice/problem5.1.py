# Write a program that asks the user to enter a number and handles:

# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero

# Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError("Number cannot be negative")

    result  = 45/num
    print(f"The result is {result}")

except ValueError:
    print("Error: Please enter a proper number")

except ZeroDivisionError:
    print("Error: Cannot divide by 0")

except NegativeNumberError as e:
    print(f"Error: {e}")

