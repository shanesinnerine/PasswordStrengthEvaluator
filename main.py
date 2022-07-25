import InputSanitization
import ScoreCalculator

#Get user's name
while(True):
    name = input("Enter your name: ")
    if(InputSanitization.cleanName(name)):
        break

# Get Date of Birth from the User
while(True):
    dateOfBirth = input("Enter your date of birth MM/DD/YYYY: ")
    if(InputSanitization.cleanDoB(dateOfBirth)):
        break

#Get password from user
while(True):
    password = input("Enter a password: ")
    if(InputSanitization.cleanPW(password)):
        print("Illegal input")
    else:
        break

#Calculate scores for password in each category
scores = dict()

#Calculate scores
scores["length"] = ScoreCalculator.lenScore(password)
scores["variety"] = ScoreCalculator.varietyScore(password)
scores["patterns"] = ScoreCalculator.patternScore(password)
scores["personalInfo"] = ScoreCalculator.personalInfoScore(name, password)
scores["words"] = ScoreCalculator.wordsScore(password)
scores["repetition"] = ScoreCalculator.repetitionScore(password)
total = 0
for score in scores.values():
    total += score
print("Score: " + str(total))
