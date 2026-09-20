# Problem 4 – Solution 5
# Programmed by John Carlo O. Aguilar
customer = "Maria Santos"
product = "Laptop Bag"
store = "Tech Store"
qty = 3
uprice = 750
totamt = qty* uprice

print ("\n\n---------------------------------------------------------")
# Version 5: Use print (format specifier % - C Language stype)
print ("Customer %s purchase from %s." % (customer, store))
print ("Product ordered: %s." % (product))
print ("Quantity ordered: %d." % (qty))
print ("The total amount to pay is %d.\n" % (totamt))

print ("Thank you, %s for your purchase!" % (customer))