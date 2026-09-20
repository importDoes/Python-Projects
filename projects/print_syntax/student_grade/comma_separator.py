# Problem 3 – Solution 1
# Programmed by John Carlo O. Aguilar
studname = "Juan Dela Cruz"
course = "BS Information Technology"
score = 85
items = 100
percentage = (score/items) * 100

print ("\n\n---------------------------------------------------------")
# Version 1 : Use print [Object-list with comma separator]
print ("Student", studname, "is enrolled in", course, end=".\n")
course = "Python Programming"
print ("He is taking", course, end=".\n")
print (studname, "obtained a score of", score, "out of", items, end=".\n")
print ("His percentage score is ", int(percentage), sep="", end="%\n\n")

print ("Congratualation,", studname, end="!\n")
