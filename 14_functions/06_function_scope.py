def  sum(a, b):
    # a nad b are local variable.
    c = a + b
    z = 1  # it create local variable called z which is destroyed after the function returns.
    return c

def greet():
    z = 32 # local variable
    print("Hello")

z = 8  # z is a global variable.
print(sum(4, 6))
print(z)