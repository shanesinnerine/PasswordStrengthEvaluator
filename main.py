import inputSanitization

#Get user's name
name = input("Enter your name: ")

# Get Date of Birth from the User
while(True):
    dateOfBirth = input("Enter your date of birth MM/DD/YYYY: ")
    if(inputSanitization.cleanDoB(dateOfBirth)):
        break

#Get password from user
while(True):
    password = input("Enter a password: ")
    if(inputSanitization.cleanPW(password)):
        print("Illegal input")
    else:
        break

#Calculate length of password
length = len(password)

# Calculate number of capital letters in password
capitalcount = list(filter(lambda c: c.isupper(), password))

#Calculate number of special characters
specialcharcount = list(filter(lambda c: not c.isalnum(), password))

#Test calculations
print("Special count: " + str(len(specialcharcount)))
print("Capital count: " + str(len(capitalcount)))
commonInputs = [] 