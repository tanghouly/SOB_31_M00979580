# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))#need to ad int for type of data which is integer

exam_three = int(input("Input exam grade three: "))#added int again for input

grades = [exam_one, exam_two ,exam_three]#commas  added and defined properly logical mistake
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)#not spelled properly

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:#colon added
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"#need double quotes for syntax
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:#change to else rather than elif
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grades))#must be defined as grades to print as list

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))
    break#break added to exit loop

if letter_grade is "F":#must be the same variable with "_"
    print ("Student is failing.")#brackets added to print
else:
    print( "Student is passing.")
