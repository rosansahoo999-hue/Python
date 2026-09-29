# Take a user input string and check if it is a palindrome (same forwards and backwards).

string = input("Enter the word: ")

if(string == string[::-1]):
    print("The string is the palindrome")
else:
    print("The string is can't palindrom")