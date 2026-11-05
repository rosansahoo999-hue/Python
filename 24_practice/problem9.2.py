# Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v1)
print(v2)
print(v3)