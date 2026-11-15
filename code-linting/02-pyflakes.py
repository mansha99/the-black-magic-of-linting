'''
Violation:  
Pyflakes("F")
- Imported module is never used
- Local variable assigned but never used

Running:
ruff check 02-pyflakes.py
'''
import os  

x = 5  
y = 10
print(f" y is {y}")

