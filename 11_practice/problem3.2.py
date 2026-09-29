# Print the multiplication table of a number (entered by user).

num = int(input('Enter the user number: '))

for i in range(1, 11):
    j = num * (i)
    print(f'{num} x {i} = {j}')