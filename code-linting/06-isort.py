"""
Violation:
isort("I")
- Split imports
- Import block is un-sorted or un-formatted
Running:
ruff check 06-isort.py
"""

from os import path
import sys

print(path)
print(sys.path)
