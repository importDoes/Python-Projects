# Problem 1 – Solution 4
# Programmed by John Carlo O. Aguilar
cust_name = "Maestro Andoy"
city = "Manila City"
item = "Wireless Mouse"
quantity = 2
price = 250
bill = quantity * price

print ("\n\n---------------------------------------------------------")
# Version 4: Use print(String.format "{}") with format method
print ("Welcome Customer {0} from {1}!\n".format(cust_name, city))
print ("You ordered {0} {1}.".format(quantity, item))
print ("The unit price of {0} is {1}.".format(item, price))
print ("Your total charge is {0}.\n".format(bill))
print ("Thank you for supporting our business, {0}!".format(cust_name))