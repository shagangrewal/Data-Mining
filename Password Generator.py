import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ?.*&%$@_+!'
a = int(input("Enter the length of the password you want!!: "))
while a>20:
    print("Maximum password length allowed is 20 characters")
    a = int(input("Enter the length of the password you want!!: "))

password = ''
for i in range(a):
    password += random.choice(chars)
print(password)
