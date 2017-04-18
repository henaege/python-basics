# print "Hello, World!"
# print("hello, World", "Again")

print """This will
ignore the new lines
until it sees
three double quotes"""

print"Let's change something and push again."

# Variables - string, number, letters or anything made with the keyboard
# and you want to stash something that's not fast into something fast.
# There is no declaration
# Python is not heavily typed (data type doesn't need to be declared)

the_meaning_of_life = 40 + 2

# Data Types:
# - Strings
# - Numbers (Ints, Floats)
# - Booleans (True/False)
# - Lists (list of variables in one variable)
# - Dictionary (variables of variables)
# - Objects

# Strings
first_name = "Drew"
last_name = "Tolliver"
print "Hello {} {}".format(first_name, last_name)

# Floats
pi_the_magic_float = 3.14
print pi_the_magic_float
print type(pi_the_magic_float)
make_me_an_integer = int(pi_the_magic_float)
print make_me_an_integer

# Booleans
the_truth = True
print type(the_truth)
the_lie = False
print type(the_lie)

# Raw Input
first_name = raw_input("First Name: ")
last_name = raw_input("Last Name: ")


# Conditionals
#  1 = assigns the value on the right to the variable on the left
#  2 = compares what's on the left to what's on the right

if(first_name == last_name):
  print "Your first name is the same as your last name?"

age = raw_input("How old are you? ")
age_as_int = int(age)
if age_as_int >= 21:
  print "You can buy beer."

