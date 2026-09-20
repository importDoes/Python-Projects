# Problem 1 – Solution 3
# Programmed by John Carlo O. Aguilar
cust_name = "Maestro Andoy"
city = "Manila City"
item = "Wireless Mouse"
quantity = 2
price = 250
bill = quantity * price

print ("\n\n---------------------------------------------------------")
# Version 3: Use print(F-String or formatted-string)
print (f"Welcome Customer {cust_name} from {city}!\n")
print (f"You ordered {quantity} {item}.")
print (f"The unit price of {item} is {price}.")
print (f"Your total charge is {bill}.\n")
print (f"Thank you for supporting our business, {cust_name}!")