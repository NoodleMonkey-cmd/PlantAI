Sprout = [100, 200, 300]


class P:
    def __init__(s):
        s.pts = 0

    def ap(s, amt):
        if isinstance(amt, bool) or not isinstance(amt, (int, float)):
            raise TypeError("Flag 6")
        if amt < 0:
            raise ValueError("Flag 6")
        s.pts += amt
