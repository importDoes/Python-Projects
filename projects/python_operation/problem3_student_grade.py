# Problem Number 3: Different Syntax of print() - Student Grades
# Programmed by "Ryan Dexter Libres"

student_name = "Juan Dela Cruz"
course = "BS Information Technology"
subject = "Python Programming"
score = 85
items = 100
percentage = (score / items) * 100

#Version 1: Use print(object-list with comma separator)
def version_1():
    print("Student", student_name, "is enrolled in", course + ".")
    print("He is taking", subject + ".")
    print("Juan Dela Cruz obtained a score of", score, "out of", str(items) + ".")
    print("His percentage score is", str(int(percentage)) + "%.")
    print("Congratulations,", student_name + "!")

#Version 2: Use print(String concatenation)
def version_2():
    print("Student " + student_name + " is enrolled in " + course + ".")
    print("He is taking " + subject + ".")
    print("Juan Dela Cruz obtained a score of " + str(score) + " out of " + str(items) + ".")
    print("His percentage score is " + str(int(percentage)) + "%.")
    print("Congratulations, " + student_name + "!")

#Version 3: Use print(F-String or formatted-string)
def version_3():
    print(f"Student {student_name} is enrolled in {course}.")
    print(f"He is taking {subject}.")
    print(f"Juan Dela Cruz obtained a score of {score} out of {items}.")
    print(f"His percentage score is {int(percentage)}%.")
    print(f"Congratulations, {student_name}!")

#Version 4: Use print(String.format "{}") with format method
def version_4():
    print("Student {} is enrolled in {}.".format(student_name, course))
    print("He is taking {}.".format(subject))
    print("Juan Dela Cruz obtained a score of {} out of {}.".format(score, items))
    print("His percentage score is {}%.".format(int(percentage)))
    print("Congratulations, {}!".format(student_name))

#Version 5: Use print (format specifier % - C Language style)
def version_5():
    print("Student %s is enrolled in %s." % (student_name, course))
    print("He is taking %s." % subject)
    print("Juan Dela Cruz obtained a score of %d out of %d." % (score, items))
    print("His percentage score is %d%%." % int(percentage))
    print("Congratulations, %s!" % student_name)


if __name__ == "__main__":
    print("VERSION 1")
    version_1()
    print()

    print("VERSION 2")
    version_2()
    print()

    print("VERSION 3")
    version_3()
    print()

    print("VERSION 4")
    version_4()
    print()

    print("VERSION 5")
    version_5()
