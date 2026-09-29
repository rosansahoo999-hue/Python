name = 'Rosan' # strings are immutable
# name[0] = "H"  # you can't do this
print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'

# ----------------------------
# print(name)
# a = len(name)
# print(a)

# -----------------------------
s = 'hello world'
y = 'HELLO WORLD'
# a = len(s)
# print(a)
# print(s.upper(),'=', s)
# print(y.lower(),'=', y)
# print(s.capitalize(),"=", s)
# print(s.title(),'=', s)

# -------------------------------
text = " hello world "
# print(text.strip(),'/', text)  # output: "hello world"
# print(text.lstrip(),'/', text) # output: "hello world "
# print(text.rstrip(),'/', text) # output: " hello world"

# ---------------------------------
text1 = 'python is fun and fun and fun'
# print(text1.find('is')) # output- 7 index of first occurence
# print(text1.replace('fun', 'awesome')) # replace the word

# -----------------------------------
fruits = "Apples,Bananas,Pineapples"
# print(fruits)
# print(fruits.split(','))
# print(",".join(['Apples', 'Bananas', 'Pineapples']))

# --------------------------------------------------
lang = "python123"
print(lang.isalpha()) # false
print(lang.isdigit()) # false
print(lang.isalnum()) # true 
print(lang.isspace()) # false