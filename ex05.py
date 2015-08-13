name = 'Ming Ruan'
age = 25 # not a lie
height = 67  # inches
weight = 120 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about this %s." % name
print "He's %r inches tall." % height   #try use %r isto %d
print "He's %d points heavy." % weight
print "Actually that's quite light."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teetch are usually %s depending on the coffee." % teeth

# this line is tricky, get it right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
