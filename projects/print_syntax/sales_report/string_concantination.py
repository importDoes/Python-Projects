# Problem 1 – Solution 2
# Programmed by John Carlo O. Aguilar
cust_name = "Maestro Andoy"
city = "Manila City"
item = "Wireless Mouse"
quantity = 2
price = 250
bill = quantity * price

print ("\n\n---------------------------------------------------------")
# Version 2 : Use print [String concatenation]
print ("Welcome Customer " + cust_name + " from " + city + "!\n")
print ("You ordered " + str(quantity) + " " + item + ".")
print ("The unit price of " + item + " is " + str(price) + ".")
print ("Your total charge is " + str(bill) + ".\n")
print ("Thank you for supporting our business, " + cust_name + "!")