# Problem 5 – Solution 4
# Programmed by John Carlo O. Aguilar
employee = "Pedro Reyes"
position = "IT Support Specialist"
company = "ABC Technologies"
days = 22
rate = 1200
salary = days* rate

print ("\n\n---------------------------------------------------------")
# Version 4 : Use print [String.format "{}"] with format method
print ("Employee {0} works as an {1}.".format(employee, position))
print ("He is employed by {}.".format(company))
print ("He worked for {0} days and his daily rate is {1}.".format(days, rate))
print ("His total salary is {}.\n".format(salary))

print ("Thank you for your hard work, {}!".format(employee))