"""
Check Uppercase or Lowercase
Take a character input and check if it is positive,negative or zero.
"""
c = input("Enter a single character: ")

if c.isupper():
    print("Uppercase letter")
elif c.islower():
    print("Lowercase letter")
else:
    print("Not a letter")
