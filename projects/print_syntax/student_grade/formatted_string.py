# Problem 3 – Solution 3
# Programmed by John Carlo O. Aguilar
studname = "Juan Dela Cruz"
course = "BS Information Technology"
score = 85
items = 100
percentage = (score/items) * 100

print ("\n\n---------------------------------------------------------")
# Version 3 : Use print [F-String or formatted-string]
print (f"Student {studname} is enrolled in {course}.")
course = "Python Programming"
print (f"He is taking {course}.")
print (f"{studname} obtained a score of {score} out of {items}.") 
print (f"His percentage score is {int(percentage)}%\n")

print (f"Congratualation, {studname}!\n")