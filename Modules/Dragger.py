import ctypes
import sys as _sys
from ctypes.wintypes import POINT


class D:
    def __init__(s, w):
        if _sys.platform != "win32":
            raise OSError("WindowDragger requires Windows")
        s.w = w
        s.g = False
        s.o = (0, 0)
        s.u = ctypes.windll.user32

    def mpos(s):
        p = POINT()
        if not s.u.GetCursorPos(ctypes.byref(p)):
            raise ctypes.WinError()
        return p.x, p.y

    def grab(s):
        mx, my = s.mpos()
        wx, wy = s.w.position
        s.o = (mx - wx, my - wy)
        s.g = True

    def drop(s):
        s.g = False

    def tick(s):
        if s.g:
            mx, my = s.mpos()
            s.w.position = (mx - s.o[0], my - s.o[1])
