# Create a class MathUtils with:

# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."

class MathUtils: 
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

a = MathUtils
print(a.add(3, 54))
a.description()
print("\n")

# Call both methods without creating an object
MathUtils.description()
print(MathUtils.add(4, 6))