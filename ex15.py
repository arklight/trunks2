# this needs the sample file ex15_sample.txt noted here
# first line: This is stuff I typed into a file.
# second line: It is really cool stuff.
# third line: Lots and lots of fun to have in here.

# this line imports a module that allows this script to take user input
from sys import argv

# unpack argv with 2 arguments
script, filename = argv
# prompt value
prompt = '-->'

# make a var and pass open argv input filename
# this will open the name of the file if it is in current path
text = open(filename)

# print lol
print "Here's your file %r" % filename
# new var for file_again
file_again = raw_input(prompt)

# access file_again with open and set var to text again
text_again = open(file_again)

# this is interesting, read text again
print text_again.read()


