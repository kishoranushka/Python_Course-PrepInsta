# Currunt workind directory

import os
os.getcwd()


# Absolute path
f = open(r'/Users/rishi/Prepinsta/Pyhton prime course resources/Python Files/sample.txt')

# Relative path
#f1 = open(r'Python Files/sample.txt')


#text = f.read()
text = f.readlines()
f.close()

print(text)