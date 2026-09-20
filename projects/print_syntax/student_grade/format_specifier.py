# Problem 3 – Solution 5
# Programmed by John Carlo O. Aguilar
studname = "Juan Dela Cruz"
course = "BS Information Technology"
score = 85
items = 100
percentage = (score/items) * 100

print ("\n\n---------------------------------------------------------")
# Version 5: Use print (format specifier % - C Language stype)
print ("Student %s is enrolled in %s."% (studname, course))
course = "Python Programming"
print ("He is taking %s." % (course))
print ("%s obtained a score of %d out of %d." % (studname, score, items))
print ("His percentage score is %d%%\n" % (percentage))

print ("Congratualation %s!\n"%(studname))