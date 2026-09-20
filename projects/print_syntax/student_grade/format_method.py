# Problem 3 – Solution 4
# Programmed by John Carlo O. Aguilar
studname = "Juan Dela Cruz"
course = "BS Information Technology"
score = 85
items = 100
percentage = (score/items) * 100

print ("\n\n---------------------------------------------------------")
# Version 4 : Use print [String.format "{}"] with format method
print ("Student {0} is enrolled in {1}.".format(studname, course))
course = "Python Programming"
print ("He is taking {}.".format(course))
print ("{0} obtained a score of {1} out of {2}.".format(studname, score, items))
print ("His percentage score is {}%\n".format(int(percentage)))

print ("Congratualation {}!\n".format(studname))