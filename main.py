import InputSanitization
import ScoreCalculator

#Get user's name
name = input("Enter your name: ")

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
scores["personalInfo"] = ScoreCalculator.personalInfoScore(password)
scores["words"] = ScoreCalculator.wordsScore(password)
scores["repetition"] = ScoreCalculator.repetitionScore(password)