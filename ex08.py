# Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.")

# Reflections:
# 1.  %r should be used with caution. Use it in debugging only.