# Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.

while(text := input("Enter Something: ")) != "quit":
    print(f"You entered {text}")