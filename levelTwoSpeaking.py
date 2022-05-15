def main():
    print("Welcome to the Level 2 Speaking Automatic Grader")
    max_points = int(input("Enter the maximum points for the assignment: "))
    start_auto_grader = input("Do you want to grade a paper? y/n ").lower()

    while start_auto_grader.startswith("y"):
        grade_student_speaking(max_points)
        start_auto_grader = input("Would you like to grade another paper? y/n ")
    else:
        print("Thank you for using the Fremch 2 IPA Speaking Auto Grader")
        print("....................................")

def grade_student_speaking(p):
    print("....................................")
    print("Preparing to grade student paper.")
    print("....................................")

    replyNumber = int(input("Enter number of sentences/replies student spoke: "))
    
    how_use = howUse(replyNumber)

    what_language = whatLanguage(replyNumber)

    accuracy = accuracyFunc(replyNumber)

    understood = understoodFunc()
    
    understand = understandFunc(replyNumber)
    
    score = ((how_use + what_language + accuracy + understood + understand)/20) * p
    
    print("Scoring paper.......")
    print("....................................")
    print("How use language socre is: " ,round(how_use, 1))
    print("What language used score is: ", round(what_language, 1))
    print("How accurate score is: ", round(accuracy, 1))
    print("How well understood score is: ", round(understood, 1))
    print("How well understands score is: ", round(understand, 1))
    print("Total score is: ", round(score, 1))
    print("....................................")

def howUse(r):
    creative = int(input("Enter number of replies that used creative structures: "))/r
    basic = int(input("Enter number of replies that used basic structures: "))/r
    phrases = int(input("Enter number of replies that used phrases: "))/r
    words = int(input("Enter number of replies that used words only: "))/r

    if creative >= .25:
        return 4
    elif creative + basic >= .8:
        return 3 + creative - ((phrases + words)/2)
    else: 
        return (basic*3)+ (phrases*2) + words

def whatLanguage(r):
    detail = int(input("Enter number of replies that included a detail: "))/r
    limited = int(input("Enter number of replies that seemed repetitious: "))/r

    return detail + 3 - (limited*2)

def accuracyFunc(r):
    print("Select the number that represemts the structure type used in the majority of replies.")
    accuracyType = int(input("complex sentences = 4 sentences = 3 phrases = 2 words = 1 "))
    accuracyRate = int(input("Enter number of error free replies: "))/r

    if accuracyType == 4:
        return 4
    else: return accuracyRate * (accuracyType+1) 

def understoodFunc():
    pronunciation = int(input("Enter number of times pronunication impacted understanding: "))
    confusion = int(input("Enter the number of confusing replies: "))

    return 4 - ((pronunciation + confusion)/10)

def understandFunc(r):
    helpPercent = int(input("Enter number of questions student needed help with: "))/r
    skipped = int(input("Enter number of questions student did not answer: "))

    return 4 - (helpPercent*2) - (skipped/(skipped+r)*4)
    
main()
