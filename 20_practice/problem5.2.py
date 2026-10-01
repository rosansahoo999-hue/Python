# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

num = {
    'rosan': 4563217895,
    'jack': 7539514563,
    'devil': 4568521937,
}

print(num)
print(num.keys())
print(num.values())

for key, value in num.items():
    print(key, value)