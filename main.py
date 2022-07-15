name = input("Enter your name: ")
dateOfBirth = input("Enter your date of birth")
a = 1
day = a
month = a
year = a
password = input("Enter a password: ")
length = len(password)
capitalcount = list(filter(lambda c: c.isupper(), password))
print(password)
print(len(capitalcount))
specialcharcount = a
commonInputs = [] 