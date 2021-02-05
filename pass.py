# import module
import string as s
from random import *

# make some type of password 
ch = s.ascii_letters + s.digits + s.punctuation

# let's define number of password charecter
password = "".join(choice(ch) for x in range(randint(8, 12)))
# print the password
print(password)