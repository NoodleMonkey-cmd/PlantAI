import json as _j
from pathlib import Path as _P

F = _P(__file__).resolve().parent / "Saved_Data.json"


class V:
    def __init__(s, a, p):
        s.a = a
        s.p = p

    def sv(s):
        d = {"animation_index": s.a.i, "points": s.p.pts}
        try:
            _j.dumps(d)
        except (TypeError, ValueError) as e:
            raise TypeError("Flag 8") from e
        with open(F, "w", encoding="utf-8") as f:
            _j.dump(d, f, indent=4, ensure_ascii=False)

    def ld(s):
        if not F.is_file():
            return False
        with open(F, "r", encoding="utf-8") as f:
            d = _j.load(f)
        if not isinstance(d, dict):
            raise ValueError("Flag 8")
        i, p = d.get("animation_index"), d.get("points")
        if (isinstance(i, bool) or not isinstance(i, int)) or (isinstance(p, bool) or not isinstance(p, (int, float))):
            raise TypeError("Flag 8")
        if not 0 <= i < len(s.a.f) or p < 0:
            raise ValueError("Flag 8")
        s.a.i = i
        s.p.pts = p
        return True
