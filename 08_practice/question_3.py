'''
Create variables to store:

Your name (string)
Your age (integer)
Your height in meters (float)
A boolean value representing whether you are a student
Print all of them in one line.
'''

name = 'tamana'
age = 25
height = 154.45
is_student = True

# f string method
print(f"The name of the student is {name}. She is {age} years old. She is {height} cms tall. \nStudents: {is_student}")

# string concating method
print("The name of the student is " + name + ". She is "+ str(age) +" years old. She is "+ str(height) +" cms tall. \nStudents: " +
    str(is_student))