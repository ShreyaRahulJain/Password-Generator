import random
x=int(input("Enter the length of the password - "))
o=""
for i in range(x):
    o=o+chr(random.randrange(65,98,1))
print(o)
