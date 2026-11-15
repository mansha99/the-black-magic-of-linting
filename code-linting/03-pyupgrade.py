"""
Violation:
pyupgrade("UP")
- Use format specifiers instead of percent format

Running:
ruff check 03-pyupgrade.py
"""

country = "India"
message = "I love my %s" % country  
print(message)
