# pull in argv
from sys import argv

# unpack argv
script, filename = argv

print "########################################"
print "#Welcome to the simple file editor 9000#"
print "########################################"
print "This file %r, is marked to be cleaned" % filename
# prompt user for input
print "To continue hit ENTER or else CTRL-C (^C)."
raw_input("CTRL-C or ENTER")
print "Are you sure?"
raw_input("CTRL-C or ENTER")

print "Opening the file..."
# open file from user input
target = open(filename, 'w+')

#print "Truncating the file. Goodbye!"
# clear the target file
#target.truncate()

print "Enter words you want in the file"

# grab raw input from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

# write to each line and print a new line
target.write("%s\n%s\n%s\n" % (
    line1, line2, line3)
)

print "Closing File, Goodbye."
# close the file
target.close()