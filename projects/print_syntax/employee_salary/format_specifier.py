# Problem 5 – Solution 5
# Programmed by John Carlo O. Aguilar
employee = "Pedro Reyes"
position = "IT Support Specialist"
company = "ABC Technologies"
days = 22
rate = 1200
salary = days* rate

print ("\n\n---------------------------------------------------------")
# Version 5: Use print (format specifier % - C Language stype)
print ("Employee %s works as an %s." % (employee, position))
print ("He is employed by %s." % (company))
print ("He worked for %d days and his daily rate is %d." % (days, rate))
print ("His total salary is %d.\n" % (salary))

print ("Thank you for your hard work, %s!" % (employee))