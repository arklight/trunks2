# name
name = 'Brandon Freeman'
# age
age = 25  # not a lie
#d_age = 365 * 25
# height
height = 72  # inches
#f_height = 72 / 12
# weight
weight = 195  # lbs
#k_weight = 2 / weight
# eye color
eyes = 'Brown'
# teeth color
teeth = 'White'
# hair color
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth  are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %r." % (
    age, height, weight, age + height + weight
)
#print "If I add %j, %t, and %e, I get %r." % (
#    d_age, f_height, k_weight, d_age + f_height + k_weight
#)
