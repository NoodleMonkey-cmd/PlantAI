Sprout = [1, 20, 50]
Sprout_Name = [
    "Small Sprout",
    "Developing Sprout",
    "Pre-mature Sprout",
    "Full-Grown Tree",
]

class PointSystem:
    def __init__(self):
        self.points = 0

    def add_point(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Flag 6")
        if amount < 0:
            raise ValueError("Flag 6")
        self.points += amount
