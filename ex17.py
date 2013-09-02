from sys import argv
# fix this later
import os

script, file_one, file_two = argv

print "Copying file from %s to %s" % (file_one, file_two)

from_file = open(file_one)
copy_data = from_file.read()

print "The input file is %d bytes long" % len(copy_data)

if os.path.exists(file_two):
    print "ERROR FILE %r EXISTS" % file_two
else:
    out_file = open(file_two, 'w+')
    out_file.write(copy_data)

    print "Alright, Done!"
    print "Goodbye."
    out_file.close()
    from_file.close()