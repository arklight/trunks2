# age of the person
age = raw_input("How old are you? ")
# how tall the person is
height = raw_input("How tall are you? ")
# how heavy this person is
weight = raw_input("How much do you weigh? ")

# the percent r is taking raw input from the values of what is
# defined in the ()
print "So, you are %r years old, %r tall and %r heavy." % (
    age, height, weight
)