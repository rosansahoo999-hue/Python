# Two types of modules in python:-
# - Built in modules
# - External modules
# https://docs.python.org/3/py-modindex.html

import math
import os
import mymodules
import requests

print(math.sqrt(16))
mymodules.hello()
r = requests.get("https://www.google.com")
print(r.text)