import json as _j
from pathlib import Path as _P


def add_animation(data):
    try:
        _j.dumps(data)
    except (TypeError, ValueError) as e:
        raise TypeError("Flag 3") from e
    with open(_P(__file__).resolve().parent / "Saved_Animation.json", "w", encoding="utf-8") as f:
        _j.dump(data, f, indent=4, ensure_ascii=False)


class A:
    def __init__(s):
        s.f = []
        s.i = 0

    def set(s, frames, idx):
        if not frames:
            raise ValueError("Flag 4")
        if not 0 <= idx < len(frames):
            raise ValueError("Flag 4")
        s.f = frames
        s.i = idx

    def _cur(s):
        if not s.f:
            raise ValueError("Flag 5")
        if not 0 <= s.i < len(s.f):
            raise IndexError("Flag 5")
        return s.f[s.i]

    def rc(s):
        return s._cur().get_rect(center=(180, 225))

    def dr(s, d):
        d.blit(s._cur(), s.rc())

    def ix(s):
        return s.i

    def nxt(s):
        if s.i < len(s.f) - 1:
            s.i += 1
            return True
        return False
