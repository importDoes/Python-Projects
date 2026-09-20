# Problem 4 – Solution 2
# Programmed by John Carlo O. Aguilar
customer = "Maria Santos"
product = "Laptop Bag"
store = "Tech Store"
qty = 3
uprice = 750
totamt = qty* uprice

print ("\n\n---------------------------------------------------------")
# Version 2 : Use print [String concatenation]
print ("Customer " + customer, " purchase from " + store + ".")
print ("Product ordered: " + product + ".")
print ("Quantity ordered: " + str(qty) + ".")
print ("The unit price of " + product + "is" + str(uprice) + ".")
print ("The total amount to pay is " + str(totamt) + ".\n")

print ("Thank you, " + customer + ", for your purchase" + "!")
