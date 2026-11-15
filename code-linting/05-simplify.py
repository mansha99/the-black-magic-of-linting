"""
Violation:
flake8-simplify("SIM")
- SIM103: needless-bool 
Running:
ruff check 05-simplify.py
"""
def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


