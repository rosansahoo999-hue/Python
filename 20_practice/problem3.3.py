# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20)

print(coordinates)
corlist = list(coordinates)
print(corlist)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)