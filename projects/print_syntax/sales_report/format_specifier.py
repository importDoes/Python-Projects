# Problem 1 – Solution 5
# Programmed by John Carlo O. Aguilar
cust_name = "Maestro Andoy"
city = "Manila City"
item = "Wireless Mouse"
quantity = 2
price = 250
bill = quantity * price

print ("\n\n---------------------------------------------------------")
# Version 5: Use print (format specifier % - C Language style)
print ("Welcome Customer %s from %s!\n" % (cust_name, city))
print ("You ordered %d %s." % (quantity, item))
print ("The unit price of %s is %d." % (item, price))
print ("Your total charge is %d.\n" % (bill))
print ("Thank you for supporting our business, %s!" % (cust_name))