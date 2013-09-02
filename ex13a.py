from sys import argv

# unpacks argv
script, first_name, last_name = argv

# string replacement
print "Your first name and last name: %s, %s " % (
    first_name, last_name
)
