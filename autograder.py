labNum = int(input("Enter the number of labs completed: "))
quizNum = int(input("Enter the number of quizzes completed: "))
if labNum >= 6:
    labGrade = 20
else:
    labGrade = (labNum/6) * 20
if quizNum >= 6:
    quizGrade = 15
else:
    quizGrade = (quizNum/6) * 15
assignment1 = int(input("Enter grade for Assignment 1: ")) 
assignment2 = int(input("Enter grade for Assignment 2: "))
assignment3 = int(input("Enter grade for Assignment 3: "))
assignment4 = int(input("Enter grade for Assignment 4: "))
midterm1 = int(input("Enter grade for Midterm 1: "))
midterm2 = int(input("Enter grade for Midterm 2: "))
final = int(input("Enter grade for Final Exam: "))
prep = int(input("Enter grade for Midterms and Final Preparation: "))
finalGrade = labGrade + quizGrade + (assignment1 * 0.04) + (assignment2 * 0.04) + (assignment3 * 0.04) + (assignment4 * 0.04) + ((midterm1 * 0.125) + (midterm2 * 0.125)) + (final * 0.18) + (prep * 0.06)
finalGrade = round(finalGrade)
print(f"Your grade is: {finalGrade}.")
