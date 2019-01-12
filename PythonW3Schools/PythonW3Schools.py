#testing short comments
""" Testing a longer comment
that is multi line. """
print("Hello world.")

x = 4 # x should be an int for now.
print(x)
x = "Sally" #now x is a String
print(x)
#yup it works
"""
Variables MUST start with a letter or the underscorce _ char
cannot start with a number 1234var (NO!)
can only be letters, _ and numbers (nums after ex: ha123ha is good)
CASE SENSITIVE 
"""

x = 5
y = 10
print(x+y)
z = x+y
print(z)

#test scientific numbers with e and printing.
print()
print("Testing scientific numbers and printing to see what looks like")

x = 35e3
y = 12E4
z = -87.7e100

print("x assigned 35e3 and prints...")
print(x)
print("y assigned 12E4 and prints...")
print(y)
print("z assigned -87.7e100 and prints...")
print(z)
