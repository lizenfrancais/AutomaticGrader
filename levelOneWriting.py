def main():
    print("Welcome to the Level 1 Writing Automatic Grader")
    total_points = int(input("Enter the maximum points for the assignment: "))
    requirements = int(input("Enter the number of required topics: "))
    min_words = int(input("Enter the minimum number of words needed: "))
    start_auto_grader = input("Do you want to grade a paper? y/n ").lower()

    while start_auto_grader.startswith("y"):
        grade_student_writing(total_points, requirements, min_words)
        start_auto_grader = input("Would you like to grade another paper? y/n ").lower()
    else:
        print("Thank you for using the Level One Writing Automatic Grader")
        print("....................................")


def grade_student_writing(p, r, w):
    print("....................................")
    print("Preparing to grade student paper.")
    print("....................................")

    requiredWords = w
    requiredTopics = r

    creativeSentences = int(input("Enter number of sentences with creative structures: "))
    simpleSentences = int(input("Enter number of simple sentences: "))
    listsPhrases = int(input("Enter number of lists or memorized phrases: "))
    words = int(input("Enter number of words not included in other structure types: "))

    totalSentences = creativeSentences + simpleSentences + listsPhrases + words

    howUse = howUseFunc(creativeSentences, simpleSentences, listsPhrases, words, totalSentences)

    variety = varietyFunc(requiredWords)

    howWellUnderstood = howWellUnderstoodFunc(totalSentences)

    howAccurate = howAccurateFunc(creativeSentences, simpleSentences, listsPhrases, words, totalSentences)
    
    howThorough = howThoroughFunc(requiredTopics)


    score = ((howUse + variety + howWellUnderstood + howAccurate + howThorough) / 20) * p

    
    print("Scoring paper.......")
    print("....................................")
    print("How use language socre is: ", round(howUse, 1))
    print("What language used score is: ", round(variety, 1))
    print("How well understood score is: " , round(howWellUnderstood, 1))
    print("How accurate score is: " , round(howAccurate, 1))
    print("How thorough score is: " , round(howThorough, 1))
    print("Total score is: ", round(score, 1))
    print("....................................")
    

def howUseFunc(cs, ss, lp, w, ts):

    if cs/ts > .1:
        return 4
    else: return ((cs + (.75 * ss) + (.5 * lp) + (.25 * w) )/ ts) * 4

def varietyFunc(w):

    writtenWords = int(input("Enter the number of words written: "))

    if writtenWords/w > 4:
        return 4
    else: return (writtenWords/w) * 4

def howWellUnderstoodFunc(ts):

    confusion = int(input("Enter number of confusing parts: "))
    english = int(input("Enter number of English instances: "))

    return ((ts - ((confusion + english) * .25)) / ts) * 4

def howAccurateFunc(cs, ss, lp, w, ts):
    
    grammarErrors = int(input("Enter number of grammar errors: "))

    if cs > 0:
        return 4 - (grammarErrors/ts)
    elif ss > 0:
        return 3 - (grammarErrors/ts)
    elif lp >0:
        return 2 - (grammarErrors/ts)
    else: return 1

def howThoroughFunc(rt):

    completionRate = int(input("Enter number of required topics that were completed: "))

    return (completionRate/rt) * 4
    

main()                
