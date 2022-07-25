import enchant

def lenScore(password):
    if(len(password) > 12):
        return 100
    if(len(password) == 0):
        return 0
    return 100 - ((13 - len(password)) * 8)

def varietyScore(password):
    capitalCount = len(list(filter(lambda c: c.isupper(), password)))
    specialCharCount = len(list(filter(lambda c: not c.isalnum(), password)))
    numCount = len(list(filter(lambda c: c.isnumeric(), password)))
    total = 10 *  (capitalCount + specialCharCount + numCount)
    if(total > 100):
        return 100
    return total

def patternScore(password):
    return 0

def personalInfoScore(name, password):
    #if(password.contains(name)):
    return 0

def wordsScore(password):
    score = 100
    d = enchant.Dict("en_US")
    longestWord = 0
    for x in range(len(password)):
        for y in range(x + 3, len(password) + 1):
            if d.check(password[x:y]):
                if y - x > longestWord:
                    longestWord = y - x
                score -= 10  
    if score < 0:
        score = 0
    score -= 40 * (longestWord/len(password))
    return score

def repetitionScore(password):
    repDict = dict()
    score = 100
    for x in password:
        repDict[x] = repDict.get(x, 0) + 1
    for value in repDict.values():
        score -= 80 * ((value - 1)/len(password))
        if value == len(password):
            return 0
    if score < 0:
        score = 0
    return score

