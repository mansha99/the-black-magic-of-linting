"""
Violation:
- unused method 'perimeter' (60% confidence)

Running:
uv run vulture 07-vulture.py
"""
class Rect:
    def __init__(self, l: int, b: int):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)


if __name__ == "__main__":
    r = Rect(3, 4)
    print(f"Area is {r.area()}")


