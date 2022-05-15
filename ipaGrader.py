def main():
    print("Welcome to the Integrated Performance Assessment Automatic Grader")
    print("Helping you ensure consistent socres across student work.")
    readyToGrade = input("Are you ready to grade an IPA? y/n ").lower()

    while readyToGrade.startswith("y"):
        startGrading()
        readyToGrade = input("Would you like to continue grading? y/n ").lower()
    else:
        print("Thank you for using the Integrated Performance Assessment Automatic Grader.")
        print("....................................")

def startGrading():
    print("Launching Auotmaic Grader.......")
    print("....................................")
    courseLevel = int(input("Enter the numeral for the course level you are grading. "))

    if courseLevel == 1:
        print("Launching Level One program...........")
        print("....................................")
        gradeLevelOne()
    elif courseLevel == 2:
        print("Launching Level Two program........")
        print("....................................")
        gradeLevelTwo()
    else:
        print("This program only grades Levels 1 and 2.")
        print("....................................")

def gradeLevelOne():
    promptType = input("Enter the type of prompt you are grading: speaking or writing ").lower()

    if promptType.startswith("s"):
        print("Launcing Level One Speaking program........")
        print("....................................")
        levelOneSpeaking()
    elif promptType.startswith("w"):
        print ("Launching Level One Writing program........")
        print("....................................")
        levelOneWriting()
    else:
        print("Prompt type not recognized.")
        print("....................................")
        gradeLevelOne()

def levelOneSpeaking():
    import levelOneSpeaking 

def levelOneWriting():
    import levelOneWriting

def gradeLevelTwo():
    promptType = input("Enter the type of prompt you are grading: speaking or writing ").lower()

    if promptType.startswith("s"):
        print("Launching Level Two Speaking program......")
        print("....................................")
        levelTwoSpeaking()
    elif promptType.startswith("w"):
        print("Launching Level Two Writing program.......")
        print("....................................")
        levelTwoWriting()
    else:
        print("Prompt type not recognized.")
        print("....................................")
        gradeLevelTwo()

def levelTwoSpeaking():
    import levelTwoSpeaking

def levelTwoWriting():
    import levelTwoWriting

main()
