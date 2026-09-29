age = int(input("Enter Your Age:- "))


if (age > 18):
    print("You Can Drive")
elif (age == 18):
    print("Lets schedule an interview")
elif (age == 0):
    print("Hey you are just born")
else:
    print("Sorry you can't drive")

print("End of program")