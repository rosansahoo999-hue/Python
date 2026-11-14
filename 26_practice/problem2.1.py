# Write a program that writes three lines of text to a file tasks.txt.

with open("tasks.txt", "w") as f:
    f.write("line1\n")
    f.write("line2\n")
    f.write("line3\n")