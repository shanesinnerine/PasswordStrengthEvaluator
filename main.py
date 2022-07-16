name = input("Enter your name: ")

# Acquiring a Date of Birth from the User 
dateOfBirth = input("Enter your date of birth MM/DD/YYYY: ")
dateOfBirth.replace(" ", "")
dobList = list(dateOfBirth.split("/"))
day = int(dobList[0]) 
month = int(dobList[1])
year = int(dobList[2])
print(day)
print(month)
print(year)
while(True):
    password = input("Enter a password: ")
    if(password.__contains__(" ") or password.__contains__("\n")):
        print("Illegal input")
    else:
        break
length = len(password)

# Calculate number of capital letters in password
capitalcount = list(filter(lambda c: c.isupper(), password))

#Calculate number of special characters
specialcharcount = list(filter(lambda c: not c.isalnum(), password))

#Test calculations
print("Special count: " + str(len(specialcharcount)))
print("Capital count: " + str(len(capitalcount)))
commonInputs = [] 