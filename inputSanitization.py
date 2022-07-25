def cleanDoB(dateOfBirth):
    dateOfBirth.replace(" ", "")
    dobList = list(dateOfBirth.split("/"))
    if (len(dobList) == 3 and len(dateOfBirth) == 10):
        try:
            day = int(dobList[0])
            month = int(dobList[1])
            year = int(dobList[2])
        except:
            print("Use Numbers dummy")
            return False
        if ((int(dobList[0]) == 2) and (int(dobList[1]) > 29)):
            print("February is not that long bro...")
            return False
        elif ((0 < int(dobList[0]) <= 12) and (0 < int(dobList[1]) <= 31)):
            return True
    else:
        print("Are you stupid enter a good DOB")
    return False

def cleanPW(password):
    return password.__contains__(" ") or password.__contains__("\n")

def cleanName(name):
    if (any(str.isdigit(c) for c in name)):
        print("Don't use numbers")
        return False
    nameList = name.split(" ")
    if (len(nameList) == 3):
        try:
            first = nameList[0] 
            middle = nameList[1]
            last = nameList[2]
        except:
            print("Enter a full name")
            return False
    if (len(nameList) == 2):
        try:
            first = nameList[0]
            last = nameList[1]
        except:
            print("Enter a full name")
            return False
    else:
        print("Are you stupid enter a good name")
        return False
    return True