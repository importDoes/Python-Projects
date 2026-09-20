# Problem 4 – Solution 4
# Programmed by John Carlo O. Aguilar
customer = "Maria Santos"
product = "Laptop Bag"
store = "Tech Store"
qty = 3
uprice = 750
totamt = qty* uprice

print ("\n\n---------------------------------------------------------")
# Version 4 : Use print [String.format "{}"] with format method
print ("Customer {0} purchase from {1}.".format(customer, store))
print ("Product ordered: {}.".format(product))
print ("Quantity ordered: {}.".format(qty))
print ("The total amount to pay is {}.\n".format(totamt))

print ("Thank you, {} for your purchase!".format(customer))