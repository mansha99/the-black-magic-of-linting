"""
Violation:
flake8-bugbear("B")
- Do not perform function call `os.getcwd` in argument defaults; 
instead, perform the call within the function

Running:
ruff check 04-bugbear.py
"""

import os

def print_dir_name(dir_name=os.getcwd()):
    print(f"{dir_name}")


