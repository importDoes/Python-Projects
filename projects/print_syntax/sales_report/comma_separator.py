# Problem 1 – Solution 1
# Programmed by John Carlo O. Aguilar
cust_name = "Maestro Andoy"
city = "Manila City"
item = "Wireless Mouse"
quantity = 2
price = 250
bill = quantity * price

print ("\n\n---------------------------------------------------------")
# Version 1: Use print(object-list with comma separator)
print ("Welcome Customer", cust_name, "from", city, end = "!\n\n")
print ("You ordered ", quantity, " ", item, ".", sep="")
print ("The unit price of", item, "is", price, end = ".\n")
print ("Your total charge is", bill, end = ".\n\n")
print ("Thank you for supporting our business, ", cust_name, sep="", end="!")
