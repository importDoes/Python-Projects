# Problem Number 2: Different Syntax of print() - Student Information
# Programmed by "Ryan Dexter Libres"

student_num = "2021-001"
student_name = "Maestro Andoy"
age = 21
is_male = True
avg_grade = 1.25

#Version 1: Use print(object-list with comma separator)
def version_1():
    print("Student Number :", student_num)
    print("Student Name :", student_name)
    print("Age :", age)
    print("Are you a male? :", is_male)
    print("Average Grade :", avg_grade)
    print("Welcome", student_name + ", your student number is " + student_num + " and your age is " + str(age) + "!")

#Version 2: Use print(String concatenation)
def version_2():
    print("Student Number : " + student_num)
    print("Student Name : " + student_name)
    print("Age : " + str(age))
    print("Are you a male? : " + str(is_male))
    print("Average Grade : " + str(avg_grade))
    print("Welcome " + student_name + ", your student number is " + student_num + " and your age is " + str(age) + "!")

#Version 3: Use print(F-String or formatted-string)
def version_3():
    print(f"Student Number : {student_num}")
    print(f"Student Name : {student_name}")
    print(f"Age : {age}")
    print(f"Are you a male? : {is_male}")
    print(f"Average Grade : {avg_grade}")
    print(f"Welcome {student_name}, your student number is {student_num} and your age is {age}!")

#Version 4: Use print(String.format "{}") with format method
def version_4():
    print("Student Number : {}".format(student_num))
    print("Student Name : {}".format(student_name))
    print("Age : {}".format(age))
    print("Are you a male? : {}".format(is_male))
    print("Average Grade : {}".format(avg_grade))
    print("Welcome {}, your student number is {} and your age is {}!".format(student_name, student_num, age))

#Version 5: Use print (format specifier % - C Language style)
def version_5():
    print("Student Number : %s" % student_num)
    print("Student Name : %s" % student_name)
    print("Age : %d" % age)
    print("Are you a male? : %r" % is_male)
    print("Average Grade : %.2f" % avg_grade)
    print("Welcome %s, your student number is %s and your age is %d!" % (student_name, student_num, age))


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
