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

def commonPhrases(password):
    phrases = ["qwerty", "wasd", "lmao", "lol", "omg", "wtf", "lmfao"]
    score = 100
    phraseLength = 0
    for i in phrases:
        if i in password.lower():
            phraseLength += len(i)
    score -= (phraseLength/len(password) * 100)
    return score

def patternScore(password):
    #multiple adjacent keyboard keys
    #counting numbers up or down
    score = 100
    pLength = 1
    for i in range(0, len(password) - 1):
        if ord(password[i]) - ord(password [i + 1] ) == 0:
            pLength += 1
        elif abs(int(ord(password[i])) - ord(password[i + 1])) == 1:
            pLength += 1
        else:
            if pLength != 1:
                score -= (pLength/len(password)) * 100
                pLength = 1
    if pLength != 1:
        score -= (pLength/len(password)) * 100
    if score < 0:
        return 0
    return score

def personalInfoScore(dob, name, password):
    score = 100
    nameList = name.split(" ")
    dob.replace(" ", "")
    dobList = list(dob.split("/"))
    decrement = 100/(len(nameList) + 3)
    for i in nameList:
        if (i in password):
                score -= decrement
    for thing in dobList:
        if (thing in password):
            score -= decrement
    if score < 0:
        return 0
    return score

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

