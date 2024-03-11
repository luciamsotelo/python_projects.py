# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello ():
  print("Hello, User")


# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(firstname,lastname,email)
  return[firstname,lastname,email]


# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat {food_list[0]}")
        for food in food_list[1:]:
            print("Next I eat {food}")

# call the functions in order of how they should print

hello()

print (pack("firstname", "lastname", "email"))

eat_lunch(["sandwich", "fruit", "chips"])
