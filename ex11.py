# Asking questions

print "How old are you?", #comma prevents print adding \n at the end
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy" % (
	age, height, weight)