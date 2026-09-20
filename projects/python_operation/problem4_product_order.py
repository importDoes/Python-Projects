# Problem Number 4: Different Syntax of print() - Product Order
# Programmed by "Ryan Dexter Libres"

customer = "Maria Santos"
product = "Laptop Bag"
store = "Tech Store"
qty = 3
uprice = 750
totamt = qty * uprice

#Version 1: Use print(object-list with comma separator)
def version_1():
    print("Customer", customer, "purchased from", store + ".")
    print("Product ordered:", product + ".")
    print("Quantity ordered:", str(qty) + ".")
    print("The unit price of", product, "is", str(uprice) + ".")
    print("The total amount to pay is", str(totamt) + ".")
    print("Thank you,", customer + ", for your purchase!")

#Version 2: Use print(String concatenation)
def version_2():
    print("Customer " + customer + " purchased from " + store + ".")
    print("Product ordered: " + product + ".")
    print("Quantity ordered: " + str(qty) + ".")
    print("The unit price of " + product + " is " + str(uprice) + ".")
    print("The total amount to pay is " + str(totamt) + ".")
    print("Thank you, " + customer + ", for your purchase!")

#Version 3: Use print(F-String or formatted-string)
def version_3():
    print(f"Customer {customer} purchased from {store}.")
    print(f"Product ordered: {product}.")
    print(f"Quantity ordered: {qty}.")
    print(f"The unit price of {product} is {uprice}.")
    print(f"The total amount to pay is {totamt}.")
    print(f"Thank you, {customer}, for your purchase!")

#Version 4: Use print(String.format "{}") with format method
def version_4():
    print("Customer {} purchased from {}.".format(customer, store))
    print("Product ordered: {}.".format(product))
    print("Quantity ordered: {}.".format(qty))
    print("The unit price of {} is {}.".format(product, uprice))
    print("The total amount to pay is {}.".format(totamt))
    print("Thank you, {}, for your purchase!".format(customer))

#Version 5: Use print (format specifier % - C Language style)
def version_5():
    print("Customer %s purchased from %s." % (customer, store))
    print("Product ordered: %s." % product)
    print("Quantity ordered: %d." % qty)
    print("The unit price of %s is %d." % (product, uprice))
    print("The total amount to pay is %d." % totamt)
    print("Thank you, %s, for your purchase!" % customer)


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
