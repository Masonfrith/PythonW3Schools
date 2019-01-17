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

#What the heck are complex numbers with this j stuff in them?

x = 3+5j
y = 5j
z = -5j

print()
print("Testing complext numbers printing")
print("x assigned 3+5j and prints...")
print(x)
print("y assigned 5j and prints...")
print(y)
print("z assigned -5j and prints...")
print(z)

print()
print("Testing substring stuff")

s = "0123456789"
print(s)
print("Print from position '3', which should be 3, because both of us started at 0")
print(s[3])
print("print from position 2 to 5, which will be?")
print(s[2:5])

print("Enter your name:")
name = input()
print("Hello, " + name)

Yello = "If you see this, var Yello, did not work as expected!:"
Yello = input("Putname again, testing asking using the input() function\n")
print("Testing var Yello: " + Yello)