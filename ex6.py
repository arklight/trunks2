# Number of people
x = "There are %d types of people." % 10
# set binary value
binary = "binary"
# set not binary value
do_not = "don't"
# add both strings together
y = "Those who know %s and those who %s." % (binary, do_not)

# print both lines
print x
print y

# print number of people
print "I said %r." % x
# print who knows binary and who does not
print "I also said: '%s'." % y

# set joke to false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# this prints the set
print joke_evaluation % hilarious

# values for left and right side of string
w = "This is the left side of..."
e = "a string with a right side."

# print that
print w + e