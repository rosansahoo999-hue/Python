# String formating

template = "Dear {}, you are awesome. take this {}$ bag"
a = 'Jhon'
a1 = 10000
b = 'Jack'
b1 = 1000
c = 'Marie'
c1 = 300

s1 = template.format(a, a1)
print(s1)
print(f"{a} you are awesome and take this {a1}$ bag")