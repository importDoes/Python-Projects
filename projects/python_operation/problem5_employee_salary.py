# Problem Number 5: Different Syntax of print() - Employee Salary
# Programmed by "Ryan Dexter Libres"

employee = "Pedro Reyes"
position = "IT Support Specialist"
company = "ABC Technologies"
days = 22
rate = 1200
salary = days * rate

#Version 1: Use print(object-list with comma separator)
def version_1():
    print("Employee", employee, "works as an", position + ".")
    print("He is employed by", company + ".")
    print("He worked for", days, "days and his daily rate is", str(rate) + ".")
    print("His total salary is", str(salary) + ".")
    print("Thank you for your hard work,", employee + "!")

#Version 2: Use print(String concatenation)
def version_2():
    print("Employee " + employee + " works as an " + position + ".")
    print("He is employed by " + company + ".")
    print("He worked for " + str(days) + " days and his daily rate is " + str(rate) + ".")
    print("His total salary is " + str(salary) + ".")
    print("Thank you for your hard work, " + employee + "!")

#Version 3: Use print(F-String or formatted-string)
def version_3():
    print(f"Employee {employee} works as an {position}.")
    print(f"He is employed by {company}.")
    print(f"He worked for {days} days and his daily rate is {rate}.")
    print(f"His total salary is {salary}.")
    print(f"Thank you for your hard work, {employee}!")

#Version 4: Use print(String.format "{}") with format method
def version_4():
    print("Employee {} works as an {}.".format(employee, position))
    print("He is employed by {}.".format(company))
    print("He worked for {} days and his daily rate is {}.".format(days, rate))
    print("His total salary is {}.".format(salary))
    print("Thank you for your hard work, {}!".format(employee))

#Version 5: Use print (format specifier % - C Language style)
def version_5():
    print("Employee %s works as an %s." % (employee, position))
    print("He is employed by %s." % company)
    print("He worked for %d days and his daily rate is %d." % (days, rate))
    print("His total salary is %d." % salary)
    print("Thank you for your hard work, %s!" % employee)


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
