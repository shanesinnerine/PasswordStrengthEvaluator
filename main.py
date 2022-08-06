import InputSanitization
import ScoreCalculator

def printDashedLine():
    print("----------------------------------------------------------")


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

while(True):
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
    scores["Length"] = ScoreCalculator.lenScore(password)
    scores["Variety"] = ScoreCalculator.varietyScore(password)
    scores["Patterns"] = ScoreCalculator.patternScore(password)
    scores["PersonalInfo"] = ScoreCalculator.personalInfoScore(dateOfBirth, name, password)
    scores["Words"] = ScoreCalculator.wordsScore(password)
    scores["Repetition"] = ScoreCalculator.repetitionScore(password)
    total = 0
    for score in scores.values():
        total += score
    printDashedLine()
    print("Total score: " + str(int(total)))
    printDashedLine()
    print("Please choose one of the following options:")
    while(True):
        choice = input("1. Detailed score breakdown\n2. Password strengths\n3. Password weaknesses\n4. Enter another password\n5. Exit program\n Selection: ")
        printDashedLine()
        if choice == "1":
            for score in scores.keys():
                print(score + "score = " + str(int(scores.get(score))))
            print("Total score: " + str(total))

            input("Press any button to continue")
        elif choice == "2":
            for score in scores.keys():
                if scores.get(score) > 70:
                    print(score)
            input("Press any button to continue")
        elif choice == "3":
            for score in scores.keys():
                if scores.get(score) <= 60:
                    print(score)
            input("Press any button to continue")
        printDashedLine()
        if choice == "4":
            break
        elif choice == "5":
            quit()
