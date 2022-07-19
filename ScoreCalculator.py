def lenScore(password):
    if(len(password) > 12):
        return 100
    if(len(password == 0)):
        return 0
    return 100 - ((13 - len(password)) * 8)

def varietyScore(password):
    capitalCount = list(filter(lambda c: c.isupper(), password))
    specialCharCount = list(filter(lambda c: not c.isalnum(), password))
    numCount = list(filter(lambda c: c.isnumeric(), password))
    total = 10 *  (capitalCount + specialCharCount + numCount)
    if(total > 100):
        return 100
    return total