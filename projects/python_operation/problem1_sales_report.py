# Problem Number 1: Different Syntax of print() - Sales Report
# Programmed by "Ryan Dexter Libres"

cust_name = "Maestro Andoy"
city = "Manila City"
item = "Wireless Mouse"
quantity = 2
price = 250
bill = quantity * price

#Version 1: Use print(object-list with comma separator)
def version_1():
    print("Welcome Customer", cust_name, "from", city, end="!")
    print()
    print("You ordered", quantity, item, end=".")
    print()
    print("The unit price of", item, "is", price, end=".")
    print()
    print("Your total charge is", bill, end=".")
    print()
    print("Thank you for supporting our business,", cust_name, end="!")
    print()

#Version 2: Use print(String concatenation)
def version_2():
    print("Welcome Customer " + cust_name + " from " + city + "!")
    print("You ordered " + str(quantity) + " " + item + ".")
    print("The unit price of " + item + " is " + str(price) + ".")
    print("Your total charge is " + str(bill) + ".")
    print("Thank you for supporting our business, " + cust_name + "!")

#Version 3: Use print(F-String or formatted-string)
def version_3():
    print(f"Welcome Customer {cust_name} from {city}!")
    print(f"You ordered {quantity} {item}.")
    print(f"The unit price of {item} is {price}.")
    print(f"Your total charge is {bill}.")
    print(f"Thank you for supporting our business, {cust_name}!")

#Version 4: Use print(String.format "{}") with format method
def version_4():
    print("Welcome Customer {} from {}!".format(cust_name, city))
    print("You ordered {} {}.".format(quantity, item))
    print("The unit price of {} is {}.".format(item, price))
    print("Your total charge is {}.".format(bill))
    print("Thank you for supporting our business, {}!".format(cust_name))

#Version 5: Use print (format specifier % - C Language style)
def version_5():
    print("Welcome Customer %s from %s!" % (cust_name, city))
    print("You ordered %d %s." % (quantity, item))
    print("The unit price of %s is %d." % (item, price))
    print("Your total charge is %d." % bill)
    print("Thank you for supporting our business, %s!" % cust_name)


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
