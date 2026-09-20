# Problem 5 – Solution 1
# Programmed by John Carlo O. Aguilar
employee = "Pedro Reyes"
position = "IT Support Specialist"
company = "ABC Technologies"
days = 22
rate = 1200
salary = days* rate

print ("\n\n---------------------------------------------------------")
# Version 1 : Use print [Object-list with comma separator]
print ("Employee", employee, "works as an", position, end=".\n")
print ("He is employed by", company, end=".\n")
print ("He worked for ", days, " days and his daily rate is ", rate, sep="", end=".\n")
print ("His total salary is ", salary, sep="", end=".\n\n")

print ("Thank you for your hard work, ", employee, sep="", end="!\n")
