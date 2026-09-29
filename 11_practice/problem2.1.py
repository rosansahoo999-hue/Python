# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
num = int(input("choice the number(1-7): "))

match num:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('thursday')
    case 6:
        print('friday')
    case 7:
        print('saturday')