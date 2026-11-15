"""
Violation:
pycodestyle ("E") and Naming ("N")
- Split imports
- Import block is un-sorted or un-formatted
- Class name `foo` should use CapWords convention

Running:
ruff check 01-pycodestyle.py
"""

import os, sys


class foo:
    pass


print(os.name)
print(sys.path)
