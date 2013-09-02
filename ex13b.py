# JUNK new lines do not work
from sys import argv

# set the raw inputs
girl = raw_input('girl: ')
year = raw_input('year: ')
happy = raw_input('happy:')

# unpack argv with girl, year, and happy
name, girl, year, happy = argv

# get new line to work
argv_print = "Her name: %r /n The year:%r /n happy:%r /n" % (
    girl, year, happy
)

print argv_print