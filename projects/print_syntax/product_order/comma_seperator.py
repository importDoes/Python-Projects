# Problem 4 – Solution 1
# Programmed by John Carlo O. Aguilar
customer = "Maria Santos"
product = "Laptop Bag"
store = "Tech Store"
qty = 3
uprice = 750
totamt = qty* uprice

print ("\n\n---------------------------------------------------------")
# Version 1 : Use print [Object-list with comma separator]
print ("Customer", customer, "purchase from", store, end=".\n")
print ("Product ordered:", product, end=".\n")
print ("Quantity ordered:", qty, end=".\n")
print ("The unit price of", product, "is", uprice, end=".\n")
print ("The total amount to pay is", totamt, end=".\n\n")

print ("Thank you, ", customer, ", for your purchase", sep="", end="!\n")
