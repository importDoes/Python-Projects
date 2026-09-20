# Problem 3 – Solution 2
# Programmed by John Carlo O. Aguilar
studname = "Juan Dela Cruz"
course = "BS Information Technology"
score = 85
items = 100
percentage = (score/items) * 100

print ("\n\n---------------------------------------------------------")
# Version 2 : Use print [String concatenation]
print ("Student " + studname + " is enrolled in " + course + ".")
course = "Python Programming"
print ("He is taking " + course + ".")
print (studname + " obtained a score of " + str(score) + " out of " + str(items) + ".")
print ("His percentage score is " + str(int(percentage)) + "%\n")

print ("Congratualation, " + studname +"!")