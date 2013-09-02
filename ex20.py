# imports
from sys import argv

# unpack argv
script, input_file = argv


# print all function
def print_all(f):
    print f.read()


# seeks to the beginning of the file
def rewind(f):
    f.seek(0)


# prints a line out of user inputted file
# note extra comma at end of print line
# this stops \n from adding space between
# the lines
def print_a_line(line_count, f):
    print line_count, f.readline(),

# open input file
current_file = open(input_file)

print "First let's print the whole file:\n"

#prints the contents of the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# set the cursor to the start of the file
rewind(current_file)

print "Let's print three lines:"

# set current line to 1
current_line = 1
print_a_line(current_line, current_file)

# add current line and value 1 together to make second line
current_line += 1
print_a_line(current_line, current_file)

# move to the next line
current_line += 1
print_a_line(current_line, current_file)